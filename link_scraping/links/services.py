import re, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from .models import ParentLink, ChildLink, GrandchildLink
from selenium.common.exceptions import WebDriverException

def find_and_save_links(parent_link = ParentLink):
    option = Options()
    option.headless = True
    capabilities = {'browserName': 'firefox'}
    try:
        browser = webdriver.Remote(desired_capabilities=capabilities, command_executor='http://selenium:4444/wd/hub')
    except:
        browser = webdriver.Firefox(options=option)

    def find_urls(url):
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        hrefs = {href['href'] for href in soup.select('a[href]')}
        hrefs = list(filter(lambda href: href.startswith(('http', '../', '/')), hrefs))

        for i, href in enumerate(hrefs):
            if href.startswith('/'):
                hrefs[i] = re.sub('//', '/', (url+href)[::-1], 1)[::-1]
            if href.startswith('../'):
                hrefs[i] = re.sub('\/?.*?\/', '', url[::-1])[::-1]+re.sub('^(..)', '', href)

        return hrefs

    def save_child_links(parent_link):
        parent_link.save()
        for child_url in find_urls(parent_link.url):
            child_link = ChildLink.objects.create(id=None, parent_link=parent_link, url=child_url)
            for grandchild_url in find_urls(child_link.url):
                GrandchildLink.objects.create(id=None, child_link=child_link, url=grandchild_url)
        browser.quit()

    try:
        save_child_links(parent_link)
    except:
        browser.quit()
