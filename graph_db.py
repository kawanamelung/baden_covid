import csv
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from operator import itemgetter
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter, MONDAY

MOVING_AVERAGE_LENGTH = 7 


def get_last_n_days_from_reference(ref_day, dates, n):
  print(ref_day)
  return list(filter(lambda day: timedelta(days=0) <= ref_day - day < timedelta(days=n), dates))


def graph_db(db):
  
  x, y = [], []
  
  with open('db.csv','r') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      for row in plots:
          x.append(row[0])
          y.append(int(row[1]))
  x = [datetime.strptime(d,'%Y-%m-%d').date() for d in x]
  
  xys_dict = dict(zip(x,y))
  
  xys = sorted(xys_dict.items(), key=itemgetter(0))
  x, y =list(zip(*xys)) 
  
  seven_day_average_y = []
  seven_day_average_x = []
  
  for i in range(0, len(x) - MOVING_AVERAGE_LENGTH):
    last_n_days = get_last_n_days_from_reference(x[i], x, MOVING_AVERAGE_LENGTH)
    if len(last_n_days)== 0: 
      continue
    print(len(last_n_days))
  
    last_n_days_covid_cases = [xys_dict[date] for date in last_n_days]
    seven_day_average_y.append(sum(last_n_days_covid_cases) / len(last_n_days_covid_cases))
    seven_day_average_x.append(x[i])
  
  
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
  if __name__ == "__main__":
    plt.show()

if __name__ == "__main__":
  graph_db('db.csv')
