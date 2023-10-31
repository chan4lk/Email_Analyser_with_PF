import json
from bs4 import BeautifulSoup
from promptflow import tool
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

@tool
def process_json_with_sentiment_analysis():
    with open('data.json', 'r') as file:
        json_data = json.load(file)

    contents = [item['body']['content'] for item in json_data['value']]
    subjects = [item['subject'] for item in json_data['value']]

    def convert_html_to_text(html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    plain_texts = [convert_html_to_text(content) if any(tag for tag in BeautifulSoup(content, 'html.parser').find_all()) else content for content in contents]

    analyses = []

    for index, text in enumerate(plain_texts):
        analysis = {
            "Subject": subjects[index],	
            "content": text,
        }
        analyses.append(analysis)

    return analyses

result = process_json_with_sentiment_analysis()
# print("Open API Prompt Input")
# print(json.dumps(result, indent=2))
