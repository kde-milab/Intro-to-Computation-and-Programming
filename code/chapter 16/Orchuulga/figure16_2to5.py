
import matplotlib.pyplot as plt
import numpy as np
import random
import math

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 20
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

# # Figure 16-2 from page 326
class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self._x, self._y = x, y
    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other._x, other._y
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'

class Field(object):
    def __init__(self):
        self._drunks = {}
        
    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError('Duplicate drunk')
        else:
            self._drunks[drunk] = loc
            
    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        #use move method of Location to get new location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)
        
    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        return self._drunks[drunk]

# # Figure 16-3 from page 327        
class Drunk(object):
    def __init__(self, name = None):
        """Assumes name is a str"""
        self._name = name

    def __str__(self):
        if self != None:
            return self._name
        return 'Anonymous'

class Usual_drunk(Drunk):
    def take_step(self):
        step_choices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(step_choices)
        return random.choice(step_choices)

# # Figure 16-4 from page 328  
def walk(f, d, num_steps):
    """Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
       Moves d num_steps times; returns the distance between the
       final location and the location at the start of the  walk."""
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))

def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
         d_class a subclass of Drunk
       Simulates num_trials walks of num_steps steps each.
       Returns a list of the final distances for each trial"""
    Homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_trials), 1))
    return distances

def drunk_test(walk_lengths, num_trials, d_class):
    """Assumes walk_lengths a sequence of ints >= 0
         num_trials an int > 0, d_class a subclass of Drunk
       For each number of steps in walk_lengths, runs sim_walks with
         num_trials walks and prints results"""
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, 'walk of', num_steps, 'steps: Mean =',
              f'{sum(distances)/len(distances):.3f}, Max =',
              f'{max(distances)}, Min = {min(distances)}')

# # Code from page 329
# random.seed(0)
# drunk_test((10, 100, 1000, 10000), 100, Usual_drunk)
# drunk_test((0,1), 100, Usual_drunk)

# sim_walks with correction described on page 329
def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
          d_class a subclass of Drunk
        Simulates num_trials walks of num_steps steps each.
        Returns a list of the final distances for each trial"""
    Homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_steps), 1))
    return distances

# random.seed(0)
# drunk_test((10, 100, 1000, 10000), 100, Usual_drunk)
# drunk_test((0,1), 100, Usual_drunk)

# Би өөрөө үүсгэсэн код


def mean_distance_from_origin(num_steps, num_trials):
    """Эхлэл цэгээсх дундаж зайг тооцоолно"""
    distances = []

    for _ in range(num_trials):
        x, y = 0, 0
        for _ in range(num_steps):
            step = random.choice(['N', 'S', 'E', 'W'])
            if step == 'N':
                y += 1
            elif step == 'S':
                y -= 1
            elif step == 'E':
                x += 1
            else:
                x -= 1
        distances.append(math.sqrt(x**2 + y**2))

    return sum(distances) / len(distances)


def generate_figure_16_5():
    num_trials = 100
    step_counts = [10**i for i in range(1, 6)]  # 10^1 ... 10^5

    mean_distances = []
    sqrt_steps = []

    for steps in step_counts:
        mean_distances.append(
            mean_distance_from_origin(steps, num_trials)
        )
        sqrt_steps.append(math.sqrt(steps))

    # === ЗУРАХ ===
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(step_counts, mean_distances,
            label='Usual_drunk алхалт',
            color='black')

    ax.plot(step_counts, sqrt_steps,
            linestyle='--',
            label='sqrt(алхамын тоо)',
            color='black'
            )

    ax.set_xscale('log')
    ax.set_yscale('log')

    ax.set_xlabel('Алхамын тоо')
    ax.set_ylabel('Эхлэл цэг хүртэлх зай')
    ax.set_title('Эхлэл цэг хүртэлх дундаж зай (100 туршилт)')

    ax.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 14\figure14_5.pdf', bbox_inches="tight", pad_inches=0.05, format="pdf")
    plt.savefig(r'C:\python\guttag\figures\Intro-to-Computation-and-Programming\code\chapter 14\figure14_5.png',bbox_inches="tight", pad_inches=0.05, format="png", dpi=300)  

    # fig.savefig(
    #     'Figure_16_5.png',
    #     dpi=300,
    #     bbox_inches='tight',
    #     pad_inches=0.05
    # )
    # plt.show()


# Зураг 16-5-г үүсгэх
generate_figure_16_5()


plt.show()
