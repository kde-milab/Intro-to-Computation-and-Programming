import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator



# plt.rcParams['figure.dpi'] = 120
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.figsize'] = (8.0, 6.0)
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
plt.rcParams['legend.fontsize'] = 18

plt.rcParams['lines.color'] = 'black'

# # The function find_payment is from Figure 10-10
def find_payment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

# # Figure 13-7 from page 264    
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        self._loan = loan
        self._rate = annRate/12.0
        self._months = months
        self._paid = [0.0] 
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = None #description of mortgage
        
    def make_payment(self):
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)
        
    def get_total_paid(self):
        return sum(self._paid)
    def __str__(self):
        return self._legend

    def plot_payments(self, style):
        plt.plot(self._paid[1:], style, label = self._legend)
    
    def plot_balance(self, style):
        plt.plot(self._outstanding, style, label = self._legend)

    def plot_tot_pd(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label = self._legend)

    def plot_net(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        equity_acquired = np.array([self._loan]*len(self._outstanding))
        equity_acquired = equity_acquired-np.array(self._outstanding)
        net = np.array(tot_pd) - equity_acquired
        plt.plot(net, style, label = self._legend)

# Code from Figure 13-8 on page 267
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self._legend = f'Тогтмол {r*100:.1f}% хүүтэй'
        
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f'Тогтмол {r*100:.1f}% хүүтэй, {pts} оноотой'

class Two_rate(Mortgage):
    def __init__(self, loan, r, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self._teaser_months = teaser_months
        self._teaser_rate = teaser_rate
        self._nextRate = r/12
        self._legend = (f'{100*r:.1f}% хүүтэй, эхний {self._teaser_months} сар {100*teaser_rate:.1f}%')
        
    def make_payment(self):
        if len(self._paid) == self._teaser_months + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1],
                                self._rate,
                                self._months - self._teaser_months)
        Mortgage.make_payment(self)

# Code from Figure 13-9 on page 268
def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                      var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    plot_mortgages(morts, amt)
    # plt.show()

# Code from Figure 13-10 on page 269    
def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc = 'best')
    styles = ['k-', 'k-.', 'k:']
    #Give names to figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(len(morts)):
        # plt.minorticks_off()
        
        plt.figure(payments)
        morts[i].plot_payments(styles[i])
        label_plot(payments, f'${amt:,} моргэйжийн зээлийн сар тутмын төлөлт', 'Сар', 'нэг сарын төлөлт')
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_11.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_11.png',bbox_inches="tight", pad_inches=0.1, format="png")  
        
        plt.figure(cost)
        morts[i].plot_tot_pd(styles[i])
        label_plot(cost, f'${amt:,} моргэйжийн зээлийн мөнгөн зардал', 'Сар', 'Нийт төлбөр')
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_12.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_12.png', bbox_inches="tight", pad_inches=0.1, format="png")  

        plt.figure(balance)
        morts[i].plot_balance(styles[i])
        label_plot(balance, f'${amt:,} моргэйжийн зээлийн үлдэгдэл баланс', 'Сар', 'Зээлийн үлдэгдэл баланс')
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_13zuun.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_13zuun.png', bbox_inches="tight", pad_inches=0.1, format="png")  

        plt.figure(net_cost)
        morts[i].plot_net(styles[i])
        label_plot(net_cost, f'${amt:,} моргэйжийн цэвэр зардал', 'Сар', 'Төлбөр – өмч $')
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_13baruun.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
        plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_13baruun.png', bbox_inches="tight", pad_inches=0.1, format="png")  

    # label_plot(cost, f'${amt:,} моргэйжийн зээлийн мөнгөн зардал', 'Сар', 'Нийт төлбөр')
    

# # Code from page 268
compare_mortgages(amt=200000, years=30, fixed_rate=0.07,
                  pts = 3.25, pts_rate=0.05, var_rate1=0.045,
                  var_rate2=0.095, var_months=48)
