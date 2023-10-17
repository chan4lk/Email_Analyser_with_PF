import nltk
import json
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.tokenize import RegexpTokenizer
from promptflow import tool

# Load the data from a file
with open("data.json", "r") as input_file:
    data = json.load(input_file)

@tool
def generate_email_summary():
    email_bodies = [item.get("body", "") for item in data if isinstance(item, dict)]
    combined_text = " ".join(email_bodies)

    sentences = sent_tokenize(combined_text)

    tokenizer = RegexpTokenizer(r"\w+")
    words = [
        word.lower() for sentence in sentences for word in tokenizer.tokenize(sentence)
    ]

    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]

    word_freq = FreqDist(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        for word in tokenizer.tokenize(sentence):
            if word.lower() in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_freq[word.lower()]
                else:
                    sentence_scores[sentence] += word_freq[word.lower()]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
        :5
    ]

    summary = TreebankWordDetokenizer().detokenize(summary_sentences)

    return summary

def chat_bot(input_text):
    if "how is my emails today" in input_text.lower():
        summary = generate_email_summary()
        return summary
    else:
        return "I'm sorry, I cannot provide information on that topic"

input_text = "How is my emails today?"
response = chat_bot(input_text)
print(response)
