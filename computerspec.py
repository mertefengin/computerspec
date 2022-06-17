import tkinter
from tkinter import *
import platform
import psutil
import cpuinfo
import wmi
import nvidia_smi

master = tkinter.Tk()

canvas = Canvas(master, height=480, width=650)
canvas.pack()

frame_sol = Frame(master, bg= '#515151' )
frame_sol.place(relx=0.01, rely=0.01, relwidth=0.2, relheight=1)

frame_sağ = Frame(master, bg= '#515151' )
frame_sağ.place(relx=0.21, rely=0.01, relwidth=0.83, relheight=1)


bilgisayaradi = platform.node()
islemcitürü = platform.processor()
isletimsistemi = platform.system()
isletimsistemisürümü = platform.version()

def sistem():
    hide_all_frames()
    ozellik = tkinter.Label(frame_sağ)
    ozellik2 = tkinter.Label(frame_sağ)
    ozellik3 = tkinter.Label(frame_sağ)
    ozellik4 = tkinter.Label(frame_sağ)
    ozellik5 = tkinter.Label(frame_sağ)
    ozellik6 = tkinter.Label(frame_sağ)
    ozellik7 = tkinter.Label(frame_sağ)
    ozellik8 = tkinter.Label(frame_sağ)
    ozellik.config(text="Bilgisayar Adı =", font="Calibri 13 ", bg="#515151" , fg="#92B3C2" ), \
    ozellik2.config(text=bilgisayaradi, font="Helvetica 11 bold ", bg="#515151" ,fg="white")
    ozellik3.config(text="İşlemci Türü =", font="Helvetica 11 bold"), \
    ozellik4.config(text=islemcitürü, font="Helvetica 8 bold", bg="grey")
    ozellik5.config(text="İşletim Sistemi =", font="Helvetica 11 bold"), \
    ozellik6.config(text=isletimsistemi, font="Helvetica 12 bold", bg="grey")
    ozellik7.config(text="Sistem Sürümü =", font="Helvetica 11 bold"), \
    ozellik8.config(text=isletimsistemisürümü, font="Helvetica 12 bold", bg="grey")
    ozellik.place(relx=0.08, rely=0.09)
    ozellik2.place(relx=0.41, rely=0.09)
    ozellik3.place(relx=0.096, rely=0.23)
    ozellik4.place(relx=0.37, rely=0.235)
    ozellik5.place(relx=0.05, rely=0.37)
    ozellik6.place(relx=0.42, rely=0.37)
    ozellik7.place(relx=0.043, rely=0.5)
    ozellik8.place(relx=0.42, rely=0.5)

sistemozellikleri_butonu = Button(frame_sol, text="Sistem Özellikleri", command=sistem , font="Helvetica 10 bold")
sistemozellikleri_butonu.pack()





islemcibilgi = cpuinfo.get_cpu_info()['brand_raw']
islemcifizikselcekirdeksayisi = psutil.cpu_count(logical=False)
islemcimantıksalcekirdeksayisi = psutil.cpu_count(logical=True)
mevcutislemcifrekansi = psutil.cpu_freq().current
minimumislemcifrekansi = psutil.cpu_freq().min
maksimumislemcifrekansi = psutil.cpu_freq().max

def cpu():
    hide_all_frames()
    ozellik = tkinter.Label(frame_sağ)
    ozellik2 = tkinter.Label(frame_sağ)
    ozellik3 = tkinter.Label(frame_sağ)
    ozellik4 = tkinter.Label(frame_sağ)
    ozellik5 = tkinter.Label(frame_sağ)
    ozellik6 = tkinter.Label(frame_sağ)
    ozellik7 = tkinter.Label(frame_sağ)
    ozellik8 = tkinter.Label(frame_sağ)
    ozellik9 = tkinter.Label(frame_sağ)
    ozellik10 = tkinter.Label(frame_sağ)
    ozellik11 = tkinter.Label(frame_sağ)
    ozellik12 = tkinter.Label(frame_sağ)
    ozellik.config(text="İşlemci =",font="Helvetica 11 bold"), \
    ozellik2.config(text=islemcibilgi,font="Helvetica 8",bg="red")
    ozellik3.config(text="Fiziksel Çekirdek Sayısı =",font="Helvetica 10 bold"),\
    ozellik4.config(text=islemcifizikselcekirdeksayisi, font="Helvetica 14",bg="red")
    ozellik5.config(text="Mantıksal Çekirdek Sayısı =", font="Helvetica 10 bold"),\
    ozellik6.config(text=islemcimantıksalcekirdeksayisi, font="Helvetica 14",bg="red")
    ozellik7.config(text="Mevcut Frekans =", font="Helvetica 11 bold"),\
    ozellik8.config(text=mevcutislemcifrekansi, font="Helvetica 14",bg="red")
    ozellik9.config(text="Minimum Frekans =", font="Helvetica 11 bold"),\
    ozellik10.config(text=minimumislemcifrekansi,font="Helvetica 14",bg="red")
    ozellik11.config(text="Maksimum Frekans =", font="Helvetica 11 bold"),\
    ozellik12.config(text=maksimumislemcifrekansi, font="Helvetica 14",bg="red")
    ozellik.place(relx=0.26, rely=0.13)
    ozellik2.place(relx=0.45, rely=0.135)
    ozellik3.place(relx=0.04, rely=0.25)
    ozellik4.place(relx=0.5, rely=0.245)
    ozellik5.place(relx=0.01, rely=0.38)
    ozellik6.place(relx=0.5, rely=0.374)
    ozellik7.place(relx=0.114, rely=0.5)
    ozellik8.place(relx=0.49, rely=0.496)
    ozellik9.place(relx=0.08, rely=0.63)
    ozellik10.place(relx=0.493, rely=0.625)
    ozellik11.place(relx=0.045, rely=0.76)
    ozellik12.place(relx=0.485, rely=0.755)



