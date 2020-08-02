from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list_of_words_link="https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"

path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get(list_of_words_link)

filer=open("words","w")
count=0
try:
    panel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wordlistsContentPanel"))
    )
    ul = panel.find_element_by_tag_name("ul")
    lis = ul.find_elements_by_tag_name("li")
    for li in lis:
        try:
            a=li.find_element_by_tag_name("a")
            text=a.text
            if(text!=""):
                filer.write(f"{text}\n")
        except:
            count+=1
finally:
    print(f"Error count:{count}")
    driver.quit()
    filer.close()