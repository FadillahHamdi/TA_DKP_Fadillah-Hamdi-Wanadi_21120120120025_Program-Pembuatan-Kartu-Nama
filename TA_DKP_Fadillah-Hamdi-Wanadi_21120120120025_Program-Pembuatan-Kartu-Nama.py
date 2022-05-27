#Modul 8 (GUI)
#Modul 1 (variabel dan tipe data)
from tkinter import *  
from tkinter import messagebox 
from tkinter import ttk


def next () : #Function
        if not stringnama.get () :
                msgn1 = messagebox.showerror(title="Error", message="Semua identitas Harap Diisi")  
        elif stringnama.get () == " "  :
                msgn2 = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif not stringalamat.get () :
                msga1 = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif stringalamat.get () == " "  :
                msga2 = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")  
        elif not stringcontact.get () :
                msgk = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif stringcontact.get () == " "  :
                msgk = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif strpekerjaan.get () == 0 :
                msgp = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")  
        elif radio.get () == 0 :
                msgr = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif not hari.get ()  :
                msgr = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif not bulan.get () :
                msgr = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        elif not tahun.get () :
                msgr = messagebox.showerror(title="Error",message="Semua identitas Harap Diisi")
        else :
                global nw
                nw = Frame (root, bg='black', width=750, height=400)
                nw.pack ()
                Label(nw, image=foto).place(x=-70, y=-100)
                root.geometry("750x400")
                root.title("Hasil")
                #input
                nama = stringnama.get () #Modul 6 (Getter)
                alamat = stringalamat.get ()
                lblk = Label(nw, text="Alamat  : "+ alamat, fg='Black', font=("times", "18", "bold")).place(x=70, y=160)
                kontak = stringcontact.get ()
                lblk = Label(nw, text="Kontak  : "+ kontak, fg='Black', font=("times", "18", "bold")).place(x=70, y=220)
                #jk 
                gender = " " 
                if radio.get () == 1 : #Modul 2 (IF ELSE)
                        gender = "Mr. "
                else :
                        gender = "Mrs. "
                lbljk=Label(nw, text="Nama     : " + gender+nama, fg='Black', font=("times", "18", "bold")).place(x=70, y=100)
                #Job
                job = strpekerjaan.get ()
                lblj = Label (nw, text="Profesi   : "+ job, fg='Black', font=("times", "18", "bold")).place(x=70, y=190)
                quit1 = Button(nw, text="Cetak", command=cetak, width=10, bg="red", fg="white", font=("times", "14", "bold")).place(x=200, y=340)
                re = Button (nw, text="Buat Ulang", command= redo, width=10, bg="red", fg="white", font=("times", "14", "bold")).place(x=400, y=340)
                lblb1= Label(root, text=" Name Card ", bg="Black", width=100, fg="white", font=("times", "20", "bold")).place(x=-180, y=0)
                te=Label(root, text=" ", bg="Black", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=290)
                #ttl
                lablttl = Label(nw, text="TTL       : " + hari.get()+" / "+bulan.get ()+" / "+tahun.get (), fg='Black', font=("times", "18", "bold")).place(x=70, y=130)
def cetak () :
    ctk = ["Pencetakan Kartu Akan Diproses"]     
    for x in ctk :#Modul 3 (Perulangan For)
            msg = messagebox.showinfo(title="Selesai", message="".join(ctk))
            x =+ 1
            break
def snk () :
    syarat = ["1. Semua data harus diisi\n", "2. Mohon data diisi dengan benar\n", "3. Semua data yang dicantumkan harus bisa \t dipertanggung jawabkan\n", 
                "4. Harap gunakan kontak yang dapat dihubungi"]     
    for x in syarat :#Modul 3 (Perulangan For)
            msg = messagebox.showinfo(title="SnK", message="".join(syarat))
            x =+ 1
            break
def redo () :
    nw.destroy ()
    root.geometry("750x400")
    root.title(" Program Pembuatan Kartu Nama")



root = Tk ()
root.geometry("750x400")
root.title(" Program Pembuatan Kartu Nama")
foto=PhotoImage(file="D:\Prak DKP\TA\BG Batik.png")
foto1=Label(root, image=foto, bg="black").place(x=-70, y=-100)
root['bg'] = "black"




