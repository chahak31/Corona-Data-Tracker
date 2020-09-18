import requests
from bs4 import BeautifulSoup 
import plyer
import tkinter as tk
import time
import datetime
import threading

#returns html data from the website
def get_html_data(url):
    data = requests.get(url)
    return data

#calculates details of corona in India from the website
def get_corona_detail_of_india():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    #print(html_data.text)

    #Using beautifulSoup to beautify the text
    #object of BeautifulSoup
    bs = BeautifulSoup(html_data.text, 'html.parser')
    #print(bs.prettify())

    info = bs.find("div",class_="content-inner").find_all(id="maincounter-wrap")
    #print(info)

    all_details = ""
    for block in info:
        text = block.get_text()
        all_details = all_details + text
    return all_details

#function use to reload data from the website
def refresh():
    newdata=get_corona_detail_of_india()
    print("Refreshing")
    mainLabel['text']=newdata

#function for notifying
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of world",
            message=get_corona_detail_of_india(),
            timeout=10,
            #app_icon='icon.ico'
            )
        time.sleep(30)

print(get_corona_detail_of_india())

#Creating gui:
root = tk.Tk()
#window's length & width
root.geometry("600x600")
#root.iconbitmap("")
root.title("CORONA DATA TRACKER")
root.configure(bg="white")

#font
f=("poppins",15,"bold")

banner=tk.PhotoImage(file="G:\JADON\Python Projects\Web Scraping\corona.gif")
bannerLabel = tk.Label(root,image=banner)
bannerLabel.pack()

mainLabel = tk.Label(root,text=get_corona_detail_of_india(),font=f,bg="white")
mainLabel.pack()

reBtn = tk.Button(root,text="REFRESH",font=f,relief="solid",command=refresh)
reBtn.pack()

#create a new thread
th1=threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()
