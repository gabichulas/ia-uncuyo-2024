from environment import *
import reflexive_agent
import random_agent
import pandas as pd
import matplotlib.pyplot as plt

def evaluate_performance(agent_class, env_class, sizes, dirt_rates, repetitions):
    results = []
    for size in sizes:
        for dirt_rate in dirt_rates:
            for _ in range(repetitions):
                env = env_class(size, size, dirt_rate)
                agent = agent_class(env)
                while not agent.die():
                    agent.think()
                performance = env.get_performance()
                results.append({
                    'Size': f'{size}x{size}',
                    'Dirt Rate': dirt_rate,
                    'Performance': performance
                })
    return pd.DataFrame(results)

sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repetitions = 10

ref_results = evaluate_performance(reflexive_agent.RefAgent, Environment, sizes, dirt_rates, repetitions)
rand_results = evaluate_performance(random_agent.RandAgent, Environment, sizes, dirt_rates, repetitions)


ref_results.to_csv('tp2-agentes-racionales/ref_agent_results.csv', index=False)
rand_results.to_csv('tp2-agentes-racionales/rand_agent_results.csv', index=False)


print("Resultados del Agente Reflexivo:")
print(ref_results)

print("\nResultados del Agente Aleatorio:")
print(rand_results)

def plot_results(df, agent_name):
    df_grouped = df.groupby(['Size', 'Dirt Rate']).mean().reset_index()
    sizes = df_grouped['Size'].unique()
    colors = plt.cm.get_cmap('tab10', len(df_grouped['Dirt Rate'].unique())) 
    for size in sizes:
        size_data = df_grouped[df_grouped['Size'] == size]
        _, ax = plt.subplots(figsize=(12, 8))
        ax.bar(size_data['Dirt Rate'].astype(str), size_data['Performance'], color=[colors(i) for i in range(len(size_data))], width=0.3)
        ax.set_ylim(0, 1) 
        ax.set_title(f'{agent_name} - Tamaño del Entorno: {size}')
        ax.set_xlabel('Tasa de Suciedad')
        ax.set_ylabel('Desempeño Promedio')
        for i, v in enumerate(size_data['Performance']):
            ax.text(i, v + 0.01, f'{v:.2f}', ha='center', va='bottom')
        plt.savefig(f'tp2-agentes-racionales/images/{agent_name}_{size}.png')
        plt.close()

plot_results(ref_results, 'Desempeño del Agente Reflexivo')
plot_results(rand_results, 'Desempeño del Agente Aleatorio')