from pprint import pp
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# Visit the website and convert the webpage to text form
response = requests.get(url="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
response.raise_for_status()
result = response.text

soup = BeautifulSoup(result, "lxml")

# Get relevant data from the necessary fields
ranks = [rank.get_text() for rank in soup.select(selector=".csr-col--rank .data-table__value")]
majors = [major.get_text() for major in soup.select(selector=".csr-col--school-name .data-table__value")]
values = [value.get_text() for value in soup.select(selector=".csr-col--right .data-table__value")]

# Get the salary values
early_career_pay = values[0:-1:3]
mid_career_pay = values[1:-1:3]
high_meaning = values[2:-1:3]

# Create a dictionary of values retrieved and store it into a csv file
salary_data = {
    "Major": majors,
    "Early Career Pay": early_career_pay,
    "Mid Career Pay": mid_career_pay,
}

df = pd.DataFrame(salary_data)
df.to_csv('salaries_from_payscale.csv')







