from selenium import webdriver     # webdriver to control the browser
import time
from bs4 import BeautifulSoup      # to parse the page source got from selenium 
import pandas as pd                # to store scraped details as csv file
from selenium.webdriver.chrome.options import Options    # 

record=[]                           # empty list to store details temporarily

print("ENTER THE FILENAME TO STORE LINKS")   # filename to store details 
file_name=str(input())
file=open(file_name+".txt","a")
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alpha\\AppData\\Local\\Google\\Chrome\\User Data\\selenium") # it create chrome user named selenium
bro = webdriver.Chrome(chrome_options=options)

print("NAVIGATE TO THE PAGE IN THE BROWSER FROM WHERE DETAILS NEED TO BE SCRAPED \n PRESS ENTER TO SCRAP THE PAGES ") # Navigate to the page from where to scrape
number=input()             # press any key to start scraping
bro.switch_to_window(bro.window_handles[1])
ss=bro.page_source          # page source from selenium
soup=BeautifulSoup(ss,'html.parser')       # html parser from bs4
members=soup.findAll("tr",{"class":"row"})
length=len(members)
flag=True
i=1
while(flag):
    try:
        ll=members[i].findAll("td")   # all the tags mentioned here are based on the need of the details to be scraped
        lll=ll[1].find("div")
        name=lll.text
        print(name)
        lf=members[i].find("div",{"class":"email-wrap has-tooltip"})
        email=lf.text
        print(email)
    except:
        email="null"
        pass
    
    i+=1
    record.append((name,email))  # adding data to the temporary storage
    df=pd.DataFrame(record,columns=['name','email'])         
    df.to_csv(file_name + '.csv',index=False,encoding='utf-8')  # writing scraped details to the file
 
	
    if(i>length):
        flag=False

	
