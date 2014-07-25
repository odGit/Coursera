import sys
import json


def readFile(fName):
    ''''(file) -> list
    Read the file and return a list'''
    file_data = open(fName)
    new_list = []
    for line in file_data:
        new_list.append(line)
        
    file_data.close()
    
    return new_list


def tweetsList(tList):
    ''' list -> list of tweet text'''
    parsed = []
    pythonResults = []
    for line in tList:
        data = json.loads(line.strip())
        pythonResults.append(data)
        
    for t in pythonResults:
        if 'text' not in t.keys():
            continue
        else:
            parsed.append(t["text"])
    
    return parsed
         
def sentimentDict(sList):
    ''' list -> dictionary'''
    sentiment = dict()
    for line in sList:
        term, value  = line.split("\t") # The file is tab-delimited. "\t"
        sentiment[term] = int(value)
        
    return sentiment
    
def myCounter(senti_dict, tweets):
    for index in range(len(tweets)):
        count = 0
        tweet_words = tweets[index].split()
        for word in tweet_words:
            word = (word.rstrip('?:!.,;"!@')).lower()  #stripe off chars and converting in lower case
            if word.encode("utf-8") in senti_dict.keys():
                count += senti_dict[word]
#        print tweets[index]
        print count
    
def main():
    sentimentData = sys.argv[1] #AFIN-111.txt
    twitterData = sys.argv[2] #output.txt
    
    t = tweetsList(readFile(twitterData))

    s = sentimentDict(readFile(sentimentData))
    myCounter(s,t)

if __name__ == '__main__':
    main()