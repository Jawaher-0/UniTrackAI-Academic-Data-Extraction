from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import json
import os

driver = None

try:
    # Check if sample website exists
    file_path = os.path.abspath("sample.html")

    if not os.path.exists(file_path):
        raise FileNotFoundError("sample.html was not found")

    # Open website using Selenium
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get("file:///" + file_path.replace("\\", "/"))

    html_content = driver.page_source

    # Extract website information
    soup = BeautifulSoup(html_content, "html.parser")

    courses_data = []

    # Find all courses
    courses = soup.find_all("div", class_="course")

    if not courses:
        print("Warning: No courses found!")

    for course in courses:

        course_title = course.find("h2")
        course_name = (
            course_title.get_text(strip=True)
            if course_title else "Unknown Course"
        )

        assignment = course.find("div", class_="assignment")

        if assignment:
            assignment_title = assignment.find("h3")
            deadline_element = assignment.find("p", class_="deadline")

            assignment_name = (
                assignment_title.get_text(strip=True)
                if assignment_title else "No Assignment"
            )

            deadline = (
                deadline_element.get_text(strip=True)
                if deadline_element else "No Deadline"
            )

        else:
            assignment_name = "No Assignment"
            deadline = "No Deadline"

        courses_data.append({
            "course": course_name,
            "assignment": assignment_name,
            "deadline": deadline
        })

    # Save data as JSON
    with open("academic_data.json", "w", encoding="utf-8") as file:
        json.dump(courses_data, file, indent=4, ensure_ascii=False)

    print("Data extracted successfully!")
    print(json.dumps(courses_data, indent=4, ensure_ascii=False))

except FileNotFoundError as error:
    print("File Error:", error)

except WebDriverException as error:
    print("Browser Error:", error)

except Exception as error:
    print("Unexpected Error:", error)

finally:
    if driver:
        driver.quit()
        print("Browser closed successfully!")