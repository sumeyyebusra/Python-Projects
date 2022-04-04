from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import sort_algorithms

veri = []
root = Tk()
root.title("Sıralama Algoritması Görselleştirici")
root.maxsize(800,500)
root.config(bg="black")
secilen_algoritma = StringVar()

def grafik_olustur(veri):
    canvas.delete("all")
    canvas_height = 280
    canvas_width = 450
    x_width = canvas_width / (len(veri)+1)
    for i in range(len(veri)):
        x1 = i * x_width + 30
        y1 = canvas_height - veri[i]
        x2 = (i+1) * x_width + 10
        y2 = canvas_height
        canvas.create_rectangle(x1,y1,x2,y2,fill="purple")
        canvas.create_text(x1+2,y1,anchor=SW,text=str(veri[i]))
    root.update_idletasks()

def rastgele_olustur():
    global veri
    if min_deger.get() == "":
        min = 1
    else:
        min = int(min_deger.get())
    if max_deger.get() == "":
        max = 100
    else:
        max = int(max_deger.get())
    if boyut.get() == "":
        size = 10
    else:
        size = int(boyut.get())
    veri = []
    for i in range(size):
        veri.append(random.randrange(min,max+1))
    grafik_olustur(veri)

def baslat():
    global veri
    if veri == []:
        messagebox.showinfo(title="Dikkat", message="Lütfen önce rastgele verileri oluşturun.")
    if algoritma_menusu.get() == "Bubble Sort":
        sort_algorithms.bubble_sort(veri, grafik_olustur)
    elif algoritma_menusu.get() == "Selection Sort":
        sort_algorithms.selection_sort(veri, grafik_olustur)
    elif algoritma_menusu.get() == "Insertion Sort":
        sort_algorithms.insertion_sort(veri, grafik_olustur)
    elif algoritma_menusu.get() == "Quick Sort":
        sort_algorithms.quick_sort(veri,0,len(veri)-1,grafik_olustur)
        grafik_olustur(veri)
    elif algoritma_menusu.get() == "Merge Sort":
        sort_algorithms.merge_sort(veri,grafik_olustur)

frame = Frame(root,width=450,height=100,bg="grey")
frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root,width=450,height=280,bg="pink")
canvas.grid(row=1,column=0,padx=10,pady=5)

Label(frame,text="Algoritma Seçiniz: ",bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algoritma_menusu = ttk.Combobox(frame,textvariable=secilen_algoritma,values=["Bubble Sort","Merge Sort","Quick Sort","Selection Sort","Insertion Sort"])
algoritma_menusu.grid(row=0,column=1,padx=5,pady=5)
algoritma_menusu.current(0)

Button(text="Sıralamayı\nBaşlat",command=baslat,bg="purple").grid(row=1,column=1,padx=5,pady=5)
Button(text="Rastgele\nOluştur",command=rastgele_olustur,bg="purple").grid(row=0,column=1,padx=5,pady=5)

Label(frame,text="Dizi Boyutu", bg="purple").grid(row=1,column=0,padx=5,pady=5,sticky=W)
boyut =Entry(frame)
boyut.insert(0,"10")
boyut.grid(row=1,column=1,padx=5,pady=5,sticky=W)

Label(frame,text="Minimum\nDeğer", bg="purple").grid(row=1,column=2,padx=5,pady=5,sticky=W)
min_deger = Entry(frame)
min_deger.grid(row=1,column=3,padx=5,pady=5,sticky=W)

Label(frame,text="Maksimum\nDeğer", bg="purple").grid(row=1,column=4,padx=5,pady=5,sticky=W)
max_deger = Entry(frame)
max_deger.grid(row=1,column=5,padx=5,pady=5,sticky=W)

root.mainloop()

