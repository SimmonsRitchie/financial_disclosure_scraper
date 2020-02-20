## SFI Scraper

Python script to download PDFs of statements of financial interest from Ethics Commission website.

#### Requirements

- Python 3.7+
- Chrome installed and located in your applications folder.
- Chromedriver. Here's a guide for installing on Mac (pretty easy) and here's a guide for installing on Ubuntu 16.04
 or 18.04 (a little trickier but not too bad).

#### Install

1. Open the terminal. Clone this repo:

    `git clone https://github.com/SimmonsRitchie/financial_disclosure_scraper.git`

2. If you don't have pipenv installed, run:

    `pip install pipenv`

3. Navigate into the project directory:

    `cd court_docket_scraper`
     
4. Use pipenv to create a virtual environment and install the project 
dependencies. Run:

    `pipenv install`

5. If needed, configure the environmental variables in .env in the root of the project directory. Refer to the
 comments for what each variable does. If you're not sure, leave the file as it is.:

    `nano .env`

#### Run
Usage from command line:

First arg: start page ID (starting at 1)
Second arg: end page ID (should be safe to end at 340000)
Third arg: int to append to the csv file name

From the terminal, make sure you're in the project directory. Run the following:

```python main.py```

Or:

```pipenv run python main.py```

#### Contributors

Ian Walker, Daniel Simmons-Ritchie.