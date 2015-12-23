# Data Manipulation (week 1)

## Development


> To use virtualenv and pip in ubuntu, install via apt-get
> `$ sudo apt-get install -y python-pip python-virtualenv`

- 1. Create virtualenv with: `$ virtualenv .env`.
- 2. Use virtualenv with: `$ source ./.env/bin/activate`
- 3. Install dependencies: `$ pip install -r REQUERIMENTS.txt`


## Assignment

### Problem 1: Get Twitter Data

- [x] Create a twitter account if you do not already have one.
- [x] Go to https://dev.twitter.com/apps and log in with your twitter credentials.
- [x] Click "Create New App"
- [x] Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
- [x] At this point you will be prompted to attach a mobile phone number to your account if you have not previously done so. Follow the instructions at the link provided. If you cannot complete this protocol, you may use the sample dataset in the repository, but we encourage you to connect to Twitter if possible so you can build your own applications.
- [x] On the next page, click the "Keys and Access Tokens" tab along the top, then scroll all the way down until you see the section "Your Access Token"
- [x] Click the button "Create My Access Token". You can Read more about Oauth authorization.
You will now copy four values into the file twitterstream.py. These values are your "Consumer Key (API Key)", your "Consumer Secret (API Secret)", your "Access token" and your "Access token secret". All four should now be visible on the "Keys and Access Tokens" page. (You may see "Consumer Key (API Key)" referred to as either "Consumer key" or "API Key" in some places in the code or on the web; all three are synonyms.) Open twitterstream.py and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:

```python
api_key             = "<Enter api key>"
api_secret          = "<Enter api secret>"
access_token_key    = "<Enter your access token key here>"
access_token_secret = "<Enter your access token secret here>"
```
- [x] Run `$ python twitterstream.py > output.json` at least 3 minutes.
- [x] If you wish, modify the file to use the [twitter search API](https://dev.twitter.com/docs/api/1.1/get/search/tweets) to search for specific terms. For example, to search for the term *"microsoft"*, you can pass the following url to the `#twitterreq` function: "https://api.twitter.com/1.1/search/tweets.json?q=microsoft", run: `$ python twitterstream.py | python -mjson.tool`
- [x] The first 20 lines of the twitter data you downloaded from the web (or the first 20 lines from the sample file if you are unable to access the Twitter Developer API due to the requirement to use a mobile phone). You can save the first 20 lines to a file `problem_1_submission.txt` by using the following command: `$ head -n 20 output.json > problem_1_submission.txt`.


### Problem 2: Derive the sentiment of each tweet

For this part, you will compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet.
The sentiment of a tweet is equivalent to the **sum of the sentiment scores** for each term in the tweet.
You are provided with a skeleton file `tweet_sentiment.py` which accepts two arguments on the command line: a *sentiment file* and a tweet file like the one you generated in **Problem 1**.
You can run the skeleton program like this: `$ python tweet_sentiment.py AFINN-111.txt output.json`
The file *AFINN-111.txt* contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score.
Each word or phrase that is found in a tweet but not found in *AFINN-111.txt* should be given a sentiment score of 0. See the file *AFINN-README.txt* for more information.
To use the data in the *AFINN-111.txt* file, you may find it useful to build a dictionary. Note that the *AFINN-111.txt* file format is tab-delimited, meaning that the term and the score are separated by a tab character.
A tab character can be identified a `\t`.The following snippet may be useful:

```python
afinnfile = open("AFINN-111.txt")
scores    = {}                     # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)        # Convert the score to an integer.
print scores.items()               # Print every (term, score) pair in the dictionary
```

The data in the tweet file you generated in **Problem 1** is represented as **JSON**, which stands for JavaScript Object Notation.
It is a simple format for representing nested structures of data --- lists of lists of dictionaries of lists of .... you get the idea.
Each line of *output.txt* represents a [streaming message](https://dev.twitter.com/docs/streaming-apis/messages).
Most, but not all, will be tweets. (The skeleton program will tell you how many lines are in the file.)
