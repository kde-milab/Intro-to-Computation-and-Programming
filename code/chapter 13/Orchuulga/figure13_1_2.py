import matplotlib.pyplot as plt
import os
print("Hello")
# plt.plot([1,2,3,4], [1,7,3,5]) #draw on current figure
# plt.show()

plt.figure(1)                		# 1-р зургийг үүсгэнэ
plt.plot([1,2,3,4], [1,2,3,4])  	# 1-р зураг дээр дүрсэлнэ
plt.figure(2)                 		# 2-р зургийг үүсгэнэ
plt.plot([1,4,2,3], [5,6,7,8])  	# 2-р зураг дээр дүрсэлнэ
plt.savefig('Figure-Addie')      	# 2-р зургийг файлд хадгална
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_2zuun.pdf', format="pdf")       	# 1-р зургийг файлд хадгална
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_2zuun.png', format="png")
plt.figure(1)                 		# 1-р зураг руу буцна
plt.plot([5,6,10,3])            	# 1-р зураг дээр дахин дүрсэлнэ
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_2baruun.pdf', format="pdf")       	# 1-р зургийг файлд хадгална
plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_2baruun.png', format="png")  

plt.show()

