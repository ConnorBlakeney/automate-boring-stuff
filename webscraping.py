from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://otbdiscs.com/product/jawbreaker-og-glo-buzzz/')
elem = browser.find_element_by_css_selector('#product-529927 > div.summary.entry-summary > p > span > bdi')