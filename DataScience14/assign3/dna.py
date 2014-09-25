import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence_id
    # value: nucleotide less 10 last characters
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[-0:-10], value[-0:-10])

def reducer(key, value):
    # key: person
    # value: list of friends
    mr.emit(value[0])
            

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
