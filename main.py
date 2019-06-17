import pandas as pd
import requests
from bs4 import BeautifulSoup


def download_iris(csv_file='output.csv'):
    link = 'https://en.wikipedia.org/wiki/Iris_flower_data_set'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, features="lxml")
    iris_table = soup.find_all('table')[0]
    iris_dataframe = pd.read_html(str(iris_table))[0]
    iris_dataframe.to_csv(csv_file)


download_iris()