#Modul 5 (Class) 
class hal1 :
        #Modul 4 (Method)
        def __init__(self) : 
                self.tulisan = self.label ()
                self.masukan = self.input ()
                self.tombol = self.button ()
                self.jk = self.radio ()
                self.cb = self.combo ()
        #Function
        
        def button (self) :     
                #Button
                slsi = Button(root, text="Submit", command=next, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=260, y=340)
                quit = Button(root, text="Quit", command=root.destroy, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=500, y=340)
                btnsnk = Button(root, text="Syarat dan Ketentuan", command=snk, width=20, bg="red", fg="white", font=("times", "14", "bold")).place(x=20, y=340) 
        def label (self) :
                #Label
                lblb1= Label(root, text=" Name Card ", bg="Black", width=100, fg="white", font=("times", "20", "bold")).place(x=-180, y=0)
                nama = Label(root, text="Masukkan Nama Anda : ", bg="Brown", fg="white",).place(x= 10, y= 50)
                alamat = Label(root, text="Masukkan Alamat Anda : ", bg="Brown", fg="white",).place(x= 10, y= 80)
                umur = Label(root, text="Masukkan Tanggal Lahir Anda : ", bg="Brown", fg="white").place(x= 10, y= 105)
                gender = Label(root, text="Pilih Jenis Kelamin : ", bg="Brown", fg="white").place(x= 10, y= 130)
                pekerjaan = Label(root, text="Masukkan Profesi Anda : ", bg="Brown", fg="white").place(x= 10, y= 205)
                contact = Label(root, text="Masukkan Kontak yang dapat dihubungi : ", bg="Brown", fg="white").place(x= 10, y= 260)
                te=Label(root, text=" ", bg="Black", width=100, fg="white", font=("times", "20", "bold")).place(x=0, y=290)
                
                
        def input (self) :
                #Entry
                global stringnama
                global stringalamat 
                global stringcontact
                stringnama = StringVar ()
                stringalamat = StringVar ()
                stringcontact = StringVar ()
                innama = Entry (root, width=40, textvariable=stringnama).place(x= 150, y= 50)
                inalamat = Entry (root, width=40, textvariable=stringalamat).place(x= 160, y= 80)
                incontact = Entry (root, width=40, textvariable=stringcontact).place(x= 250, y= 260)
        def radio (self) :
                #Radio
                global radio 
                radio = IntVar()
                R1 = Radiobutton(root, text="Laki-Laki     ", variable=radio, value=1, bg="White", fg="black").place(x=10, y=155)  
                R2 = Radiobutton(root, text="Perempuan", variable=radio, value=2, bg="White", fg="black").place(x=10, y=175)  
        def combo (self) :
                #Combobox pekerjaan
                global strpekerjaan
                strpekerjaan = StringVar(value='Pilih Pekerjaan Anda') 
                Cb1 = ttk.Combobox(root, width = 20, textvariable = strpekerjaan, state="readonly")
                Cb1.place(x=10, y=230
                )
                Cb1['values']=('PNS', 
                                'SWASTA', 
                                'BUMN', 
                                'DOKTER', 
                                'PILOT', 
                                'TNI', 
                                'POLRI',
                                'PELAJAR/MAHASISWA')
                #Combobox TTL
                global hari
                global bulan
                global tahun
                ttld = IntVar(value="Tanggal")
                ttlm = StringVar(value="Bulan")
                ttly = StringVar(value="Tahun")
                hari = ttk.Combobox (root, width = 10, textvariable = ttld, state="readonly")
                hari.place(x=190, y=105)
                garing = Label (root, text="   /", bg="black", fg='white').place(x=270, y=105)
                bulan = ttk.Combobox (root, width = 10, textvariable = ttlm, state="readonly")
                bulan.place(x=300, y=105)
                garing2 = Label(root, text="  /", bg="black", fg='white').place (x=380, y=105)
                tahun = ttk.Combobox (root, width = 10, textvariable = ttly, state="readonly")
                tahun.place(x=400, y=105)
                hari ['values'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                bulan ['values'] = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
                tahun ['values']  =[1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

page = hal1 ()
root.mainloop()