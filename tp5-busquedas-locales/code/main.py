from algorithms import *
import pandas as pd

sizes = [4,8,10,12,15]

# max_iterations es por defecto 1000 para todos los casos.

def run():

    global sizes

    def iterate(s):
        algorithms = [hill_climbing, simulated_annealing, genetic, genetic2]
        results = [
            (algorithm.__name__, s, *result)
            for _ in range(30)
            for algorithm in algorithms
            for result in [algorithm(s)]
        ]
        return results

    print("Executing!")

    all_results = []
    for size in sizes:
        start = time.time()
        print(f"Running for size {size}...")
        results = iterate(size)
        all_results.extend(results)
        end = time.time() - start
        print(f"Finished! Time elapsed for size {size}: {end}")

    
    print("Creating DataFrame...")
    df = pd.DataFrame(all_results, columns=['algorithm_name', 'size', 'solution', 'generations', 'time', 'conflicts'])

    df.to_csv('results.csv', index=False)

def plot():

    print("Plotting results...")

    df = pd.read_csv('results.csv')

    success_rate = df.groupby(['algorithm_name', 'size']).apply(lambda x: (x['conflicts'] == 0).mean()).reset_index()
    success_rate.columns = ['algorithm_name', 'size', 'success_rate']

    import matplotlib.pyplot as plt
    import seaborn as sns # type: ignore

    plt.figure(figsize=(10, 6))
    sns.barplot(data=success_rate, x='size', y='success_rate', hue='algorithm_name')
    plt.title('Success Rate by Algorithm and Size')
    plt.xlabel('Size')
    plt.ylabel('Success Rate')
    plt.legend(title='Algorithm')
    plt.savefig('images/success_rate.png')


    by_time = df.groupby(['algorithm_name', 'size'])['time'].agg(['mean', 'std']).reset_index()
    by_time.columns = ['algorithm_name', 'size', 'mean_time', 'std_time']

    print("Mean and Std. Deviation of time elapsed:")
    print(by_time)

    plt.figure(figsize=(10,6))
    sns.barplot(data=by_time, x='size', y='mean_time', hue='algorithm_name', errorbar='sd')
    plt.title('Mean Execution Time by Algorithm and Size')
    plt.xlabel('Size')
    plt.ylabel('Mean Execution Time (s)')
    plt.legend(title='Algorithm')
    plt.savefig('images/mean_execution_time.png')

    algorithms = df['algorithm_name'].unique()
    for algorithm in algorithms:
        subset = df[df['algorithm_name']==algorithm]
        plt.figure(figsize=(16,8))
        sns.boxplot(data=subset, hue='size', y='time',legend=False, palette='Set3')
        plt.title(f'Variation of Execution Time by Size for {algorithm}')
        plt.xlabel('Size')
        plt.ylabel('Time (s)')
        plt.savefig(f'images/{algorithm}_time_boxplot.png')
    
    for algorithm in algorithms:
        subset = df[df['algorithm_name']==algorithm]
        plt.figure(figsize=(16,8))
        sns.boxplot(data=subset, hue='size', y='generations',legend=False, palette='Set3')
        plt.title(f'Variation of Generations by Size for {algorithm}')
        plt.xlabel('Size')
        plt.ylabel('Generations')
        plt.savefig(f'images/{algorithm}_generations_boxplot.png')
    
    ### h() a traves de una ejecución

    while True:
        _, _, _, _, h_list_hc = hill_climbing_with_tracking(8)
        print('Running HC...')
        if h_list_hc[-1] == 0:
            print('Solution found!')
            break
        print(f'Solution not found, value found: {h_list_hc[-1]}')

    while True:
        _, _, _, _, h_list_sa = simulated_annealing_with_tracking(8)
        print('Running SA...')
        if h_list_sa[-1] == 0:
            print('Solution found!')
            break
        print(f'Solution not found, value found: {h_list_sa[-1]}')

    while True:
        _, _, _, _, h_list_gen1 = genetic_with_tracking(8)
        print('Running G1...')
        if h_list_gen1[-1] == 0:
            print('Solution found!')
            break
        print(f'Solution not found, value found: {h_list_gen1[-1]}')

    while True:
        _, _, _, _, h_list_gen2 = genetic2_with_tracking(8)
        print('Running G2...')
        if h_list_gen2[-1] == 0:
            print('Solution found!')
            break
        print(f'Solution not found, value found: {h_list_gen2[-1]}')

    lists = {
    "h_list_hc": h_list_hc,
    "h_list_sa": h_list_sa,
    "h_list_gen1": h_list_gen1,
    "h_list_gen2": h_list_gen2
    }

    for name, lst in lists.items():
        plt.figure(figsize=(10,6))
        sns.lineplot(data=lst)
        plt.title(f'Variation of Heuristic Value Through Iterations: {name}')
        plt.ylabel('h()')
        plt.savefig(f'images/{name}_lineplot')
        plt.close()
    
    print('Finished! :)')


plot()
