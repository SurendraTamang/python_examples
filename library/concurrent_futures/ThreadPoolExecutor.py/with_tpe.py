from concurrent.futures import ThreadPoolExecutor
import requests
import time
def scrape_page(page_number):
    url = f'https://quotes.toscrape.com/page/{page_number}/'
    response = requests.get(url)
    return len(response.text)

if __name__ == '__main__':
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(scrape_page,range(1,10)))
    for result in results:
        print(result)
    end_time = time.time()
    print("Total time used", end_time - start_time)
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(scrape_page,range(20,40)))
    for result in results:
        print(result)

'''Results
---
y/concurrent_futures/ThreadPoolExecutor.py/with_tpe.py
11011
13689
9977
10273
9960
10364
10668
11335
10970
Total time used 1.071183204650879
'''
