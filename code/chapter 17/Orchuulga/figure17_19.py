import matplotlib.pyplot as plt

code = """random.seed(0)
vals = []
for i in range(1000):
    num1 = random.choice(range(0, 101))
    num2 = random.choice(range(0, 101))
    vals.append(num1 + num2)
plt.hist(vals, bins = 10, 
    facecolor='lightgray', ec = 'k')
plt.xlabel('Нийлбэр')
plt.ylabel('Тохиолын тоо')
"""

fig, ax = plt.subplots(figsize=(3.5, 2.5))
ax.text(
    0.01, 0.99,
    code,
    fontfamily='monospace',
    fontsize=10,
    va='top'
)

ax.axis('off')
# plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_19zuun.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 17\Orchuulga\figure17_19zuun.png',bbox_inches="tight", pad_inches=0.05, format="png", dpi=300)  
# plt.show()