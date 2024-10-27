# import classes and functions FOR selenium
# will return all the content from the website 
# bright data (allows to get past captcahs and it bans)

import selenium.webdriver as webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup # html parser
import os


def scrape_website(website):
    print("Launching Chrome browser...")

    chrome_driver_path = "./chromedriver"  # Update this path if necessary
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Create a Service object to pass to the WebDriver
    service = Service(chrome_driver_path)
    
    # Initialize the Chrome WebDriver with options
    with webdriver.Chrome(service=service, options=options) as driver:
        # Navigate to the specified website
        driver.get(website)
        print("Navigated! Scraping page content...")
        
        # Get the page source
        html = driver.page_source
        return html

#--- helper fucntiosn that will clean up so the data you pass in to LLM removes the nonsense you dont wnat
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return "" # just so no errors

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # for loop: going to look inside the parsed content (soup), then its getting rid of the tags script and style
    for script_or_style in soup(["script", "style"]): # 
        script_or_style.extract() # remvoing

    cleaned_content = soup.get_text(separator='\n')
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
    
    return cleaned_content


'''s pliting up into batches 
     becasue when using LLM, have a token limit (8k chracters)
         so spilit text from webpages up in to batches of whatever the max content character limit is'''
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ] # create dom_content, from index i (0), from i + maxlength, so the for loop is now 6000 and it will keep going up by setting i to the next 6000 
