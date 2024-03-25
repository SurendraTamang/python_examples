from concurrent.futures import ThreadPoolExecutor
import requests
import time
def scrape_page(page_number):
    url = f'https://quotes.toscrape.com/page/{page_number}/'
    response = requests.get(url)
    return len(response.text)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(1,10):
        print(scrape_page(i))
    end_time = time.time()
    print("Total time used", end_time - start_time)

'''Results
---
11011
13689
9977
10273
9960
10364
10668
11335
10970
Total time used 7.911605358123779
'''

    
