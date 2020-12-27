import sys
import os

README = """
Two or more command line args are required: 
1. The html file of the covid table.
2. The list of cities to process.
"""

def html_to_stats(html_file, city):
  with open(html_file, 'r') as f:
    lines = f.readlines()
  possibleMatches = list(filter(lambda line: city in "".join(line[1].split()), enumerate(lines)))
  if len(possibleMatches) != 1:
    print("ERROR ")
    print(possibleMatches)
  else:
    line_with_new_cases = list(filter(lambda x: "(+" in x, lines[possibleMatches[0][0]:]))[0]
    print(line_with_new_cases)
    
    new_cases = line_with_new_cases.split('(+')[1].split(')')[0].strip()
    date = list(filter(lambda line: "Stand: " in line, lines))[0].split("Stand: ")[1].split(",")[0]
    
    return date, new_cases

if __name__ == "__main__":
  if (len(sys.argv) < 3):
    print (README)
  else: 
    print(html_to_stats(sys.argv[1], " ".join(sys.argv[2:])))

