import re, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from .models import ParentLink, ChildLink, GrandchildLink
from selenium.common.exceptions import WebDriverException

def format_url(url):
    if not re.match('https?://', url):
        return 'https://'+url

def link_to_previous_directory(url, href):
    return remove_last_directory(url)+remove_previous_directory_reference(href)

def remove_last_directory(url):
    return re.sub('^(\/?.*?\/)', '', url[::-1])[::-1]

def remove_previous_directory_reference(href):
    return re.sub('^(..)', '', href)

def is_href_valid(href):
    return href.startswith(('http', '../', '/'))

def concat_url_with_href(url, href):
     return re.sub('//', '/', (url+href)[::-1], 1)[::-1]

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
        hrefs = list(filter(lambda href: is_href_valid(href), hrefs))

        for i, href in enumerate(hrefs):
            if href.startswith('/'):
                hrefs[i] = concat_url_with_href(url, href)
            if href.startswith('../'):
                hrefs[i] = link_to_previous_directory(url, href)

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
