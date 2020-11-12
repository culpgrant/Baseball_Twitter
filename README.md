# Baseball_Twitter
Daily Baseball Twitter that tweets out playoff/WS probability for Chicago Cubs and White Sox from Fangraphs.
Link to [Twitter account](https://twitter.com/CubsPlayoff) follow me if you want!


## Motivation:
This was a project that I wanted to create because I like baseball and the analytics surrounding the sport. I decided to create a Twitter bot that would tweet out the Cubs/White Sox playoff and World Series Championship odds every morning at 8:00 am (CST).

## How:
I am running this code as an AWS lambda function. To create the AWS Lambda function I used a deployment package with the python packages necessary. I make a call to their API with the requests library and then do some data cleaning from that part to drill down to the two teams I need and the two statistics I need.

## Code Resources:
- **Python Version:** 3.8
- **Packages:** [tweepy](http://docs.tweepy.org/en/latest/), [requests](https://requests.readthedocs.io/en/master/)

## Reflection:
This was a good lesson on branding because I messed up the branding by only using Cubs in the handle. I had originally only intended to do this for the Cubs but a lot of my friends are Sox fans so I expanded it.
