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
    new_dict = dict()
    for index in range(len(tweets)):
        count = 0
        tweet_words = tweets[index].split()
        for word in tweet_words:
            word = (word
                    .replace("\n", "")
                    .replace(",", "")
                    .replace(".", "")
                    .replace("!", "")
                    .replace("?", "")
                    .rstrip()).lower()  #stripe off chars and converting in lower case
            if word.encode("utf-8") in senti_dict.keys():
                count += senti_dict[word]
                
        new_dict[tweets[index]] = count

        return new_dict

def tweetDict(tweets_weight, sent_dict):
    newer_dict = dict()
    

#    for new_term, sent_values in new_terms_dict.iteritems():
#        sent_average = float(sum(sent_values))/float(len(sent_values))
#        print new_term.encode('utf-8'), str(sent_average)



    
def main():
    sentimentData = sys.argv[1] #AFIN-111.txt
    twitterData = sys.argv[2] #output.txt
    
    t = tweetsList(readFile(twitterData))  #tweeter List
    
    sent_dict = sentimentDict(readFile(sentimentData)) #create a sentimet dictionary from the provided file
    myCounter(sent_dict,t)

if __name__ == '__main__':
    main()