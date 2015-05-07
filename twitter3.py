from TwitterSearch import *
import re

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['gate']) # let's define all words we would like to have a look for
    tso.set_include_entities(False) # and don't give us all those entity information
    tso.set_language('en')
    tso.set_count(25)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'UMsyzWOqZAEjeRqNcpiElwVtd',
        consumer_secret = '4o3zE5Ty5Oq0XsMRueXOgtHZLc3WaDUTOt10gHXnckwRqCaxYe',
        access_token = '305678511-oP3uuW73E7VBkiN7Q7FpVsWMp5tv2UrkAQVXR4vN',
        access_token_secret = 'kyyCTWICTmnsyGczDvNieNbrJJSsIjjfE9uwmsnGNEqGR'
     )

     # this is where the fun actually starts :)
     # Will find all tweets where the text includes -gate or a word with gate at the end
     # won't catch gate by itself because that leads to a ton of false positives
    for tweet in ts.search_tweets_iterable(tso):
        try:
            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            matchObj = re.match('(\w+|\w+-)gate', tweet['text'], re.I)
            if matchObj:
                #print("Found a match! ", matchObj.group())
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
           # else:
               # print("No match")
        except UnicodeEncodeError:
            pass

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
