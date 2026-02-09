import numpy as np
import matplotlib.pyplot as plt

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 16
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 16
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

# x in [-4, 4]
x = np.linspace(-4, 4, 500)

# Standard normal PDF (continuous)
pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

plt.figure(figsize=(6, 3))
plt.plot(x, pdf, color='black', linewidth=2)

plt.xlabel('')      # continuous variable (italic, math style)
plt.ylabel('')       # НФ = нягтын функц (PDF)
plt.title('Хэвийн тархалт, \n 0 математик дундажтай, 1 дисперстэй')

plt.xlim(-4, 4)
plt.ylim(0, pdf.max() * 1.05)
plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_24.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_24.png',bbox_inches="tight", pad_inches=0.05, format="png", dpi=300)  

