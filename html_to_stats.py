import sys
import os

README = """
Two or more command line args are required: 
1. The html file of the covid table.
2. The list of cities to process.
"""

def html_to_stats(html_file, *cities):
  strings_to_match = list(map(lambda city: ">SK {}</span></div>".format(city), cities))

  with open(html_file, 'r') as f:
    lines = f.readlines()
  possibleMatches = filter(lambda line: any(map(lambda x: x in line, strings_to_match)), lines)
  if len(possibleMatches != 1):
    print("ERROR ")
    print(possibleMatches)

if __name__ == "__main__":
  if (len(sys.argv) < 3):
    print (README)
  else: 
    html_to_stats(sys.argv[1], sys.argv[2:])

