import feedparser
url = 'https://bitsrfr.com/rss/'

feed = feedparser.parse(url)

entries = feed.entries

for entry in entries:
    print(entry.title)
    print(entry.published)