import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = (4.0, 3.0)
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





# plotting the left side of figure 13.4
plt.figure(1)
principal = 10000			 
interest_rate = 0.05		  
years = 20				  
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interest_rate
plt.plot(values, 'k')
# axs[0].plot(values)
plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_4zuun.pdf', bbox_inches="tight",
    pad_inches=0.5, format="pdf")    
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_4zuun.png', bbox_inches="tight",
    pad_inches=0.5, format="png")

# plotting the right side of figure 13.4
plt.figure(2)
principal = 10000			 
interest_rate = 0.05		  
years = 20				  
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interest_rate

plt.plot(values,'k')
plt.title('Нийлмэл өсөлт (жилийн 5% хүү)')
plt.xlabel('Хуримтлагдах хугацаа (жилээр)')
plt.ylabel('Үндсэн хадгаламжийн хэмжээ ($)')
plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_4baruun.pdf', bbox_inches="tight",
    pad_inches=0.05, format="pdf")    
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_4baruun.png',bbox_inches="tight",
    pad_inches=0.05, format="png")
# plt.show()

# plotting figure 13.5
plt.figure(3)
principal = 10000			 
interest_rate = 0.05		  
years = 20				  
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interest_rate

plt.plot(values,'ko')
plt.title('Нийлмэл өсөлт (жилийн 5% хүү)')
plt.xlabel('Хуримтлагдах хугацаа (жилээр)')
plt.ylabel('Үндсэн хадгаламжийн хэмжээ ($)')
plt.tight_layout()
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_5.pdf', bbox_inches="tight",
    pad_inches=0.05, format="pdf")    
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_5.png', bbox_inches="tight",
    pad_inches=0.05, format="png")

# plt.show()


# from PIL import Image

# img = Image.open(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_4baruun.png')
# print(img.size)   # (өргөн, өндөр) пикселээр
# print(img.info)


