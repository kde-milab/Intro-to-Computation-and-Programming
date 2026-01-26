import matplotlib.pyplot as plt
import numpy as np
import random

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
plt.rcParams['legend.fontsize'] = 18

plt.rcParams['lines.color'] = 'black'

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
    
# # Figure 16-6 from page 331
class Cold_drunk(Drunk):
    def take_step(self):
        stepChoices = [(0.0,1.0), (0.0,-2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EW_drunk(Drunk):
    def take_step(self):
        stepChoices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices) 

def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)

# # Code from page 332
random.seed(0)       
sim_all((Usual_drunk, Cold_drunk, EW_drunk), (100, 1000), 10)

# # Figure 16-7 from page 333
class style_iterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

# # Figure 16-8 from page 333
def sim_drunk(num_trials, d_class, walk_lengths):
    meanDistances = []
    for num_steps in walk_lengths:
        print('Starting simulation of', num_steps, 'steps')
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    style_choice = style_iterator(('m-', 'r:', 'k-.'))
    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print('Starting simulation of', d_class.__name__)
        means = sim_drunk(num_trials, d_class, walk_lengths)
        plt.plot(walk_lengths, means, cur_style,
                   label = d_class.__name__)
    plt.title(f'Mean Distance from Origin ({num_trials} trials')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc = 'best')
    plt.semilogx()
    plt.semilogy()

# # Code from page 334    
# sim_all_plot((Usual_drunk, Cold_drunk, EW_drunk),
#               (10, 100, 1000, 10000, 100000), 100)
