# PDF Grabber

A simple Python script that downloads all PDF files from a webpage.

## What it does

Scrapes a webpage for PDF links and downloads them all to a local `pdfs` folder.

## Requirements
```bash
pip install requests beautifulsoup4
```

## Usage
```python
from pdf_grabber import webpage_parser

# Download all PDFs from a webpage
webpage_parser("https://example.com/page-with-pdfs")
```

Or run directly in the script by adding:
```python
if __name__ == "__main__":
    webpage_parser("YOUR_URL_HERE")
```

## How it works

- Fetches the webpage HTML
- Finds all links containing `.pdf`
- Downloads each PDF with the link text as filename
- Saves to `./pdfs/` directory (created automatically)

## Notes

- Filenames are based on link text from the page
- Downloads are streamed in chunks for efficiency
- 30-second timeout per download
