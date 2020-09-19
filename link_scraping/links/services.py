from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
from .models import ParentLink, ChildLink, GrandchildLink

def find_and_save_links(ParentLink):
    parent_link = ParentLink
    option = Options()
    option.headless = False
    browser = webdriver.Firefox(options=option)

    def find_links(url, is_browser_init):
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        links = {link['href'] for link in soup.select('a[href]')}
        links = list(filter(lambda link: "#" not in link, links))

        for i, link in enumerate(links):
            if link.startswith('/'):
                links[i] = url+link

        return links


    def save_child_links(ParentLink):
        for link in find_links(ParentLink.url, True):
            child_link = ChildLink.objects.create(id=None, parent_link=ParentLink, url=link)
            child_link.save()
            print('\n\n')
            for link in find_links(child_link.url, False):
                grandchild_link = GrandchildLink.objects.create(id=None, parent_link=child_link, url=link)
                grandchild_link.save()
        browser.quit()

    save_child_links(parent_link)
