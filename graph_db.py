import csv
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from operator import itemgetter, attrgetter
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter, MONDAY

MOVING_AVERAGE_LENGTH = 7 


x, y = [], []

with open('db.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(int(row[1]))
x = [dt.datetime.strptime(d,'%d.%m.%Y').date() for d in x]

xys = sorted(list(zip(x, y)), key=itemgetter(0))
x, y =list(zip(*xys)) 

seven_day_average_y = [sum(y[i:i+MOVING_AVERAGE_LENGTH]) / MOVING_AVERAGE_LENGTH for i in range(0, len(y) - MOVING_AVERAGE_LENGTH)]
seven_day_average_x = x[MOVING_AVERAGE_LENGTH:]

months = MonthLocator(range(1, 13), bymonthday=1, interval=1)
monthsFmt = DateFormatter("%b '%y")
mondays = WeekdayLocator(MONDAY)



fig, ax = plt.subplots()
ax.set_title("Freiburg im Breisgau\nCovid cases per day (7-day moving average)")
ax.set_xlabel("Date")
ax.set_ylabel("Cases per day")

ax.plot_date(seven_day_average_x, seven_day_average_y, '-')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
ax.grid(True)

plt.savefig('books_read.png')
plt.show()
