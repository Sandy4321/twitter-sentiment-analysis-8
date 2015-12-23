#!/usr/bin/env python

import sys
import json


def load_scores(data):
    scores = {}
    for line in data:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def tweets_digest(data):
    tweets = []
    for line in data:
        tweet = json.loads(line, encoding="utf-8")
        if valid_tweet(tweet):
            tweets.append(tweet)
    return tweets


def valid_tweet(tweet):
    return tweet.has_key("text")

def init():
    afinn  = open(sys.argv[1])
    dump   = open(sys.argv[2])
    scores = load_scores(afinn)
    tweets = tweets_digest(dump)

    print "Loaded %s scores\n\n" % len(scores)

    for index, tweet in enumerate(tweets, start=1):
        print "%s: @%s: \"%s\" -- %s" % (index, tweet["user"]["screen_name"], tweet['text'], tweet['lang'])


if __name__ == '__main__':
    init()
