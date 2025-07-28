import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']


def read_url(url):
    with urllib.request.urlopen(url, timeout=60) as conn:
        return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    future_url = {executor.submit(read_url, url):url for url in URLS}
    for future in concurrent.futures.as_completed(future_url):
        url = future_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(exc)
        else:
            print(f"Page in bytes {len(data)}")