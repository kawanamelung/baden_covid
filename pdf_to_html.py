import sys
import os

README = """
Exactly two command line args are required: 
1. The PDF file
2. The output file
"""

def convert_pdf_to_html(pdf_file, output_dir):
  os.system('./bin/pdftohtml ' + pdf_file + ' ' +  output_dir)

if __name__ == "__main__":
  if (len(sys.argv) != 3):
    print (README)
  else: 
    convert_pdf_to_html(sys.argv[1], sys.argv[2])

