import praw
from psaw import PushshiftAPI
import datetime
from collections import Counter

# praw initialization
user_agent = "Web Scraper by /u/Bodanski"
reddit = praw.Reddit(client_id="nfp3OV0TrUwhaDmtFiCCtQ",
                     client_secret="joHsh0Oep5bzcS8U5Rb_WXMmdMNlAA",
                     user_agent=user_agent)

# psaw initialization
api = PushshiftAPI()

# nltk_stopwords list consists of Natural Language Toolkit stopwords
nltk_stopwords = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
                  "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such",
                  "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him",
                  "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don",
                  "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while",
                  "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
                  "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because",
                  "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has",
                  "just",
                  "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if",
                  "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]

# my_stopwords list consists of stopwords I've manually added in through testing
my_stopwords = ["ELI5", "ELI5:", "how", "why", "what", "How", "Why", "What", ":", "Eli5:", "And", "eli5:", "get",
                "make", "like", "work"]

weekly_top_list = []


# Returns most common keywords in the titles of the past week's top 1000 posts on r/explainlikeimfive
for submission in reddit.subreddit("explainlikeimfive").top("week", limit=50):
    if not submission.stickied:
        split_submission = submission.title.split()
        for word in split_submission:
            if word not in nltk_stopwords:
                if word not in my_stopwords:
                    weekly_top_list.append(word)
Counter = Counter(weekly_top_list)
print(Counter.most_common(10))


# Returns total amount of times user-inputted keyword has been in a title on r/explainlikeimfive, since start_time
start_time = int(datetime.datetime(2022, 2, 1).timestamp())
keyword = input("Keyword: ")

submissions = api.search_submissions(after=start_time,
                                     q=keyword,
                                     subreddit="explainlikeimfive",
                                     filter=["url", "author", "title", "subreddit"])
submission_count = 0

for submission in submissions:
    print(submission.title)
    submission_count = submission_count + 1
print(submission_count)