cpuozellikleri_butonu = Button(frame_sol, text="CPU Özellikleri", command=cpu , font="Helvetica 10 bold")
cpuozellikleri_butonu.pack()


toplamram = round(psutil.virtual_memory().total/1000000000, 2)
kullanılmayanram = round(psutil.virtual_memory().available/1000000000, 2)
kullanılanram = round(psutil.virtual_memory().used/1000000000, 2)
ramkullanımı = psutil.virtual_memory().percent

def hide_all_frames():
    for widget in frame_sağ.winfo_children():
        widget.destroy()
    frame_sağ.pack_forget()



def ram():
    hide_all_frames()
    ozellik = tkinter.Label(frame_sağ)
    ozellik2 = tkinter.Label(frame_sağ)
    ozellik3 = tkinter.Label(frame_sağ)
    ozellik4 = tkinter.Label(frame_sağ)
    ozellik5 = tkinter.Label(frame_sağ)
    ozellik6 = tkinter.Label(frame_sağ)
    ozellik7 = tkinter.Label(frame_sağ)
    ozellik8 = tkinter.Label(frame_sağ)
    ozellik.config(text="Toplam RAM =", font="Helvetica 11 bold"), \
    ozellik2.config(text=toplamram, font="Helvetica 14", bg="red")
    ozellik3.config(text="Kullanılmayan RAM =", font="Helvetica 11 bold"), \
    ozellik4.config(text=kullanılmayanram, font="Helvetica 14", bg="red")
    ozellik5.config(text="Kullanılan RAM =", font="Helvetica 11 bold"), \
    ozellik6.config(text=kullanılanram, font="Helvetica 14", bg="red")
    ozellik7.config(text="RAM Kullanımı (%) =", font="Helvetica 11 bold"), \
    ozellik8.config(text=ramkullanımı, font="Helvetica 14", bg="red")
    ozellik.place(relx=0.148, rely=0.06)
    ozellik2.place(relx=0.47, rely=0.056)
    ozellik3.place(relx=0.033, rely=0.18)
    ozellik4.place(relx=0.47, rely=0.177)
    ozellik5.place(relx=0.107, rely=0.3)
    ozellik6.place(relx=0.47, rely=0.298)
    ozellik7.place(relx=0.03, rely=0.43)
    ozellik8.place(relx=0.47, rely=0.428)


ramozellikleri_butonu = Button(frame_sol, text="RAM Özellikleri", command=ram , font="Helvetica 10 bold")
ramozellikleri_butonu.pack()

computer = wmi.WMI()

dahili = computer.Win32_VideoController()[0]
dahiliekrankartı = '{0}'.format(dahili.Name)
harici = computer.Win32_VideoController()[1]
hariciekrankartı = '{0}'.format(harici.Name)

nvidia_smi.nvmlInit()
handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
info = nvidia_smi.nvmlDeviceGetMemoryInfo(handle)
fizikselbellek = round(info.total/1000000),"MB"
bosbellek = round(info.free/1000000),"MB"
kullanılanbellek = round(info.used/1000000),"MB"


def gpu():
    hide_all_frames()
    ozellik = tkinter.Label(frame_sağ)
    ozellik2 = tkinter.Label(frame_sağ)
    ozellik3 = tkinter.Label(frame_sağ)
    ozellik4 = tkinter.Label(frame_sağ)
    ozellik5 = tkinter.Label(frame_sağ)
    ozellik6 = tkinter.Label(frame_sağ)
    ozellik7 = tkinter.Label(frame_sağ)
    ozellik8 = tkinter.Label(frame_sağ)
    ozellik9 = tkinter.Label(frame_sağ)
    ozellik10 = tkinter.Label(frame_sağ)
    ozellik.config(text="Dahili Ekran Kartı =", font="Helvetica 12 bold"), \
    ozellik2.config(text=dahiliekrankartı, font="Helvetica 13", bg="red")
    ozellik3.config(text="Harici Ekran Kartı =", font="Helvetica 12 bold"), \
    ozellik4.config(text=hariciekrankartı, font="Helvetica 13", bg="red")
    ozellik5.config(text="Fiziksel Bellek =", font="Helvetica 12 bold"), \
    ozellik6.config(text=fizikselbellek, font="Helvetica 13", bg="red")
    ozellik7.config(text="Boş Bellek =", font="Helvetica 12 bold"), \
    ozellik8.config(text=bosbellek, font="Helvetica 13", bg="red")
    ozellik9.config(text="Kullanılan Bellek =", font="Helvetica 12 bold"), \
    ozellik10.config(text=kullanılanbellek, font="Helvetica 13", bg="red")
    ozellik.place(relx=0.01, rely=0.03)
    ozellik2.place(relx=0.4,rely=0.027)
    ozellik3.place(relx=0.01,rely=0.15)
    ozellik4.place(relx=0.4,rely=0.148)
    ozellik5.place(relx=0.08, rely=0.27)
    ozellik6.place(relx=0.4, rely=0.27)
    ozellik7.place(relx=0.14, rely=0.39)
    ozellik8.place(relx=0.4, rely=0.39)
    ozellik9.place(relx=0.035, rely=0.51)
    ozellik10.place(relx=0.4, rely=0.51)

gpuozellikleri_butonu = Button(frame_sol, text="GPU Özellikleri", command=gpu , font="Helvetica 10 bold")
gpuozellikleri_butonu.pack()

master.mainloop()
