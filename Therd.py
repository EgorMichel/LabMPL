import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.gridspec as gridspec

with open("Third/students.csv") as file:
    lines_from_file = file.readlines()

lines = []
for line in lines_from_file:
    lines.append(line[:-1].split(';'))

data = pd.DataFrame(lines)
print(data)


def func(pct, allvals):
    absolute = int(pct/100. * sum(allvals))
    return absolute


class Prep:
    def __init__(self, name):
        self.marks = [0] * 11
        self.name = name
        self.labels = [str(i) for i in range(11)]
        self.colors = [((10 - i) / 10, i / 10, 0) for i in range(11)]

    def add_mark(self, mark):
        self.marks[mark] += 1

    def prepare_mark(self):
        deleted = 0
        for i in range(11):
            if self.marks[i - deleted] == 0:
                self.marks.pop(i - deleted)
                self.labels.pop(i - deleted)
                self.colors.pop(i - deleted)
                deleted += 1


preps = [Prep(i) for i in sorted(list(set(data.loc[:, 0])))]
groups = [Prep(i) for i in sorted(list(set(data.loc[:, 1])))]

for i in range(len(preps)):
    for j in range(len(data.loc[:, 1])):
        if data.loc[j, 0] == preps[i].name:
            preps[i].add_mark(int(data.loc[j, 2]))

for i in range(len(groups)):
    for j in range(len(data.loc[:, 1])):
        if data.loc[j, 1] == groups[i].name:
            groups[i].add_mark(int(data.loc[j, 2]))

fig = plt.figure(tight_layout=True, figsize=(14, 7))
gs = gridspec.GridSpec(2, max(len(preps), len(groups)))
count = 0
for prep in preps:
    ax = fig.add_subplot(gs[0, count])
    prep.prepare_mark()
    ax.pie(prep.marks, labels=prep.labels, colors=prep.colors,
           autopct=lambda pct: func(pct, prep.marks), textprops={'size': 'smaller'})
    ax.set_title(prep.name)
    count += 1

count = 0
for group in groups:
    ax = fig.add_subplot(gs[1, count])
    group.prepare_mark()
    ax.pie(group.marks, labels=group.labels, colors=group.colors)
    ax.set_title(group.name)
    count += 1


plt.text(-8, 8, "Results per prep", fontsize=18, wrap=True)
plt.text(-8, 2.6, "Results per group", fontsize=18, wrap=True)
plt.show()
