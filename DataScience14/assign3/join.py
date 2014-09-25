import MapReduce
import json
import sys

mr = MapReduce.MapReduce()
# Map function
# mr - MapReduce object
# data - json object formatted as a string
orders = {}
def mapper(record):
    table_name = record[0]
    order_number = record[1]
    if (table_name == "order"):
        orders[order_number] = record
    else: 
        mr.emit_intermediate(order_number, record)
    # output (key, value) pair (only for mapper)

# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer( key, line_items):
    # output item (only for reducer)
    for line_item in line_items:
        mr.emit(orders[key] + line_item)

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    MapReduce.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
