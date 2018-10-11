import csv
import pandas as pd

def parse(filename):
  '''
  takes a filename and returns attribute information and all the data in array of dictionaries
  '''
  # initialize variables

  out = []  
  csvfile = open(filename,'r')
  fileToRead = csv.reader(csvfile)

  headers = next(fileToRead)

  # iterate through rows of actual data
  for row in fileToRead:
    out.append(dict(zip(headers, row)))

  return out

dataset = parse("/Users/aea/Desktop/Northwestern/Year 4/Fall/EECS 349 - Machine Learning/Psets/PS1/house_votes_84.data")
print(dataset[1:10])

#print(dataset['Class'])
    

#
#def panda_parse(filename):
#    
#    csvfile = open(filename, 'r')
#    df = pd.read_csv(csvfile)
#    
#    return df
#    
    
#df = pd.read_csv(open("/Users/aea/Desktop/Northwestern/Year 4/Fall/EECS 349 - Machine Learning/Psets/PS1/house_votes_84.data", 'r'))
#
#df[1]
    
    