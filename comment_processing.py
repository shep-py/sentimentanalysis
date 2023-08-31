from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
def vader_analyse(comment):
    obj=SentimentIntensityAnalyzer()
    sentiment_dict=obj.polarity_scores(comment)
    neg=sentiment_dict['neg']
    neu=sentiment_dict['neu']
    pos=sentiment_dict['pos']
    return [neg,neu,pos]



