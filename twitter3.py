from TwitterSearch import *
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
    for tweet in ts.search_tweets_iterable(tso):
        try:
            print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        except UnicodeEncodeError:
            pass

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
