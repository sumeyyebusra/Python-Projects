from tkinter import *
from tkinterhtml import HtmlFrame
import urllib.request as urllib2
from bs4 import BeautifulSoup
import re

class editor(Frame): #Class'ın init fonksiyonunu yazıp arkaplanını ve başlığını belirledik.
    def __init__(self,parent):
        Frame.__init__(self,parent,bg='grey')
        self.parent = parent
        self.parent.title("Ürün Arama")
        self.initUI()

    def initUI(self):
        #Text, Label, Entry, Button, Listbox, Radiobotton ve Scrollbar widgetlerını oluşturup yerleştirdik.
        self.grid(columnspan= TRUE,rowspan=TRUE)
        self.label = Label(self,text="Enter The Product Name",bg="pink")
        self.label.grid(row=0,column=0,ipadx=10,padx=10,sticky=W)
        self.var = StringVar()
        self.entry = Entry(self, textvariable=self.var, width=5)
        self.entry.grid(row=0, column=0,ipadx=105,sticky=W,padx=180)
        self.ara_butonu = Button(self, text="Search", bg="white", command=self.ara)
        self.ara_butonu.grid(row=0, column=0, ipadx=20,pady=10)
        self.label2 = Label(self, text="Min", bg="pink")
        self.label2.grid(row=0, column=0,sticky=W,padx=480, ipadx=10,pady=10)
        self.var2 = IntVar()
        self.entry2 = Entry(self, textvariable=self.var2, width=5)
        self.entry2.grid(row=0, column=0,sticky=W,padx=540, ipadx=10,pady=10)
        self.label3 = Label(self, text="Max", bg="pink")
        self.label3.grid(row=0, column=0,sticky=W,padx=650, ipadx=10,pady=10)
        self.var3 = IntVar()
        self.entry3 = Entry(self, textvariable=self.var3, width=5)
        self.entry3.grid(row=0, column=0,sticky=W,padx=710, ipadx=10,pady=10)
        self.label4 = Label(self, text="Items:", bg="pink")
        self.label4.grid(row=1,column=0,ipadx=10,padx=10,sticky=W)
        self.label5 = Label(self, text="Description:", bg="pink")
        self.label5.grid(row=1,column=0,ipadx=10,padx=480,sticky=W)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=4, column=0,pady=10,ipady=282,sticky=W,padx=435)
        self.listbox = Listbox(self, width=70, height=38, yscrollcommand=self.scrollbar)
        self.listbox.bind("<<ListboxSelect>>", self.onSelect) #Listbox'ta seçim yapıldığında bir fonksiyona bağlanmasını sağladık.
        self.listbox.grid(row=4,column=0,sticky=W,padx=10)
        self.html = HtmlFrame(self,horizontal_scrollbar="auto")
        self.html.grid(row=4,column=0,padx=480)

    def ara(self): #Ürün ismi girildiğinde gerekli linkin oluşturulup listbox'a yazılmasını sağlayan fonksiyon
        sozluk = dict()
        self.listbox.delete(0,END)
        link = 'http://www.n11.com/arama?q='
        arama = self.var.get().split()
        s = '+'.join(arama)
        link += s
        if self.var2.get() == 0:
            pass
        else:
            min= str(self.var2.get())
            link += '&minp=' + min
        if self.var3.get() == 0:
            pass
        else:
            max= str(self.var3.get())
            link += '&maxp=' + max
        for i in range (1,5):
            link += '&pg=' + str(i)
            c = urllib2.urlopen(link)
            soup = BeautifulSoup(c.read(), "html.parser")
            veri = soup.find_all("div", {"class": "proDetail"}) #Yarattığımız linkten dönen soup nesnesini işleyerek başlık ve fiyat bilgisini çektik ve girilen min ve max değerlerine uyuyorsa listbox'a yerleştirdik.
            for i in veri:
                fiyat = re.compile(r'<[^>]+>').sub('', str(i.find('ins'))).split('\n')[0] #Html etiketlerinin atılıp ürünün fiyat kısmının çekilmesini sağladık.
                fiyat = fiyat.split(',')[0]
                title = i.find('a')['title']
                urun_linki = i.find("a")['href']
                for krktr in fiyat:
                    if krktr == '.':
                        fiyat = fiyat.replace('.','') #Fiyatlardaki "." karakterini kaldırıp ondalık tabanda yazılmasını sağladık.
                insert = title + ' ' + fiyat + 'TL'
                self.listbox.insert(ACTIVE,insert)
                sozluk[insert] = urun_linki
        return sozluk

    def onSelect(self, val): #Listbox'ta seçim yapıldığında HtmlFrame'e ayrıntılar kısmının gelmesini sağlayan fonksiyon
        widget = val.widget
        idx = widget.curselection()
        value = widget.get(idx)
        sozluk = self.ara()
        for key in sozluk:
            if value == key:
                link = sozluk[key]
        c1 = urllib2.urlopen(link)
        soup1 = BeautifulSoup(c1.read(), "html.parser") #Yarattığımız linkten dönen soup nesnesini işleyip ayrıntılar kısmını çektik ve HtmlFrame'e yazdırdık.
        veri = soup1.find_all("section", {"class": "tabPanelItem details"})
        self.html.set_content(veri)

def main():
    root = Tk()
    root.geometry("1500x700+15+15")
    app = editor(root)
    root.mainloop()

if __name__ == "__main__":
    main()