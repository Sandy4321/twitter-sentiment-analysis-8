# Data Manipulation (week 1)

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
- [ ] Run `$ python twitterstream.py > output.json` at least 3 minutes.
- [ ] If you wish, modify the file to use the [twitter search API](https://dev.twitter.com/docs/api/1.1/get/search/tweets) to search for specific terms. For example, to search for the term *"microsoft"*, you can pass the following url to the `#twitterreq` function: "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"
- [ ] The first 20 lines of the twitter data you downloaded from the web (or the first 20 lines from the sample file if you are unable to access the Twitter Developer API due to the requirement to use a mobile phone). You can save the first 20 lines to a file `problem_1_submission.txt` by using the following command: `$ head -n 20 output.json > problem_1_submission.txt`.
