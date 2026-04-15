import matplotlib
matplotlib.use('Agg')  # importante en Linux sin GUI

import matplotlib.pyplot as plt

def generate_chart(df):
    x = df.columns[0]
    y = df.columns[1]

    plt.figure()
    df.plot(kind='bar', x=x, y=y)
    plt.title("Resultados")
    plt.tight_layout()

    file_path = "output_chart.png"
    plt.savefig(file_path)
    plt.close()

    return file_path