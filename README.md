# Neural Big Sean Bot

A pointless application of text-based Recurrent Neural Network training to generate "Big Sean" lyrics from scraping data.

## Why

I still don't know

## How

1. Scraped lyrics for all Big Sean songs from Genius.com using their API
2. Flattened lyrics into text file, separated by each lyric line
3. Trained a recurrent neural network using [TextGenRNN](https://github.com/minimaxir/textgenrnn) and 200,000 lines of his lyrics
4. Generated 1,000 sample lyrics
5. Created a CRON job to tweet one lyric every hour