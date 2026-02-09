import requests
from bs4 import BeautifulSoup
import os

head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }


def grab_pdf(title, pdf_link):
    with requests.get(pdf_link, stream=True, timeout=30, headers=head) as r:
        r.raise_for_status()
        #file download
        with open(f"./pdfs/{title}.pdf", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def webpage_parser(page_link):
    soup = BeautifulSoup(requests.get(page_link).text, 'html.parser')
    os.makedirs(f"pdfs", exist_ok=True) #create folder for pdfs
    #loop through each link. check if pdf --> download
    for pdf_links in soup.find_all("a"):
        if ".pdf" in pdf_links.get("href").lower():
            grab_pdf(pdf_links.get_text(), pdf_links.get("href"))
        
