import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (5.0, 4.0)
# plt.rcParams['figure.dpi'] = 120
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

# # Code from Figure 13-14 on page 272
def simulation(fixed, variable):
    infected = [fixed['initial_infections']]
    new_infections = [fixed['initial_infections']]
    total_infections = fixed['initial_infections']
    
    for t in range(fixed['duration']):
        cur_infections = infected[-1]
        # remove people who are no longer contagious
        if len(new_infections) > fixed['days_spreading']:
            cur_infections -= new_infections[-fixed['days_spreading']-1]
        # if social distancing, change number of daily contacts
        if t >= variable['red_start'] and t < variable['red_end']:
            daily_contacts = variable['red_daily_contacts']
        else:
            daily_contacts = fixed['init_contacts']
        # compute number of new cases
        total_contacts = cur_infections * daily_contacts
        susceptible = fixed['pop'] - total_infections
        risky_contacts = total_contacts * (susceptible/fixed['pop'])
        newly_infected = round(risky_contacts*fixed['contagiousness'])
        # update variables
        new_infections.append(newly_infected)
        total_infections += newly_infected
        infected.append(cur_infections + newly_infected)

    return infected, total_infections

# # Code from Figure 13-15 on page 273
def plot_infections(infections, total_infections, fixed):
    infection_plot = plt.plot(infections, 'k', label = 'Infected')[0]
    plt.xticks(fontsize = 'large')
    plt.yticks(fontsize = 'large')
    plt.xlabel('Халдвар илэрснээс хойших хугацаа (хоногоор)')
    plt.ylabel('Идэвхтэй халдвар тээгчийн тоо (x10^6)')

    plt.title(
    'Вакцингүй тохиолдолын халдварын тоо\n'
    f'Хүн амын тоо = {fixed["pop"]:,}, '
    f'Өдөрт харилцах хүний тоо = {fixed["init_contacts"]}, \n'
    f'Халдварлах чадвар = {(100*fixed["contagiousness"]):.1f}%, '
    f'Халдвар тараах хугацаа (хоногоор) = {fixed["days_spreading"]}'
    )

    # plt.xlabel('Days Since First Infection',fontsize = 'xx-large')
    # plt.ylabel('Ивэхтэй халдвар тээгчийн тоо',fontsize = 'xx-large')
    # plt.title('Number of Infections Assuming No Vaccine\n' +
    #           f'Pop = {fixed["pop"]:,}, ' +
    #           f'Contacts/Day = {fixed["init_contacts"]}, ' +
    #           f'Infectivity = {(100*fixed["contagiousness"]):.1f}%, ' +
    #           f'Days Contagious = {fixed["days_spreading"]}',
    #           fontsize = 'xx-large')
    plt.legend(['Халдвар тээгч'], fontsize = 16)
    # plt.legend('Халдвар тээгч',fontsize = 'xx-large')
    
    txt_box = plt.text(plt.xlim()[1]/3.5, plt.ylim()[1]/1.25,
              f'Халдвар авсан хүний нийт тоо =  {total_infections:,.0f}',
              fontdict = {'size':'xx-large', 'weight':'bold',
                          'color':'black'})
    
    # plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_17.pdf', bbox_inches="tight", pad_inches=0.1, format="pdf")
    # plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_17.png',bbox_inches="tight", pad_inches=0.1, format="png")  

    return infection_plot, txt_box

# Code from Figure 13-16 on page 274
fixed = {
    'pop': 5000000, # population at risk
    'duration': 500, # number of days for simulation
    'initial_infections': 4, # initial number of cases
    'init_contacts': 50, #contacts without social distancing
    'contagiousness': 0.005, # prob. of getting disease if exposed
    'days_spreading': 10} # days contagious after infection

variable = {
    # 'red_daily_contacts': 4, # social distancing
    'red_daily_contacts': fixed['init_contacts'], # social distancing
    'red_start': 20, # start of social distancing
    'red_end': 200} # end of social distancing

infections, total_infections = simulation(fixed, variable)
fig = plt.figure(figsize=(12, 8.5))
plot_infections(infections, total_infections, fixed)
# plt.show()

# To use interactive plots, you might might need change your
# Python preferences. Go to preferences->iPythonConsole->graphics.
# Set backend to automatic, and then restart the iPython console

# Cdpe from page 275
# Layout for figure
fig = plt.figure(figsize=(12, 8.5))
infections_ax = plt.axes([0.12, 0.2, 0.8, 0.65])
contacts_ax = plt.axes([0.25, 0.09, 0.65, 0.03])
start_ax = plt.axes([0.25, 0.06, 0.65, 0.03])
end_ax = plt.axes([0.25, 0.03, 0.65, 0.03])

# Code from page 276
# Create the sliders
from matplotlib.widgets import Slider

# contacts_slider = Slider(
#                       contacts_ax,  # axes object containing the slider
#                       'reduced\n contacts/day',  # name of slider
#                       0,   # minimal value of the parameter
#                       50,  # maximal value of the parameter
#                       50)  # initial value of the parameter)
contacts_slider = Slider(contacts_ax, 'Өдөрт харилцах хүний тоо', 0, 50)
contacts_slider.set_val(25)
contacts_slider.label.set_fontsize(12)

start_day_slider = Slider(start_ax, 'Хөл хорио эхлэх өдөр', 1, 30)
start_day_slider.set_val(20)
start_day_slider.label.set_fontsize(12)

end_day_slider = Slider(end_ax, 'Хөл хорио дуусах өдөр', 30, 400)
end_day_slider.set_val(300)
end_day_slider.label.set_fontsize(12)

# Define a function that will be executed each time the value
# indicated by any slider changes.
def update(fixed, infection_plot, txt_box,
            contacts_slider, start_day_slider, end_day_slider):
    variable = {'red_daily_contacts': contacts_slider.val,
                'red_start': start_day_slider.val,
                'red_end': end_day_slider.val}
    I, total_infections = simulation(fixed, variable)
    infection_plot.set_ydata(I)   # new y-coordinates for plot
    txt_box.set_text(f'Халдвар авсан хүний нийт тоо =  {total_infections:,.0f}')

# Cdoe from page 277
slider_update = lambda _: update(fixed, infection_plot, txt_box,
                                  contacts_slider, start_day_slider,
                                  end_day_slider)
contacts_slider.on_changed(slider_update)
start_day_slider.on_changed(slider_update)
end_day_slider.on_changed(slider_update)

infections, total_infections = simulation(fixed, variable)
plt.axes(infections_ax)
infection_plot, txt_box = plot_infections(infections,
                                          total_infections, fixed)

# plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_19.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
# plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 13\figure13_19.png',bbox_inches="tight", pad_inches=0.05, format="png")  


plt.show()
