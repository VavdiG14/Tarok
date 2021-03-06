__author__ = 'Gregor'
import tkinter as tk
from tkinter import messagebox


igre = {'Tri': 10, 'Dva': 20, 'Ena': 30, 'SoloTri': 40, 'SoloDva': 50, 'SoloEna': 60, 'Berač': 70, 'SoloBrez': 80, 'BarvniValat': 125,
        'Valat': 250}

dodatneigre_nenapovedane = {'Kralji': 10, 'Trula': 10, 'ZadnjiKralj': 10, 'pagatUltimo': 25}

dodatneIgre_napovedane = {'Kralji': 20, 'Trula': 20, 'ZadnjiKralj': 20, 'pagatUltimo': 50}

class GUI():

    def __init__(self, master):
        self.master = master
        menu = tk.Menu(master)
        master.config(menu=menu)
        self.master.resizable(width=False, height=False)
        self.številkaIgre = 1
        self.igralec1 = 0
        self.igralec2 = 0
        self.igralec3 = 0
        self.igralec4 = 0
        self.radelc1 = 0
        self.radelc2 = 0
        self.radelc3 = 0
        self.radelc4 = 0
        self.igralci = [ self.igralec1, self.igralec2, self.igralec3, self.igralec4]
        self.radelci = [self.radelc1, self.radelc2, self.radelc3, self.radelc4]
        self.imena = []

        self.canvas1 = tk.Canvas(root, width=100, height=21, background='white')
        self.canvas1.grid(row=1, column=1)
        self.canvas3 = tk.Canvas(root, width=100, height=21, background='white')
        self.canvas3.grid(row=1, column=3)
        self.canvas5 = tk.Canvas(root, width=100, height=21, background='white')
        self.canvas5.grid(row=1, column=5)
        self.canvas7 = tk.Canvas(root, width=100, height=21, background='white')
        self.canvas7.grid(row=1, column=7)



        # Podmeni Igra
        menu_igra = tk.Menu(menu)
        menu.add_cascade(label="Igra", menu=menu_igra)
        menu_igra.add_command(label="Dodaj igralca", command=self.izbira_nove_igre)
        menu_igra.add_command(label="Izhod", command=master.destroy)


    def izbira_nove_igre(self):
        """Ustvari okno za izbiro nastavitev nove igre (če ne obstaja) ter začne novo igro, z izbranimi nastavitvami."""

        def izpisi():
            """Pomožna funkcija, ki ustvari novo igro, nastavi ime igralcev ter zapre okno za izbiro nastavitev."""
            tk.Label(root, text=ime_1.get(), font=('Helvetica', 14)).grid(row=0, column=1)
            tk.Label(root, text=ime_2.get(), font=('Helvetica', 14)).grid(row=0, column=3)
            tk.Label(root, text=ime_3.get(), font=('Helvetica', 14)).grid(row=0, column=5)
            tk.Label(root, text=ime_4.get(), font=('Helvetica', 14)).grid(row=0, column=7)
            tk.Button(root, text='Vnesi igro', command=self.igra).grid(row=0, column=20)
            self.imena = [ime_1.get(), ime_2.get(), ime_3.get(),ime_4.get()]
            new_game.destroy()

        # Ustvari novo okno za izbiro nastavitev nove igre.
        new_game = tk.Toplevel()
        new_game.grab_set()                                   # Postavi fokus na okno in ga obdrži
        new_game.title("Tarok - Nova igra")                # Naslov okna
        new_game.resizable(width=False, height=False)         # Velikosti okna ni mogoče spreminjati


        tk.Label(new_game, text="Nastavitve nove igre", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=4)
        # Nastavitve igralcev
        # ---------------------------------------------------------
        tk.Label(new_game, text="Ime igralca 1:").grid(row=5, column=0, sticky="E")
        tk.Label(new_game, text="Ime igralca 2:").grid(row=6, column=0, sticky="E")
        tk.Label(new_game, text="Ime igralca 3:").grid(row=7, column=0, sticky="E")
        tk.Label(new_game, text="Ime igralca 4:").grid(row=8, column=0, sticky="E")

        ime_1 = tk.Entry(new_game, font="Helvetica 12", width=10)  # Vnosno polje za ime prvega igralca
        ime_1.grid(row=5, column=1)
        ime_2 = tk.Entry(new_game, font="Helvetica 12", width=10)  # Vnosno polje za ime drugega igralca
        ime_2.grid(row=6, column=1)
        ime_3 = tk.Entry(new_game, font="Helvetica 12", width=10)  # Vnosno polje za ime tretjega igralca
        ime_3.grid(row=7, column=1)
        ime_4 = tk.Entry(new_game, font="Helvetica 12", width=10)  # Vnosno polje za ime četrega igralca
        ime_4.grid(row=8, column=1)
        # ---------------------------------------------------------

        # Gumba za začetek nove igre in preklic
        tk.Button(new_game, text="Prekliči", width=20, height=2,
                  command=lambda: new_game.destroy()).grid(row=20, column=0, columnspan=3, sticky="E")
        tk.Button(new_game, text="Začni igro", width=20, height=2,
                  command=lambda: izpisi()).grid(row=20, column=3, columnspan=3, sticky="E")



    def igra(self):

        izbira = tk.Toplevel()
        izbira.title("Tarok - Izpis igre")                # Naslov okna
        izbira.resizable(width=False, height=False)         # Velikosti okna ni mogoče spreminjati
        self.kdo = tk.IntVar()
        self.kaj = tk.IntVar()
        self.igralec = tk.IntVar()
        Nenapovedana1 = tk.IntVar()
        Nenapovedana2 = tk.IntVar()
        Nenapovedana3 = tk.IntVar()
        Nenapovedana4 = tk.IntVar()
        razlika = tk.IntVar()
        zmagal = tk.BooleanVar()
        self.skupaj1 = tk.IntVar()
        self.kdo1 = tk.IntVar()
        self.kdo2 = tk.IntVar()
        self.kdo3 = tk.IntVar()
        self.kdo4 = tk.IntVar()
        self.klop1 = tk.StringVar()
        self.klop2 = tk.StringVar()
        self.klop3 = tk.StringVar()
        self.klop4 = tk.StringVar()

        def računanjeKlop():
            '''Računamo igro Klop'''
            seznam = self.seznam
            print(seznam)
            vsota = []
            for i in seznam:
                j = seznam.index(i)
                if i%5 != 0 or i < 0:
                    messagebox.showwarning('Opozorilo', 'Številke se ne ujemajo')
                if i >= 35:
                    vsota.append(-70)
                    vsota.append(0)
                    vsota.append(0)
                    vsota.append(0)
                elif i > 0:
                    vsota.append(i*(-1))
                elif i == 0:
                    vsota.append(70)
            return vsota

        def klop():
            def odčitaj():
                self.seznam =[int(klop1.get()), int(klop2.get()), int(klop3.get()), int(klop4.get())]
                okno.destroy()
            okno = tk.Toplevel()
            okno.title('Klop')
            okno.resizable(width=False, height=False)
            j = 1
            for i in self.imena:
                tk.Label(okno, text=i).grid(row=1, column=j + 1)
                j += 1
            klop1 = tk.Entry(okno,  font="Helvetica 12", width=10)
            klop1.grid(row=2, column=2)
            klop2 = tk.Entry(okno,  font="Helvetica 12", width=10)
            klop2.grid(row=2, column=3)
            klop3 = tk.Entry(okno,  font="Helvetica 12", width=10)
            klop3.grid(row=2, column=4)
            klop4 = tk.Entry(okno,  font="Helvetica 12", width=10)
            klop4.grid(row=2, column=5)
            tk.Button(okno, text='Vredu', command=lambda: odčitaj()).grid(row =3)
            okno.wait_window(okno)

        def beli_okvirček(stolpec):
            if stolpec == 0:
                self.canvas1 = tk.Canvas(root, width=100, height=21, background='white')
                self.canvas1.grid(row=1, column=1)
            elif stolpec == 1:
                self.canvas3 = tk.Canvas(root, width=100, height=21, background='white')
                self.canvas3.grid(row=1, column=3)
            elif stolpec == 2:
                self.canvas5 = tk.Canvas(root, width=100, height=21, background='white')
                self.canvas5.grid(row=1, column=5)
            elif stolpec == 3:
                self.canvas7 = tk.Canvas(root, width=100, height=21, background='white')
                self.canvas7.grid(row=1, column=7)

        def vrstaIgre():
            """Izriše vrsto igre"""
            igre = [('Tri', 10), ('Dva', 20), ('Ena', 30), ('Solo Tri', 40), ('Solo Dva', 50),
                    ('Solo Ena', 60), ('Berač', 70), ('Solo Brez Talona', 80), ('Barvni Valat', 125), ('Valat', 250)]
            for vrstica, (ime, vrednost) in enumerate(igre):
                tk.Radiobutton(izbira, text=ime, variable=self.kaj, value=vrednost, width=10,
                               anchor="w").grid(row=6 + vrstica, column=1)
            tk.Radiobutton(izbira, text='Klop', variable=self.kaj, value=1, anchor="w").grid(row=5, column=1)


        def kdoIgra():
            """Nariše v okno Izbira, imena vseh igralcev"""
            tk.Checkbutton(izbira, text=self.imena[0], variable=self.kdo1).grid(row=2, column=3)
            tk.Checkbutton(izbira, text=self.imena[1], variable=self.kdo2).grid(row=2, column=4)
            tk.Checkbutton(izbira, text=self.imena[2], variable=self.kdo3).grid(row=2, column=5)
            tk.Checkbutton(izbira, text=self.imena[3], variable=self.kdo4).grid(row=2, column=6)

        def narišiKrogec(št_radelcev,stolpec):
            '''Narišemo krogec v stolpec'''
            '''št_radelcev: pove koliko radelcev moramo narisati'''
            '''stolpec: kateri stoplec rišemo'''
            print(št_radelcev)
            if stolpec == 1:
                if št_radelcev >= 1:
                    for koliko in range(1, št_radelcev+1):
                        self.canvas1.create_oval(10 * (št_radelcev+1), 16, 10*št_radelcev, 6, fill='green' )
                else:
                     self.canvas1 = tk.Canvas(root, width=100, height=21, background='white')
                     self.canvas1.grid(row=1, column=1)
            elif stolpec == 3:
                if št_radelcev >= 1:
                    for koliko in range(1, št_radelcev+1):
                        self.canvas3.create_oval(10 * (št_radelcev+1), 16, 10*(št_radelcev), 6, fill='green' )
                else:
                     self.canvas3 = tk.Canvas(root, width=100, height=21, background='white')
                     self.canvas3.grid(row=1, column=3)
            elif stolpec == 5:
               if št_radelcev >= 1:
                    for koliko in range(1, št_radelcev+1):
                        self.canvas5.create_oval(10 * (št_radelcev+1), 16, 10*(št_radelcev), 6, fill='green' )
               else:
                    self.canvas5 = tk.Canvas(root, width = 100, height=21, background='white')
                    self.canvas5.grid(row=1, column=5)
            elif stolpec == 7:
                if št_radelcev >= 1:
                    for koliko in range(1, št_radelcev+1):
                        self.canvas7.create_oval(10 * (št_radelcev+1), 16, 10*(št_radelcev), 6, fill='green' )
                else:
                     self.canvas7 = tk.Canvas(root, width=100, height=21, background='white')
                     self.canvas7.grid(row=1, column=7)

        def risanjeKrogcev(sez):
            stolpec = 1
            for i in sez:
                narišiKrogec(i, stolpec)
                stolpec += 2

        def številoIger(number):
            tk.Label(root, text=str(number-1)+'.', font=('Helvetica, 12')).grid(row=number, column=0)

        def seštevanjeKdo(s):
            if len(s) == 2:
                return preveriKdo(s)
            else:
                return igraSam(s)

        def radelci(i):
            if self.radelci[i] >= 1:
                return True
            return False

        def radelciBriši(s):
            if len(s) == 1:
                self.radelci[s[0]] -= 1






        def preveriKdo(s):
            def zapri(s):
                kdo.destroy()
                return igrataDva(s)
            kdo = tk.Toplevel()
            kdo.grab_set()                                   # Postavi fokus na okno in ga obdrži
            kdo.title("Igra v dva")                # Naslov okna
            kdo.resizable(width=False, height=False)         # Velikosti okna ni mogoče spreminjati
            tk.Label(kdo, text='Kdo je igral igro?').grid(row=1)
            seznam = self.imena
            print(seznam)
            for (m, i) in enumerate(seznam):
                tk.Radiobutton(kdo, text=i, variable=self.igralec, value=m).grid(row=m, column=m+1)
            tk.Button(kdo, text='Vredu', command=lambda: zapri(s)).grid(row=2)


        def seštevanje(krogec,s):
            kolikoTočk = self.kaj.get() #točke
            if kolikoTočk >= 70 and kolikoTočk != 80:
                razlika1 = 0
                dodatne = 0
                self.radelci = list(map(lambda x: x + 1, self.radelci))
            else:
                razlika1 = razlika.get()
                dodatne = Nenapovedana1.get()+ Nenapovedana2.get()+ Nenapovedana3.get()+ Nenapovedana4.get()
            seštevek = kolikoTočk + dodatne + razlika1
            if zmagal.get():
                if krogec:
                    seštevek = seštevek * 2
                    radelciBriši(s)
                    beli_okvirček(s[0])
            else:
                if krogec:
                    seštevek = seštevek * (-2)
                else:
                    seštevek = seštevek * (-1)
            return seštevek

        def igrataDva(s):
            glavni = self.igralec.get()
            self.številkaIgre += 1
            krogec = radelci(glavni)    #Postavi na True, če glavni ima radelc
            seštevek = seštevanje(krogec, [glavni])
            for i in s:
                indeks = i+1
                tk.Label(root, text=(str(seštevek)), font=('Helvetica', 12)).grid(row=self.številkaIgre, column=2*indeks-1)
                self.igralci[i] += seštevek
                tk.Label(root, text=str(self.igralci[i]), font=('Helvetica', 12)).grid(row=30, column=2*indeks-1)
            risanjeKrogcev(self.radelci)
            številoIger(self.številkaIgre)

        def igrajoVsi(s):
            '''Vnašanje igre pri igri KLOP'''
            '''s: seznam [0,1,2,3] ker igrajo vsi igralci'''
            vsotaKlop = računanjeKlop()
            m = 0
            print(vsotaKlop)
            self.številkaIgre += 1
            for i in s:
                seštevek = vsotaKlop[m]
                krogec = radelci(i)
                if krogec:
                    seštevek = seštevek * 2
                m += 1
                indeks = 2*i + 1
                tk.Label(root, text=(str(seštevek)), font=('Helvetica', 12)).grid(row=self.številkaIgre, column=indeks)
                self.igralci[i] += seštevek
                tk.Label(root, text=str(self.igralci[i]), font=('Helvetica', 12)).grid(row=30, column=indeks)
            self.radelci = list(map(lambda x: x + 1, self.radelci))

            risanjeKrogcev(self.radelci)
            številoIger(self.številkaIgre)


        def igraSam(s):
            self.številkaIgre += 1
            krogec = radelci(s[0])
            seštevek = seštevanje(krogec, s)
            print(s)
            for i in s:
                indeks = 2*i + 1
                tk.Label(root, text=(str(seštevek)), font=('Helvetica', 12)).grid(row=self.številkaIgre, column=indeks)
                self.igralci[i] += seštevek
                tk.Label(root, text=str(self.igralci[i]), font=('Helvetica', 12)).grid(row=30, column=indeks)
            risanjeKrogcev(self.radelci)
            številoIger(self.številkaIgre)

        def opozorilo1(sez):
            if len(sez) > 2 or self.kaj.get() == 0:
                messagebox.showwarning('Opozorilo', 'Preveč izbranih možnosti')
                return False
            return True


        def kdoIgra1(sez):
            j= 0
            seznam = []
            for i in sez:
                if i == 1:
                    seznam.append(j)
                j += 1
            return seznam

        def pišiVzvezek(s):
            '''Rezultat trenutne igre zapišemo v datoteko .txt'''
            file = open("tarok.txt", "w")
            imena = self.imena
            kaj = self.kaj.get()
            razlika1 = razlika.get()
            if self.kaj.get() == 1:
                vsotaKlop = računanjeKlop()
                print(str(self.številkaIgre-1) + '\t' + 'Klop:' + imena[0] + ': ' + str(vsotaKlop[0]) + ', ' +
                      imena[1] + ': '+str(vsotaKlop[1]) + ', ' + imena[2] + ': ' + str(vsotaKlop[2]) + ', ' + imena[3] + ': ' +
                      str(vsotaKlop[3]), file=file )
            if zmagal.get():
                zmagalJe = 'zmagal'
            else:
                zmagalJe = 'izgubil'
            if len(s) == 1:
                kdo = imena[s[0]]
                print(kdo + ' je igral ' + (list(igre.keys())[list(igre.values()).index(kaj)]) + ' in '+zmagalJe + ' z razliko ' + str(razlika1) +'.' +
                      ' Napovedi: ', file=file)






        def iz():
            '''Ob kliku na gumb Izpiši se izvede ta funkcija'''
            if self.kaj.get() == 1:
                klop()
                igrajoVsi([0, 1, 2, 3])
                kdo = [0, 1, 2, 3]
            else:
                kdo = kdoIgra1([self.kdo1.get(), self.kdo2.get(), self.kdo3.get(), self.kdo4.get()])
                t = opozorilo1(kdo)
                if t:
                    seštevanjeKdo(kdo)
            pišiVzvezek(kdo)
            print(self.radelci)

        tk.Label(izbira, text="Zapisnik igre", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=4) #naslov
        #-------------------KDO JE IGRAL ----------------------------

        tk.Label(izbira, text="Kdo je igral: ").grid(row=1, column=1, sticky = 'W')
        kdoIgra()

        #---------VRSTE IGRE -------------------------------
        tk.Label(izbira, text="Izberite igro: ").grid(row=4, column=1, sticky = 'W')
        vrstaIgre()

        #----------------------------------DODATNE IGRE -----------------------
        tk.Label(izbira, text = "Dodatne igre - nenapovedane: ").grid(row=4, column=3, sticky = 'W')

        tk.Checkbutton(izbira, text='Kralji', variable=Nenapovedana1, onvalue=10, width=10,
                       anchor="w").grid(row=5, column=3)
        tk.Checkbutton(izbira, text='Trula', variable=Nenapovedana2, onvalue=10, width=10,
                       anchor="w").grid(row=6, column=3)
        tk.Checkbutton(izbira, text='Zadnji kralj', variable=Nenapovedana3, onvalue=10, width=10,
                       anchor="w").grid(row=7, column=3)
        tk.Checkbutton(izbira, text='pagatUltimo', variable=Nenapovedana4, onvalue=25, width=10,
                       anchor="w").grid(row=8, column=3)

        tk.Label(izbira, text="Dodatne igre - napovedane: ").grid(row=4, column=5, sticky = 'W')
        tk.Checkbutton(izbira, text='Kralji', variable=Nenapovedana1, onvalue=20, width=10,
                       anchor="w").grid(row=5, column=5)
        tk.Checkbutton(izbira, text='Trula', variable=Nenapovedana2, onvalue=20, width=10,
                       anchor="w").grid(row=6, column=5)
        tk.Checkbutton(izbira, text='Zadnji kralj', variable=Nenapovedana3, onvalue=20, width=10,
                       anchor="w").grid(row=7, column=5)
        tk.Checkbutton(izbira, text='pagatUltimo', variable=Nenapovedana4, onvalue=50, width=10,
                       anchor="w").grid(row=8, column=5)
        #--------ZMAGAL/ZGUBIL--------------------------
        tk.Label(izbira, text = 'Zmagal/Izgubil').grid(row=12, column=3)
        tk.Radiobutton(izbira, text='Zmagal', variable=zmagal, value=True, width=10,
                       anchor='w').grid(row=12, column=4)
        tk.Radiobutton(izbira, text='Izgubil', variable=zmagal, value=False, width=10,
                       anchor='w').grid(row=12, column=5)
        #------------------------------------------------------------------------
        tk.Label(izbira, text='Razlika: ').grid(row=10, column=3, sticky='W')
        tk.Entry(izbira, font="Helvetica 12", width=10, textvariable=razlika).grid(row=10, column=4)
        tk.Button(izbira, text='Izpiši', command=lambda: iz()).grid(row=20, column=5)




if __name__ == "__main__":
    # Ustvarimo glavno okno igre
    root = tk.Tk()
    root.title("Tarok")

    # Ustvarimo objekt razreda GUI in ga pospravimo
    aplikacija = GUI(root)

    # Mainloop nadzira glavno okno in se neha izvajati ko okno zapremo
    root.mainloop()
