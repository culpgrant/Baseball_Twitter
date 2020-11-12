import json
import requests
import tweepy

def lambda_function(event = None, context = None):
    url = 'https://www.fangraphs.com/api/playoff-odds/odds'
    url_tweet = 'https://www.fangraphs.com/standings/playoff-odds/fg/mlb'
    session = requests.session()
    response = session.get(url)
    result = json.loads(response.text)
    for team in result:
        if team['shortName'] == "Cubs":
            cubs_playoff_odds = int(float(team['endData']['poffTitle'])*100)
            cubs_ws_odds = int(float(team['endData']['csWin'])*100)
        if team['shortName'] == "White Sox":
            sox_playoff_odds = int(float(team['endData']['poffTitle'])*100)
            sox_ws_odds = int(float(team['endData']['csWin'])*100)

    consumer_key = '' #API KEY
    consumer_secret = '' #API_SECRET_KEY
    access_token = '' #bearertoken/accesstoken
    access_token_secret = '' #accesstokensecret


    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    tweet_text = f"""
    Cubs Playoff Prob: {cubs_playoff_odds}%.
    Cubs WS Win Prob: {cubs_ws_odds}%.
    White Sox Playoff Prob: {sox_playoff_odds}%.
    White Sox WS Win Prob: {sox_ws_odds}%.
    #Cubs #Whitesox
    source: {url_tweet}
        """
    return api.update_status(tweet_text)
lambda_function()
