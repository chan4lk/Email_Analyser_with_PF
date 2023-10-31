import re
import json
from promptflow import tool

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
  text = "The emails for today are as follows:\n\n1. Subject: Updates from Clean Coders Club at BISTEC Global\n   Category: Low-priority\n   Sender: Clean Coders Club BG\n\n2. Subject: Agile Quiz Competition\n   Category: Important\n   Sender: Project Management Initiative\n\n3. Subject: Hearts Meeting- October 2023\n   Category: Important\n   Sender: Thushini Maheepala\n\n4. Subject: Happy Announcement!\n   Category: Low-priority\n   Sender: Thushini Maheepala\n\n5. Subject: None\n   Category: Unknown\n   Sender: Unknown"

# Split the text into separate emails using a regular expression
  emails = re.split(r'\d+\.', text)
  category_rate_mapping = {
    "Low-priority": 1,
    "Important": 2,
    "Urgent": 3	
  }

  # Initialize variables to store email details
  email_details = []
  for email in emails:
      email = email.strip()
      if not email:
          continue

      subject_match = re.search(r'Subject: (.+)', email)
      category_match = re.search(r'Category: (.+)', email)
      sender_match = re.search(r'Sender: (.+)', email)

      if subject_match and category_match:
          category = category_match.group(1).strip()
          rate = category_rate_mapping.get(category, 0)
      
          email_info = {
              "Subject": subject_match.group(1).strip(),
              "Category": category,
              "Rate": rate
          }

          if sender_match:
              email_info["Sender"] = sender_match.group(1).strip()

          email_details.append(email_info)

  # Sort the emails by rate
  email_details = sorted(email_details, key=lambda x: x["Rate"], reverse=True)

  # Convert the list of email details to a JSON array
  json_data = json.dumps(email_details, indent=4)

  formatted_messages = []
  formatted_string = "\n The emails for today are as follows: Here  they are the summarized \n \n"

  for email_info in email_details:
      subject = email_info["Subject"]
      category = email_info["Category"]
      sender = email_info.get("Sender", "N/A") # If the sender is not available, use "N/A"
      
      message = f"\r\r\r Mail Category: \"{category}, Subject: \"{subject}\", Sender: \"{sender}\"\n"
      
      formatted_messages.append(message)
      formatted_string += message

  formatted_string += "\nPlease let me know if you need any further assistance."	
  # for message in formatted_messages:
  #   print(message)

  return formatted_string

my_python_tool('')
