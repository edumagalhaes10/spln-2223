import newspaper
import os

path = os.getcwd()

if not os.path.exists('/tmp/.newspaper_scraper/'):
    origin = os.path.join(path, 'newspaper_scraper')
    os.symlink(origin, '/tmp/.newspaper_scraper/')

url = "https://www.dn.pt/"
# url = "https://www.ojogo.pt/"

jn = newspaper.build(url)

print(f'Number of articles found = {jn.size()}')

for article in jn.articles:
    # print(f'URL: {article.url}\nTITLE: {article.title}\n****************************')
    ar = newspaper.Article(article.url)
    ar.download()
    ar.parse()
    print(f'''{ar.title}
    {ar.text}

    ''')