## SFI Scraper

Python script to download PDFs of statements of financial interest from Ethics Commission website.

#### Prerequistes

- Python 3.7+
- Chrome installed and located in your applications folder.
- Chromedriver. Here's a guide for installing on Mac (pretty easy) and here's a guide for installing on Ubuntu 16.04
 or 18.04 (a little trickier but not too bad).

#### Run
Usage from command line:

First arg: start page ID (starting at 1)
Second arg: end page ID (should be safe to end at 340000)
Third arg: int to append to the csv file name

Eg.

```python main.py 1 30000 1```