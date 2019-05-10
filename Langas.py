from paste_6 import *
import collections
# from funkcijos import *

langas = Tk()
langas.title("Dažniausiai tekste panaudotų žodžių skaičiuoklė (Top - 10) KK X 4.0")
langas.iconbitmap(r'top_X4.ico')
# langas.config(background="blue")

ats_list =["", ""]

def pateikti_atsakyma(a):
    ats_list = a
    atsakymas1.set(ats_list[0])

# Pasiimti duomenis iš bokso ir viska padaryti iki atsakymo returninimo

def pasiimti():
    duomenys = boksas.get("1.0", "end-1c")
    duomenys2 = str(duomenys)
    print("Štai kas paiimta iš bokso(duomeny): " + str(duomenys))
    print("O štai kaip tarodo duomenys2: " + str(duomenys2))
    # x = duomenys.split()
    #
    # pateikti_atsakyma(x)
    # print(x)
    # return x

    pateikta = duomenys.lower()
    for skiryba in [',', ':', '.', '"', '!', '?', '–', '(', ')', '\n', '\r']:
        pateikta = pateikta.replace(skiryba, ' ')
    visi_zodziai = pateikta.split(" ")
    # PATIKRINIMUI ATSPAUSDINAM
    print(visi_zodziai)

    zodziu_skaicius = {}
    for zodis in visi_zodziai:
        suskaiciuota_dabar = zodziu_skaicius.get(zodis, 0)
        suskaiciuota_dabar_update = suskaiciuota_dabar + 1
        zodziu_skaicius[zodis] = suskaiciuota_dabar_update
    print("zodziu_skaicius yra :" + str(zodziu_skaicius))

    zodis = collections.namedtuple('zodis', 'score name')
    d = zodziu_skaicius
    worst = sorted(zodis(v, k) for (k, v) in d.items())
    best = sorted([zodis(v, k) for (k, v) in d.items()], reverse=True)
    print(best[0])
    print(best[0].name)
    print(best[0].score)

    pirmas_z = str(best[0].name)
    pirmas_s = best[0].score
    #
    print(pirmas_z)
    # print(pirmas_s)
    # pateikti_atsakyma()
    print(best)
    ats_list.append(pirmas_z)
    pateikti_atsakyma(a)
    return ats_list

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
zodis.grid(row=20, column=2, sticky=W)

panaudotas_kartu = Label(langas, text="Panaudotas kartų:            ")
panaudotas_kartu.grid(row=20, column=4, sticky=E)

procentai = Label(langas, text="Procentais:            ")
procentai.grid(row=20, column=6, sticky=E)

skaicius1 = Label(langas, text="1   ")
skaicius1.grid(row=22, column=1, sticky=E)
skaicius2 = Label(langas, text="2   ")
skaicius2.grid(row=23, column=1, sticky=E)
skaicius3 = Label(langas, text="3   ")
skaicius3.grid(row=24, column=1, sticky=E)

"""----------ATSAKYMU SLOTAI-----------"""
# atsakymas1 = StringVar()
# ats1 = Label(langas, textvariable= atsakymas1)
# ats1 = Label(langas, text=pirmas_z )
# ats1.grid(row=22, column=2, sticky=W)

"""----------ATSAKYMU SLOTAI-----------"""
atsakymas1 = StringVar()
ats1 = Label(langas, textvariable = atsakymas1)
ats1.grid(row=22, column=2, sticky=W)


print(ats_list)
langas.mainloop()
