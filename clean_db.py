import csv
from datetime import timedelta, datetime
from operator import itemgetter

x, y = [], []

with open('db.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
x = [datetime.strptime(d,'%d.%m.%Y').date() for d in x]

xys_dict = dict(zip(x,y))

xys = sorted(xys_dict.items(), key=itemgetter(0))
x, y =list(zip(*xys)) 

with open('db.csv', 'w') as f:
  for x_val, y_val in zip(x,y):
    f.write('{},{}\n'.format(x_val, y_val))
