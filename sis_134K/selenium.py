from selenium import Webdriver
import requests
import os
import pickle

# Initialize the selenium webdriver
driver = webdriver.Firefox()
driver.get("https://www.example.com")

# Save the cookies to a file
cookies = driver.get_cookies()
with open("cookies.pkl", "wb") as cookie_file:
    pickle.dump(cookies, cookie_file)

# Load the cookies into a requests session
session = requests.Session()
with open("cookies.pkl", "rb") as cookie_file:
    cookies = pickle.load(cookie_file)
    for cookie in cookies:
        session.cookies.update({cookie["name"]: cookie["value"]})

# Use the session to make a request with the cookies
response = session.get("https://www.example.com")



