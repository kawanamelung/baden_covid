import os
import pdf_to_html
import html_to_stats

BASE_DIR = 'pdf_files'

def add_new_stats_to_db(date, stats, db_file_name):
  with open(db_file_name, 'a+') as f:
    f.write("{},{}\n".format(date, ",".join(stats)))

if __name__ == "__main__":
  for file in os.listdir(BASE_DIR):
    print(file)
    os.system('rm -rf out')
    pdf_to_html.convert_pdf_to_html(BASE_DIR + '/' + file, 'out')
    date, cases = html_to_stats.html_to_stats('out' + '/' + 'page2.html', 'Freiburg')
    file_date = file.split(".")[0].replace("-",".")
    
    add_new_stats_to_db(file_date, [cases], 'db.csv')
