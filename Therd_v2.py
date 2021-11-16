import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

colours = {}
for i in range(11):
    colours[i] = ((10 - i) / 10, i / 10, 0)

data = pd.read_csv("Third/students.csv", sep=';', names=['prep', 'group', 'mark'])

fig = plt.figure(tight_layout=True, figsize=(14, 7))
gs = gridspec.GridSpec(2, max(len(data['prep'].unique()), len(data['group'].unique())))


def do_stuff(all_data, key, line):
    count = 0
    for prep in all_data[key].unique():
        marks = all_data[all_data[key] == prep] \
            .sort_values('mark')['mark'] \
            .value_counts().sort_index()
        indexes = marks.index.tolist()

        ax = fig.add_subplot(gs[line, count])
        ax.pie(marks, labels=indexes,
               autopct=lambda pct: int(pct / 100. * sum(marks)),
               textprops={'size': 'smaller'},
               colors=[colours[key] for key in indexes])
        ax.set_title(prep)
        count += 1


do_stuff(data, 'prep', 0)
do_stuff(data, 'group', 1)
plt.show()
