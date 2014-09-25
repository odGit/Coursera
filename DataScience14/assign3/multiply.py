import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i,j) of the resulting matrix
    # value: (n, val) where n is the col or row and val is the value of original matrix
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    if (matrix == "a"):
        for col in range(0,5):
            key = (i,col)
            value = (j, val)
            mr.emit_intermediate(key, value)
    elif (matrix == "b"):
        for row in range(0,5):
            key = (row,j)
            value = (i, val)
            mr.emit_intermediate(key, value)

def reducer(key, value):
    # key: matrix position
    # value: sume of all multiples
    sum_of_products = 0
    list_of_indexes = []
    temp_hash = {}
    for tup in value:
        temp_hash.setdefault(tup[0], [])
        temp_hash[tup[0]].append(tup[1])
    for k in temp_hash:
        if(len(temp_hash[k]) == 2):
            product = temp_hash[k][0] * temp_hash[k][1]
            sum_of_products = sum_of_products + product
    result = list(key)
    result.append(sum_of_products)
    mr.emit(tuple(result)) 
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
