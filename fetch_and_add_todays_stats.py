import os
from datetime import datetime
import os
import pdf_to_html
import html_to_stats

BASE_DIR = 'pdf_files'

os.system("mkdir out pdf_files")

def add_new_stats_to_db(date, stats, db_file_name):
  with open(db_file_name, 'a+') as f:
    f.write("{},{}\n".format(date, ",".join(stats)))

def fetch_and_add_todays_stats(db):
  currentDay = datetime.now().day
  currentMonth = datetime.now().month
  currentYear = datetime.now().year
  
  command = "curl https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/{:02d}{:02d}{:02d}_COVID_Tagesbericht_LGA.pdf -o pdf_files/{:02d}-{:02d}-{}.pdf --fail".format(currentYear - 2000, currentMonth, currentDay, currentDay, currentMonth, currentYear)

  print(command)
  os.system(command)

  file = "{:02d}-{:02d}-{}.pdf".format(currentDay, currentMonth, currentYear)
  
  os.system('rm -rf out')
  pdf_to_html.convert_pdf_to_html(BASE_DIR + '/' + file, 'out')
  date, cases = html_to_stats.html_to_stats('out' + '/' + 'page2.html', 'Freiburg')
  file_date = file.split(".")[0]
    
  add_new_stats_to_db(datetime.now().date(), [cases], db)

if __name__ == "__main__":
  fetch_and_add_todays_stats('db.csv') 
