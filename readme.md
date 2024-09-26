# Indian Kanoon Scraper API

This Django project provides a REST API that allows you to scrape search results from Indian Kanoon and save the scraped data (title, data, and link) in a database. You can query the data by making GET requests to the API with a search parameter.

## Features
- Dynamic Scraping: Scrapes real-time data based on a user-provided search query.
- Data Storage: Saves scraped data (Title, Content, Link) in the database.
- REST API: Provides a RESTful endpoint to retrieve the scraped data.
- Character Limitation: Automatically trims content to 10,000 characters if it exceeds the limit.

## Requirements

- Python 3.11+
- Django 5.1+
- Django REST framework
- SQLite (or any other database supported by Django)
- Requests
- BeautifulSoup4

## Setup Instructions

### 1. Clone the Repository
Start by cloning the repository:
```bash
git clone https://github.com/Paras-Singh7/case-minister-assessment.git
cd article_project
```

### 2. Setup environment
It's recommended to use a virtual environment to manage dependencies:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Run Server
To start the server:
```bash
python manage.py runserver
```

## Admin access
You can access the Django admin panel to manage the scraped data:

- URL: http://127.0.0.1:8000/admin/
- Username: admin
- Password: admin123

## API Usage
You can now make GET requests to the API to scrape and retrieve data from Indian Kanoon.

### API Endpoint
- URL: /api/v1/article/
- Method: GET
- Query Parameter: searchfor=<search_query>

Example Request:
> GET http://127.0.0.1:8000/api/v1/article/?query=property+law

### Response  format
```json
[
  {
    "title": "Case Title",
    "data": "Content of the case...",
    "link": "https://www.indiankanoon.org/doc/case_link/"
  },
  {
    "title": "Another Case Title",
    "data": "More content of another case...",
    "link": "https://www.indiankanoon.org/doc/another_case_link/"
  },
  ...
]
```

