from datetime import datetime
from pytz import timezone

lastest_event = ""

def check_similar_post(post):
  global lastest_event
  
  tz = timezone("EST")
  current_date = datetime.now(tz).day

  date_text = post[post.find("Date"):post.find("Event")]
  data_third_space = date_text.find(" ", date_text.find(" ", date_text.find(" ") + 1) + 1)
  data_second_comma = date_text.find(",", date_text.find(",") + 1)

  post_date = int(date_text[data_third_space + 1:data_second_comma])

  event_text = post[post.find("Event"):post.find("link")]
  event_fourth_space = event_text.find(" ", event_text.find(" ", event_text.find(" ", event_text.find(" ") + 1) + 1) + 1)

  post_event = event_text[event_fourth_space + 1:-1]
  
  if current_date == post_date and lastest_event != post_event:
    print("Not posted")
    lastest_event = post_event
    return True
  else:
    print("Posted")