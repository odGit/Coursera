import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
# Map function
# mr - MapReduce object
# data - json object formatted as a string
def mapper(record):
    document = record[0]
    words = record[1].split()
    unique_words = list(set(words))
    for unique_word in unique_words:
        mr.emit_intermediate(unique_word, document)
    # output (key, value) pair (only for mapper)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer( key, list_of_values):
    print list_of_values
    # output item (only for reducer)
    mr.emit((key, list_of_values))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
