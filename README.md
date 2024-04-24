# Web Scraping With Python Scrapy Framework

## A web scraping project made with python's scrapy framework, data from petlebi.com was crawled, stored in a json format and then the json data stored into a MySQL Database.

To run this project and scrape the data, you need to first create a virtual environment and activate it, depending on your OS this step may vary, below you can find the instructions.

Windows:

``` cmd

python3 -m venv venv
.\venv\Scripts\activate

cd ..\DirectoryOfTheRepository\petlebiScraper

scrapy crawl petlebi -O petlebi_products.json

```

Linux: 

``` unix
python3 -m venv venv
source \venv\bin\activate

cd ..\DirectoryOfTheRepository\petlebiScraper

scrapy crawl petlebi -O petlebi_products.json
```

After you can use the .sql files to create the database and the .py file to store the json formatted data.
