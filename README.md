# UniTrackAI – Academic Data Extraction

## Project Overview
This project automates a sample academic website using Python and Selenium. It extracts course names, assignments, and deadlines using BeautifulSoup, then saves the information in a JSON file.

## Technologies Used
- Python
- Selenium
- BeautifulSoup
- JSON

## Installation
Install the required libraries:

bash python -m pip install selenium beautifulsoup4 

## How to Run
1. Make sure sample.html and extractor.py are in the same folder.
2. Open the project folder in VS Code.
3. Run the following command:

bash python extractor.py 

## Output
The extracted data is saved in academic_data.json.

## Error Handling
The program handles:
- Missing HTML files.
- Missing course information.
- Missing assignment details.
- Missing deadlines.
- Browser errors.