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

# === x тэнхлэгүүд ===
x1 = np.linspace(0, 1, 200)
x2 = np.linspace(0, 2, 400)

# === PDF-үүд ===
pdf_random = np.ones(len(x1))              # Uniform(0,1)
pdf_sum = np.where(
    x2 <= 1,
    x2,                                     # өсөх хэсэг
    2 - x2                                 # буурах хэсэг
)

# === Зурах ===
fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.6))

# --- PDF for random.random() ---
axes[0].plot(x1, pdf_random, color='black', linewidth=2)
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0.94, 1.06)
axes[0].set_title('random.random() \n нягтын функц')
axes[0].set_xlabel('x', fontstyle = 'italic')
axes[0].set_ylabel('Нягтийн функц')   # PDF → НФ (нягтын функц)
# plt.tight_layout()
# plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_22zuun.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
# plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_22zuun.png',bbox_inches="tight", pad_inches=0.05, format="png", dpi=300)  


# --- PDF for random.random() + random.random() ---
axes[1].plot(x2, pdf_sum, color='black', linewidth=2)
axes[1].set_xlim(0, 2)
axes[1].set_ylim(0, 1.05)
axes[1].set_title('random.random()+random.random() \n нягтын функц')
axes[1].set_xlabel('x', fontstyle='italic')
axes[1].set_ylabel('Нягтийн функц')

plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_22.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_22.png',bbox_inches="tight", pad_inches=0.05, format="png", dpi=300)  
# plt.show()
# plt.show()
