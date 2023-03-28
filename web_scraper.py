import requests
from bs4 import BeautifulSoup

def scrape():
  result = requests.get("https://www.campussafety.utoronto.ca/news/categories/community-safety-alerts")
  doc = BeautifulSoup(result.text, "html.parser")

  event = str(doc.find(class_ = "bD0vt9 KNiaIk").string)
  text = str(doc.find(class_ = "BOlnTh").string)

  time_text_start = text.find("Broadcast Time") + len("Broadcast Time: ")
  date_text_start = text.find("Date") + len("Date: ")

  time = text[time_text_start:text.find("Date")]
  date = text[date_text_start:text.find("Type")]

  hyphen = event.find("-", event.find("-")+1)
  event_text = event[:hyphen] + event[hyphen + 1:]
  event_text = event_text.lower().split()
  subject = "-".join(event_text)
  
  link = "https://www.campussafety.utoronto.ca/post/" + subject

  return """
Latest News
Date: %s
Time: %s
Event: %s
link: %s
""" % (date, time, event, link)