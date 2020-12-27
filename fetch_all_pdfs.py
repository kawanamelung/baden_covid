import os

for month in range(12, 13):
  for day in range(1, 32):
    os.system("curl https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/20{:02d}{:02d}_COVID_Tagesbericht_LGA.pdf -o pdf_files/{:02d}-{:02d}-2020.pdf --fail".format(month, day, day, month))

