import MapReduce
import json
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)

def reducer(key, value):
    # key: person
    # value: list of friends
    for friend in value:
        try: 
            friends_list = mr.intermediate[friend]
            if (key not in friends_list):
                mr.emit((key, friend))
                mr.emit((friend,key))
        except KeyError:
            mr.emit((key, friend))
            mr.emit((friend,key))
            

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
