# this script scrapes information from a website
import requests
from bs4 import BeautifulSoup

def web_scraper():
    URL = "https://infosec-jobs.com/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id = "job-list")

    job_elements = results.find_all("div", class_="list-group-item px-2 px-lg-3 py-0")
    for job_element in job_elements:
        company = job_element.find("p", class_ = "m-0 text-muted job-list-item-company")
        title = job_element.find("h3", class_ = "h5 mb-1")
        location = job_element.find("span", class_ = "d-block d-md-none text-break job-list-item-location")
        date_posted = job_element.find("span", class_ = "d-block text-muted")
        apply = job_element.find("a", class_ = "col list-group-item-action p-2")
        
        print(company.text.strip())
        print(title.text.strip())
        print(location.text.strip())
        print(date_posted.text.strip())
        print(apply.text.strip())
        print()
        print()  

web_scraper()