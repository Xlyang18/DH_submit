import urllib.request
from bs4 import BeautifulSoup


def get_review_content(review_url):
    # 根据书评的URL获取完整书评内容
    response = urllib.request.urlopen(review_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    review_content = soup.find('div', class_='review-content').text.strip()
    return review_content


def scrape_book_reviews(book_url):
    # 爬取当前页面的书评人、书评标题、书评内容并保存到文件中
    response = urllib.request.urlopen(book_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    reviews = []
    review_list = soup.find_all('div', class_='review-item')
    for review in review_list:
        reviewer = review.find('a', class_='name').text.strip()
        review_title = review.find('h2').text.strip()
        review_url = review.find('a', class_='title')['href']
        full_review_content = get_review_content(review_url)

        reviews.append({
            'Reviewer': reviewer,
            'Review Title': review_title,
            'Review Content': full_review_content
        })

    # 将书评内容保存到文件
    with open('book_reviews.txt', 'w', encoding='utf-8') as file:
        for review in reviews:
            file.write(f"Reviewer: {review['Reviewer']}\n")
            file.write(f"Review Title: {review['Review Title']}\n")
            file.write(f"Review Content:\n{review['Review Content']}\n\n")


# 替换为你想要爬取书评的书籍页面链接
book_url_to_scrape = 'https://book.douban.com/subject/36626626/?icn=index-latestbook-subject'

scrape_book_reviews(book_url_to_scrape)
