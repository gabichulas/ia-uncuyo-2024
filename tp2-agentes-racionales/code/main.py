from environment import *
import reflexive_agent
import random_agent
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def evaluate_performance(agent_class, env_class, sizes, dirt_rates, repetitions):
    results = []
    for size in sizes:
        for dirt_rate in dirt_rates:
            for _ in range(repetitions):
                env = env_class(size, size, dirt_rate, 12) # dale boca
                agent = agent_class(env)
                while not agent.die():
                    agent.think()
                performance = env.get_performance()
                results.append({
                    'Size': f'{size}x{size}',
                    'Dirt Rate': dirt_rate,
                    'Performance': performance,
                    'Time': 1000-agent.lives
                })
    return pd.DataFrame(results)

sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repetitions = 10

ref_results = evaluate_performance(reflexive_agent.RefAgent, Environment, sizes, dirt_rates, repetitions)
rand_results = evaluate_performance(random_agent.RandAgent, Environment, sizes, dirt_rates, repetitions)

ref_results.to_csv('tp2-agentes-racionales/ref_agent_results.csv', index=False)
rand_results.to_csv('tp2-agentes-racionales/rand_agent_results.csv', index=False)

def plot_results(df, agent_name):
    df_grouped = df.groupby(['Size', 'Dirt Rate']).mean().reset_index()
    sizes = ["2x2", "4x4", "8x8", "16x16", "32x32", "64x64", "128x128"]
    colors = matplotlib.colormaps.get_cmap('tab10') 

    # Gráfico de barra
    for size in sizes:
        size_data = df_grouped[df_grouped['Size'] == size]
        _, ax = plt.subplots(figsize=(12, 8))
        ax.bar(size_data['Dirt Rate'].astype(str), size_data['Performance'], color=[colors(i) for i in range(len(size_data))], width=0.3)
        ax.set_title(f'{agent_name} Performance for Size {size}')
        ax.set_xlabel('Dirt Rate')
        ax.set_ylabel('Performance')
        ax.set_ylim(0,1)
        plt.savefig(f'tp2-agentes-racionales/images/{agent_name}_barplot_size_{size}.png')
        plt.close()
        

    # Gráfico de caja
    sizes = ["2x2", "4x4", "8x8", "16x16", "32x32", "64x64", "128x128"]

    # Gráfico de caja
    for dirt_rate in df['Dirt Rate'].unique():
        plt.figure(figsize=(10, 6))
        df_filtered = df[(df['Dirt Rate'] == dirt_rate) & (df['Size'].isin(sizes))].copy()
        if not df_filtered.empty:
            # Convertir la columna 'Size' a tipo categórico con un orden específico
            df_filtered['Size'] = pd.Categorical(df_filtered['Size'], categories=sizes, ordered=True)
            df_filtered.boxplot(by='Size', column='Performance', grid=False)
            plt.title(f'Boxplot of {agent_name} Performance for Dirt Rate {dirt_rate}')
            plt.suptitle('')
            plt.xlabel('Size')
            plt.ylabel('Performance')
            plt.xticks(rotation=45)
            plt.savefig(f'tp2-agentes-racionales/images/{agent_name}_boxplot_dirt_rate_{dirt_rate}.png')
        plt.close()

# Generar gráficos para ref_results
plot_results(ref_results, 'RefAgent')

# Generar gráficos para rand_results
plot_results(rand_results, 'RandAgent')

