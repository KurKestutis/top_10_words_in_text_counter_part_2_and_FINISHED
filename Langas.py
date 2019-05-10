from paste_6 import *
import collections
# from funkcijos import *

langas = Tk()
langas.title("Dažniausiai tekste panaudotų žodžių skaičiuoklė (Top - 10) KK X 4.0")
langas.iconbitmap(r'top_X4.ico')
# langas.config(background="blue")

# Pasiimti duomenis iš bokso ir viska padaryti iki atsakymo returninimo
def pasiimti():
    duomenys = boksas.get("1.0", "end-1c")
    duomenys2 = str(duomenys)
    print("Štai kas paiimta iš bokso(duomeny): " + str(duomenys))
    print("O štai kaip tarodo duomenys2: " + str(duomenys2))

    pateikta = duomenys.lower()
    for skiryba in [',', ':', '.', '"', '!', '?', '–', '(', ')','ir', ' kad,', ' the ', ' a ', ' o ', ' kad ', '\n', '\r']:
        pateikta = pateikta.replace(skiryba, '')
    visi_zodziai = pateikta.split(" ")
    # PATIKRINIMUI ATSPAUSDINAM jei norim
    # print(visi_zodziai)

    zodziu_skaicius = {}
    for zodis in visi_zodziai:
        suskaiciuota_dabar = zodziu_skaicius.get(zodis, 0)
        suskaiciuota_dabar_update = suskaiciuota_dabar + 1
        zodziu_skaicius[zodis] = suskaiciuota_dabar_update
    print("zodziu_skaicius yra :" + str(zodziu_skaicius))

    zodis = collections.namedtuple('zodis', 'score name')
    d = zodziu_skaicius
    best = sorted([zodis(v, k) for (k, v) in d.items()], reverse=True)
    print(best)

    ats1 = Label(langas, text=best[0].name )
    ats1.grid(row=22, column=2, sticky=W+E)
    pk1 = Label(langas, text=best[0].score )
    pk1.grid(row=22, column=4, sticky=W+E)

    ats2 = Label(langas, text=best[1].name )
    ats2.grid(row=23, column=2, sticky=W+E)
    pk2 = Label(langas, text=best[1].score )
    pk2.grid(row=23, column=4, sticky=W+E)

    ats3 = Label(langas, text=best[2].name)
    ats3.grid(row=24, column=2, sticky=W + E)
    pk3 = Label(langas, text=best[2].score)
    pk3.grid(row=24, column=4, sticky=W + E)

    ats4 = Label(langas, text=best[3].name )
    ats4.grid(row=25, column=2, sticky=W+E)
    pk4 = Label(langas, text=best[3].score )
    pk4.grid(row=25, column=4, sticky=W+E)

    ats5 = Label(langas, text=best[4].name )
    ats5.grid(row=26, column=2, sticky=W+E)
    pk5 = Label(langas, text=best[4].score )
    pk5.grid(row=26, column=4, sticky=W+E)

    ats6 = Label(langas, text=best[5].name )
    ats6.grid(row=27, column=2, sticky=W+E)
    pk6 = Label(langas, text=best[5].score )
    pk6.grid(row=27, column=4, sticky=W+E)

    ats7 = Label(langas, text=best[6].name )
    ats7.grid(row=28, column=2, sticky=W+E)
    pk7 = Label(langas, text=best[6].score )
    pk7.grid(row=28, column=4, sticky=W+E)

    ats8 = Label(langas, text=best[7].name)
    ats8.grid(row=29, column=2, sticky=W + E)
    pk8 = Label(langas, text=best[7].score)
    pk8.grid(row=29, column=4, sticky=W + E)

    ats9 = Label(langas, text=best[8].name )
    ats9.grid(row=30, column=2, sticky=W+E)
    pk9 = Label(langas, text=best[8].score )
    pk9.grid(row=30, column=4, sticky=W+E)

    ats10 = Label(langas, text=best[9].name )
    ats10.grid(row=31, column=2, sticky=W+E)
    pk10 = Label(langas, text=best[9].score )
    pk10.grid(row=31, column=4, sticky=W+E)


"""-----------Laukai/Mygtukai/Užrašai----------"""
uzrasas1 = Label(langas, text="Įveskite tekstą:")
boksas = Text(langas, height=20, width=70)
mygtukas_pateikti = Button(langas, text="          Pateikti          ", command=lambda: pasiimti())
#command=lambda: pasiimti() >>> just means do this when i press the button

parasteWN = Label(langas, text="   ")
parasteEN = Label(langas, text="   ")
parasteWS = Label(langas, text="   ")
parasteEN = Label(langas, text="   ")
perskyrimas = Label(langas, text="   ")

"""-------------------PARAŠTĖS--------------------"""
parasteWN.grid(row=0, column=0)
parasteEN.grid(row=0, column=7)
parasteWS.grid(row=32, column=0)
parasteEN.grid(row=32, column=7)
perskyrimas.grid(row=15, column=0)

"""-------------FUNKCIJŲ PALEIDIMAS---------------"""
boksas.grid(row=2, column=1, columnspan=6, sticky=W)

uzrasas1.grid(row=1, column=1, sticky=W)
mygtukas_pateikti.grid(row=16, column=6, sticky=E)

"""--------------------POPUO MENU----------------"""
boksas.bind('<Button-3>', rClicker, add='')

'''-----------------SCCROLLBAR-------------------'''
#nesugebėjau padaryti:(

"""--------ATSAKYMU DALIES LENTELE-----------"""
perskyrimas_du = Label(langas, text="   ")
perskyrimas_du.grid(row=17, column=0, sticky=E)

zodis = Label(langas, text="Žodis:                                  ")
zodis.grid(row=20, column=2, sticky=W+E)

panaudotas_kartu = Label(langas, text="Panaudotas kartų:            ")
panaudotas_kartu.grid(row=20, column=4, sticky=W)

# procentai = Label(langas, text="Procentais:            ")
# procentai.grid(row=20, column=6, sticky=W+E)

skaicius1 = Label(langas, text="1   ")
skaicius1.grid(row=22, column=1, sticky=E)
skaicius2 = Label(langas, text="2   ")
skaicius2.grid(row=23, column=1, sticky=E)
skaicius3 = Label(langas, text="3   ")
skaicius3.grid(row=24, column=1, sticky=E)
skaicius4 = Label(langas, text="4   ")
skaicius4.grid(row=25, column=1, sticky=E)
skaicius5 = Label(langas, text="5   ")
skaicius5.grid(row=26, column=1, sticky=E)
skaicius6 = Label(langas, text="6   ")
skaicius6.grid(row=27, column=1, sticky=E)
skaicius7 = Label(langas, text="7   ")
skaicius7.grid(row=28, column=1, sticky=E)
skaicius8 = Label(langas, text="8   ")
skaicius8.grid(row=29, column=1, sticky=E)
skaicius9 = Label(langas, text="9   ")
skaicius9.grid(row=30, column=1, sticky=E)
skaicius10 = Label(langas, text="10   ")
skaicius10.grid(row=31, column=1, sticky=E)

"""----------ATSAKYMU SLOTAI-----------"""
# atsakymas1 = StringVar()
# ats1 = Label(langas, textvariable= atsakymas1)
# ats1 = Label(langas, text=pirmas_z )
# ats1.grid(row=22, column=2, sticky=W)

"""----------ATSAKYMU SLOTAI-----------"""
# atsakymas1 = StringVar()
# ats1 = Label(langas, textvariable= atsakymas1)
# ats1.grid(row=22, column=2, sticky=W)

# print(ats_list)
langas.mainloop()
