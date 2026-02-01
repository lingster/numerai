# Ling's Numerai notes

This repo contains notes and my findings on Numerai Datascience Tournament. 

## EDA folder
The folder EDA, contains a reasonably comprehensive set of reports from EDA(exploratory data analysis)
of the Numerai v5.0 dataset. This may be a useful first read to get a feel of the data and potentionally
what models to build to make predictions for the numerai challenge. 

## GraphQL 
Numerai provides a GraphQL endpoint that allows you to retrieve the performance of your models and other
data. 
The file: [`numerai_graphql.md`](numerai_graphql.md) provides details on how to access the GraphQL data and make queries to 
retrieve the data that you may need. Just paste this into your nearest LLM prompt and ask it to build code to get your 
resolved rounds submission history. 

Hope this will be useful to fellow datascientists out there! If anyone has any questions etc, feel free to 
raise an Issue in github, or you can find me in the Numerai discord.

## Utils
A collection of python tools to retrieve and compare your performance against other models

## Discord
There's signal and noise in the discord channel, so for the benefit of anyone wanting to come up to speed, I've 
created a summary of the main channels with potentially useful tidbits of information for anyone who's new here like I was. 
Check out [`discord`](https://github.com/lingster/numerai/tree/main/discord)
