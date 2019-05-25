from tkinter import *
from threading import Thread
from bs4 import BeautifulSoup
from urllib.request import urlopen



class Win():
    def __init__(self):

        self.win = Tk()
        self.win.configure(background="purple")
        self.win.geometry("400x500")
        self.win.title("ENG-TUR Translater v0.1 CagriAtalar")
        self.buton = Button(text="Translate",command=self.searchTureng,fg = "yellow",bg="black")
        self.buton.place(relx=0.15,rely=0.05)
        self.text1 = Entry(font="Bold 20",fg="red",bg="black")
        self.text1.place(relx=0.15,rely=0.15)
        self.text2 = Text(width=20,height=10,font="Bold 17",fg="green",bg="black")
        self.text2.tag_config('warning', background="yellow", foreground="red",font="Bold 24")
        self.text2.place(relx=0.15,rely=0.25)

    def ok(self):
        self.win.mainloop()

    def searchTureng(self):
        def _searchTureng():
            word = self.text1.get()
            url="http://www.tureng.com/search/"+word
            try:
                answer = urlopen(url)
            except:
                self.text2.insert(END,"No connection\n","warning")
            html = answer.read()
            soup = BeautifulSoup(html, "lxml")
            trlated=''
            try:
                table = soup.find('table')
                td = table.findAll('td', attrs={'lang':'tr'})
                for val in td[0:5]:
                    trlated = trlated + val.text + '\n'
                self.text2.insert(END,trlated)
            except:
                self.text2.insert(END, "Not Found !\n","warning")
        self.text2.delete(1.0,END)
        Thread(target=_searchTureng,args=()).start()
        

Win1 = Win()
Win1.ok()
