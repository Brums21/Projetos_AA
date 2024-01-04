import matplotlib.pyplot as plt

def plot_comparison():
    
    lines_aprox = None
    lines_sc = None
    
    with open("./results/time_aproximate.txt", "r") as file:
        lines_aprox = file.readlines()
    
    with open("./results/time_space_saving.txt", "r") as file:
        lines_sc = file.readlines()    
    
    languages = ["English", "Spanish", "French"]
    
    aprox = []
    k3_sc = []
    k5_sc = []
    k11_sc = []
    
    for i in range(0, len(lines_sc), 7):
        k3_sc.append(float(lines_sc[i+2]))
        k5_sc.append(float(lines_sc[i+4]))
        k11_sc.append(float(lines_sc[i+6]))

    for i in range(len(lines_aprox)):
        aprox.append(float(lines_aprox[i][4:]))

    plt.figure(figsize=(10,6))

    plt.plot(languages, aprox, marker='o', color=(0.922, 0.651, 0.216, 1), label='Approximate Counter')
    plt.plot(languages, k3_sc, marker='o', color=(0.678, 0.176, 0.153, 1), label='Space Saving - k=3')
    plt.plot(languages, k5_sc, marker='o', color=(0.404, 0.722, 0.431, 1), label='Space Saving - k=5')
    plt.plot(languages, k11_sc, marker='o', color=(0.169, 0.631, 0.831, 1), label='Space Saving - k=11')

    plt.xlabel('Languages')
    plt.ylabel('Computational time (secs)')
    plt.title('Computational effort for approximate count and space-saving algorithms')
    plt.legend()
    

    plt.savefig("./images/comp_effor_approx_space_saving.png")
    plt.close()
    
def plot_comparison_all():
    lines_exact = None
    lines_aprox = None
    lines_sc = None
    
    with open("./results/time_exact.txt", "r") as file:
        lines_exact = file.readlines()
    
    with open("./results/time_aproximate.txt", "r") as file:
        lines_aprox = file.readlines()
    
    with open("./results/time_space_saving.txt", "r") as file:
        lines_sc = file.readlines()    
    
    languages = ["English", "Spanish", "French"]
    
    exact = []
    aprox = []
    sc = []
    
    for i in range(0, len(lines_sc), 7):
        sc.append(float(lines_sc[i+6]))

    for i in range(len(lines_aprox)):
        exact.append(float(lines_exact[i][4:]))
        aprox.append(float(lines_aprox[i][4:]))

    plt.figure(figsize=(10,6))

    plt.plot(languages, exact, marker='o', color=(0.922, 0.651, 0.216, 1), label='Exact Counter')
    plt.plot(languages, aprox, marker='o', color=(0.678, 0.176, 0.153, 1), label='Approximate Counter')
    plt.plot(languages, sc, marker='o', color=(0.404, 0.722, 0.431, 1), label='Space-Saving - k=11')
    
    plt.xlabel('Languages')
    plt.ylabel('Computational time (secs)')
    plt.title('Computational effort for exact count, approximate count and space-saving algorithms')
    plt.legend()

    plt.savefig("./images/comp_effor_all.png")
    plt.close()

    
if "__main__"==__name__:
    plot_comparison()
    plot_comparison_all()