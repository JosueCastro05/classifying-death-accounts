# Web scraping functions

import requests
from bs4 import BeautifulSoup
import json
import re


def scrape_data(data_url):
    print('Scraping data...')
    url = data_url
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the first 1000 characters of the response for debugging
    # print(soup.prettify()[:200])

    stories = []
    for story_div in soup.select('div.container.clearfix'):
        text = story_div.get_text(separator=' ', strip=True)

        #Split the parts, because it is giving me the whole div container
        parts = re.split(r'(?m)(?=\n?\d{4,}\.)', text)
        for part in parts:
            cleaned = part.strip()
            cleaned = cleaned.replace('â\x80\x94', '--')
            if len(cleaned)>100:
                stories.append({'text': cleaned, 'label': 'NDE'})
    return stories

jan_to_jun_2025 = scrape_data("https://www.nderf.org/Archives/2_1_2025.html")
july_to_dec_2024 = scrape_data("https://www.nderf.org/Archives/2_6_2024.html")
jan_to_jun_2024 = scrape_data("https://www.nderf.org/Archives/2_1_2024.html")
july_to_dec_2023 = scrape_data("https://www.nderf.org/Archives/2_6_2023.html")
jan_to_jun_2023 = scrape_data("https://www.nderf.org/Archives/2_1_2023.html")
july_to_jun_2022 = scrape_data("https://www.nderf.org/Archives/2_6_2022.html")
jan_to_jun_2022 = scrape_data("https://www.nderf.org/Archives/2_1_2022.html")
july_to_dec_2021 = scrape_data("https://www.nderf.org/Archives/2_6_2021.html")
jan_to_jun_2021 = scrape_data("https://www.nderf.org/Archives/2_1_2021.html")
july_to_dec_2020 = scrape_data("https://www.nderf.org/Archives/2_6_2020.html")
jan_to_jun_2020 = scrape_data("https://www.nderf.org/Archives/2_1_2020.html")
july_to_dec_2019 = scrape_data("https://www.nderf.org/Archives/2_6_2019.html")
jan_to_jun_2019 = scrape_data("https://www.nderf.org/Archives/2_1_2019.html")
july_to_dec_2018 = scrape_data("https://www.nderf.org/Archives/2_6_2018.html")
jan_to_jun_2018 = scrape_data("https://www.nderf.org/Archives/2_1_2018.html")
july_to_dec_2017 = scrape_data("https://www.nderf.org/Archives/2_6_2017.html")
jan_to_jun_2017 = scrape_data("https://www.nderf.org/Archives/2_1_2017.html")
july_to_dec_2016 = scrape_data("https://www.nderf.org/Archives/2_6_2016.html")
jan_to_jun_2016 = scrape_data("https://www.nderf.org/Archives/2_1_2016.html")
july_to_dec_2015 = scrape_data("https://www.nderf.org/Archives/2_6_2015.html")
jan_to_jun_2015 = scrape_data("https://www.nderf.org/Archives/2_1_2015.html")
july_to_dec_2014 = scrape_data("https://www.nderf.org/Archives/2_6_2014.html")
jan_to_jun_2014 = scrape_data("https://www.nderf.org/Archives/2_1_2014.html")
july_to_dec_2013 = scrape_data("https://www.nderf.org/Archives/2_6_2013.html")
jan_to_jun_2013 = scrape_data("https://www.nderf.org/Archives/2_1_2013.html")
july_to_dec_2012 = scrape_data("https://www.nderf.org/Archives/2_6_2012.html")
jan_to_jun_2012 = scrape_data("https://www.nderf.org/Archives/2_1_2012.html")
july_to_dec_2011 = scrape_data("https://www.nderf.org/Archives/2_6_2011.html")
jan_to_jun_2011 = scrape_data("https://www.nderf.org/Archives/2_1_2011.html")
july_to_dec_2010 = scrape_data("https://www.nderf.org/Archives/2_6_2010.html")
jan_to_jun_2010 = scrape_data("https://www.nderf.org/Archives/2_1_2010.html")
july_to_dec_2009 = scrape_data("https://www.nderf.org/Archives/2_6_2009.html")
jan_to_jun_2009 = scrape_data("https://www.nderf.org/Archives/2_1_2009.html")
july_to_dec_2008 = scrape_data("https://www.nderf.org/Archives/2_6_2008.html")
jan_to_jun_2008 = scrape_data("https://www.nderf.org/Archives/2_1_2008.html")
july_to_dec_2007 = scrape_data("https://www.nderf.org/Archives/2_6_2007.html")
jan_to_jun_2007 = scrape_data("https://www.nderf.org/Archives/2_1_2007.html")
july_to_dec_2006 = scrape_data("https://www.nderf.org/Archives/2_6_2006.html")
jan_to_jun_2006 = scrape_data("https://www.nderf.org/Archives/2_1_2006.html")
july_to_dec_2005 = scrape_data("https://www.nderf.org/Archives/2_6_2005.html")
jan_to_jun_2005 = scrape_data("https://www.nderf.org/Archives/2_1_2005.html")
july_to_dec_2004 = scrape_data("https://www.nderf.org/Archives/2_6_2004.html")
jan_to_jun_2004 = scrape_data("https://www.nderf.org/Archives/2_1_2004.html")
year_2003 = scrape_data("https://www.nderf.org/Archives/2_2003.html")
july_to_dec_2002 = scrape_data("https://www.nderf.org/Archives/2_6_2002.html")
jan_to_jun_2002 = scrape_data("https://www.nderf.org/Archives/2_1_2002.html")
years_1998_to_2001 = scrape_data("https://www.nderf.org/Archives/2_1998_2001.html")

# Combine all the scraped data into a single list
all_stories = (
    jan_to_jun_2025 +
    july_to_dec_2024 +
    jan_to_jun_2024 +
    july_to_dec_2023 +
    jan_to_jun_2023 +
    july_to_jun_2022 +
    jan_to_jun_2022 +
    july_to_dec_2021 +
    jan_to_jun_2021 +
    july_to_dec_2020 +
    jan_to_jun_2020 +
    july_to_dec_2019 +
    jan_to_jun_2019 +
    july_to_dec_2018 +
    jan_to_jun_2018 +
    july_to_dec_2017 +
    jan_to_jun_2017 +
    july_to_dec_2016 +
    jan_to_jun_2016 +
    july_to_dec_2015 +
    jan_to_jun_2015 +
    july_to_dec_2014 +
    jan_to_jun_2014 +
    july_to_dec_2013 +
    jan_to_jun_2013 +
    july_to_dec_2012 +
    jan_to_jun_2012 +
    july_to_dec_2011 +
    jan_to_jun_2011 +
    july_to_dec_2010 +
    jan_to_jun_2010 +
    july_to_dec_2009 +
    jan_to_jun_2009 +
    july_to_dec_2008 +
    jan_to_jun_2008 +
    july_to_dec_2007 +
    jan_to_jun_2007 +
    july_to_dec_2006 +
    jan_to_jun_2006 +
    july_to_dec_2005 +
    jan_to_jun_2005 +
    july_to_dec_2004 +
    jan_to_jun_2004 +
    year_2003 +
    july_to_dec_2002 +
    jan_to_jun_2002 +
    years_1998_to_2001
)

print(f'Total stories scraped: {len(all_stories)}')

