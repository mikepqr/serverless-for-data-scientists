# Serverless for data scientists

Code and notebooks for a talk given at PyBay, 2018-08-19.

 - [The talk (slides and words)](https://mike.place/talks/serverless/)

## Contents

 1. [Deployment of a basic flask application with zappa](zappa/)
 2. [Pywren demo](pywren/)
 3. [Hyperparameter optimization with pywren](hyperparameters/)
 4. [Model deployment on AWS Lambda with zappa](modelserver/)

## Coming soon

 - A link to the talk recording

## Projects and resources mentioned in the talk

 - [zappa](https://github.com/Miserlou/zappa) -- tool for AWS Lambda deployment
   of Python applications
 - [dwx](http://github.com/williamsmj/dwx) -- Twitter bot that runs on AWS
   Labmda.
 - [Serving 39 Million Requests for
   $370/Month](https://trackchanges.postlight.com/serving-39-million-requests-for-370-month-or-how-we-reduced-our-hosting-costs-by-two-orders-of-edc30a9a88cd)
   -- AWS Lambda migration example
 - [Occupy the Cloud: Distributed Computing for the
   99%](https://arxiv.org/abs/1702.04024) -- the pywren paper
 - [pywren](https://github.com/pywren/pywren) -- tool for embarrassingly
   parallel computation using AWS Lambda as the backend
 - [riscamp 2017 pywren
   tutorial](https://github.com/ucbrise/risecamp/tree/risecamp2017/pywren) --
   more detailed look at pywren than my talk
 - [pywren web
   scraping](https://blog.seanssmith.com/posts/pywren-web-scraping.html) --
   blog post that inspired the webscraping example in the talk
 - [305 Million Solutions to The Black-Scholes Equation in 16 Minutes with AWS
   Lambda](http://www.bradfordlynch.com/blog/2017/05/28/ComputeOnLambda.html)
   -- large scale embarrassingly parallel numerical computation example
 - [nips.json](https://github.com/williamsmj/nips.json) -- code to scrape the
   NIPS website using pywren (and the data scraped)
 - [Encoding, Fast and Slow: Low-Latency Video Processing Using Thousands of
   Tiny
   Threads](https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/fouladi)
   -- an example of AWS Lambda as part of a long-lived data processing pipeline
   (doesn't use pywren)
