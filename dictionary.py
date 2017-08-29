"""from collections import defaultdict

sentence = "Peter piper picked a peck of pickled peppers A peck of pickled " \
           "peppers Peter piper picked If Peter piper picked a peck of pickled "\
            "peppers Wheres the peck of pickled peppers Peter piper picked"

word_dict = defaultdict(int)

for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1"""


#print(word_dict)#


"""from collections import Counter
sentence = "Peter piper picked a peck of pickled peppers A peck of pickled " \
           "peppers Peter piper picked If Peter piper picked a peck of pickled "\
            "peppers Wheres the peck of pickled peppers Peter piper picked"
words =  sentence.split()

words_count = Counter(words)

print("word counter : ",words_count)

from collections import defaultdict

user_movie_Rating =  defaultdict(lambda : defaultdict(int))

user_movie_Rating["Alice"]["LOR1"] = 4
user_movie_Rating["Alice"]["LOR2"]= 5
user_movie_Rating["Alice"]["LOR3"] = 3
user_movie_Rating["Alice"]["SW1"] = 5
user_movie_Rating["Alice"]["SW2"] = 3

print(user_movie_Rating)"""

import twitter
CONSUMER_KEY = 'xgAnvfxgrEQPtDayyC4mwy5Kw'
CONSUMER_SECRET = '00XjuE2sFP0WHycI7pWJ5FgUxDbTJJX8yfGieaJECl8P3nm8rN'
OUATH_TOKEN = '423899151-dDL1vM6J3nfnGJghmqsPg6sNdmKlwhIB1gX7qpMo'
OUATH_TOKEN_SECRET = 'cTCegnjH3otlxvvTdivzjnKsOWKp7uNmKaODoBWVdYzqH'

auth = twitter.OAuth(OUATH_TOKEN,OUATH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_api =twitter.Twitter(auth=auth)

print (twitter_api)


