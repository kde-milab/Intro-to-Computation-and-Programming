import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 120
plt.rcParams['savefig.dpi'] = 300
# шугамын өргөнийг тохируулах
plt.rcParams['lines.linewidth'] = 4
# гарчгийн фонтын хэмжээг тохируулах
plt.rcParams['axes.titlesize'] = 20
# тэнхлэгийн тэмдэглэгээний фонтын хэмжээ
plt.rcParams['axes.labelsize'] = 20
# x тэнхлэгийн тоонуудын хэмжээ
plt.rcParams['xtick.labelsize'] = 16
# y тэнхлэгийн тоонуудын хэмжээ
plt.rcParams['ytick.labelsize'] = 16
# x тэнхлэгийн хэрчдэсний хэмжээ
plt.rcParams['xtick.major.size'] = 7
# y тэнхлэгийн хэрчдэсний хэмжээ
plt.rcParams['ytick.major.size'] = 7
# тэмдэгийн (жишээ нь, цэгийг төлөөлөх дугуйн хэмжээ) хэмжээ
plt.rcParams['lines.markersize'] = 10
# тэмдэглэгээний (legend) цэст тухайн тэмдэгтийн тоог тохируулах
plt.rcParams['legend.numpoints'] = 1
# тэмдэглэгээний фонтын хэмжээ
plt.rcParams['legend.fontsize'] = 24

plt.rcParams['lines.color'] = 'black'

plt.figure(1)
principal = 10000 # эхний хадгаламж
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
plt.plot(values, '-k', linewidth = 30)
plt.title('Нийлмэл өсөлт (жилийн 5% хүү)', fontsize=28)
plt.xlabel('Хуримтлагдах хугацаа (жилээр)', fontsize='x-small')
plt.ylabel('Үндсэн хадгаламжийн хэмжээ ($)')
# plt.tight_layout()

# plt.title('Жилийн нийлмэл 5% өсөлт', )
# plt.xlabel('Нийлмэл жил', )
# plt.ylabel('Мөнгөн дүн ($)')

plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_6.pdf', bbox_inches="tight",
    pad_inches=0.5, format="pdf")    
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_6.png',  bbox_inches="tight",
    pad_inches=0.5, format="png")

# plt.show()
