import matplotlib.pyplot as plt
import numpy as np

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 18
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 18
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
#set number of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
#Set size of type in legend
plt.rcParams['legend.fontsize'] = 14

states = [
    'Хойд нутаг',
    'ACT',
    'Баруун Австрали',
    'Шинэ Өмнөд Уэльс',
    'Австрали (нийт)',
    'Квинсланд',
    'Викториа',
    'Өмнөд Австрали',
    'Тасмани'
]

mean_income = [
    1450, 1900, 1440, 1330, 1330, 1280, 1280, 1150, 950
]

std_dev = [
    720, 680, 680, 640, 620, 560, 500, 450, 400
]


def plot_income_figure():
    y_pos = np.arange(len(states))

    fig, ax = plt.subplots(figsize=(8, 4.5))

    # === Mean income (саарал, урт bar) ===
    ax.barh(
        y_pos,
        mean_income,
        color='lightgray',
        edgecolor='black',
        height=0.6,
        label='Дундаж орлого'
    )

    # === Standard deviation (хар, богино bar) ===
    ax.barh(
        y_pos,
        std_dev,
        color='black',
        height=0.35,
        label='Стандарт хазайлт'
    )

    # === Тэнхлэг, шошго ===
    ax.set_yticks(y_pos)
    ax.set_yticklabels(states)
    ax.invert_yaxis()  # дээдээс доош англи зурагтай адил

    ax.set_xlabel('Орлого    ')

    ax.set_xlim(0, 2000)
    ax.set_xticks([0, 500, 1000, 1500, 2000])
    ax.set_xticklabels(['£0', '£500', '£1,000', '£1,500', '£2,000'])

    # === Grid (зөвхөн x тэнхлэг) ===
    ax.xaxis.grid(True, linestyle='-', linewidth=0.8)
    ax.yaxis.grid(False)

    # === Legend ===
    ax.legend(loc='lower right', frameon=True)

    fig.text(
    0.99, 0.00001,
    'censusstats.blogspot.com',
    ha='right',
    va='bottom',
    fontsize=14,
    color='gray'
    )

    # plt.tight_layout()
    # plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_18.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
    # plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_18.png',bbox_inches="tight", pad_inches=0.1, format="png", dpi=300)  
    # plt.show()


plot_income_figure()
