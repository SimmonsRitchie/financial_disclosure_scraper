## Financial Disclosure Scraper

Python script to download PDFs of statements of financial interest from Ethics Commission website.

#### Requirements

- Python 3.7+
- Chrome installed and located in your applications folder.
- Chromedriver. Here's a guide for installing on Mac (pretty easy) and here's a guide for installing on Ubuntu 16.04
 or 18.04 (a little trickier but not too bad).

#### Install

1. Open the terminal. Clone the project repo:

    `git clone https://github.com/SimmonsRitchie/financial_disclosure_scraper.git`

2. If you don't have pipenv installed on your machine, run:

    `pip install pipenv`

3. Navigate into the project directory:

    `cd financial_disclosure_scraper`
     
4. Use pipenv to create a virtual environment and install the project 
dependencies. Run:

    `pipenv install`

5. If needed, configure the environmental variables in .env in the root of the project directory:
     
     `nano .env`
 
 Refer to the comments for what each variable does.



#### Run

From the terminal, make sure you're in the project directory. Run the following:

```python scraper/runner.py```

Or:

```pipenv run python scraper/runner.py```

#### Contributors

Ian Walker, Daniel Simmons-Ritchie.