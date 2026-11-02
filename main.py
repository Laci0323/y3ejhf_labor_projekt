import tkinter as tk
from tkinter import ttk, messagebox
from MLS_modul import ZeneMLS

app = tk.Tk()
app.title("Zenei lejátszási lista")

szelesseg = (app.winfo_screenwidth() - 500) // 2
magassag = (app.winfo_screenheight() - 500) // 2
app.geometry(f"500x500+{szelesseg}+{magassag}")
app.resizable(False, False)

app.iconphoto(True, tk.PhotoImage(file="icon.png"))

stilus = ttk.Style()
stilus.theme_use("clam")
stilus.configure("TButton", font=("Arial", 12), padding=6)
stilus.configure("TLabel", font=("Arial", 12))

zenekezelo = ZeneMLS()

def megnyit_MLS(oldal):
    menu.pack_forget()
    oldal.pack(fill="both", expand=True)

def fomenu_MLS(oldal):
    oldal.pack_forget()
    menu.pack(fill="both", expand=True)

def oldal_MLS(cim):
    oldal = ttk.Frame(app)
    ttk.Label(oldal, text=cim, font=("Arial", 24, "bold")).pack(pady=30)
    ttk.Button(oldal, text="Vissza a főmenübe", command=lambda: fomenu_MLS(oldal)).pack(side="bottom", pady=15)
    return oldal

def beviteli_oldal_MLS(cim, felirat, parancs):
    oldal = oldal_MLS(cim)
    mezo = ttk.Entry(oldal, width=30)
    mezo.pack(pady=15)
    ttk.Button(oldal, text=felirat, command=parancs).pack()
    visszajelzo = ttk.Label(oldal)
    visszajelzo.pack(pady=15)
    return oldal, mezo, visszajelzo

def hozzaadas_MLS():
    zene = hozzaadas_mezo.get().strip()
    if zene == "":
        messagebox.showwarning("Üres mező", "Üres mezőt nem lehet hozzáadni a listához!")
    elif zenekezelo.mentes_MLS(zene, 1):
        hozzaadas_visszajelzo.config(text="A zene sikeresen hozzá lett adva a listához!")
    else:
        messagebox.showwarning("Létező zeneszám", "A megadott zene már létezik a listában!")
    hozzaadas_mezo.delete(0, tk.END)

def kereses_MLS():
    zene = kereses_mezo.get().strip()
    if zene == "":
        messagebox.showwarning("Üres mező", "Üres mezőt nem lehet keresni a listában!")
    elif zenekezelo.letezik_MLS(zene):
        kereses_visszajelzo.config(text="A keresett zene létezik a listában.")
    else:
        kereses_visszajelzo.config(text="A keresett zene nem létezik a listában.")
    kereses_mezo.delete(0, tk.END)

def torles_MLS():
    zene = torles_mezo.get().strip()
    if zene == "":
        messagebox.showwarning("Üres mező", "Üres mezőt nem lehet törölni a listához!")
    elif zenekezelo.torles_MLS(zene):
        torles_visszajelzo.config(text="A zene törlése sikeres volt.")
    else:
        torles_visszajelzo.config(text="A törölni kívánt zene nem létezik a listában.")
    torles_mezo.delete(0, tk.END)

def listaz_MLS():
    lista.delete(0, tk.END)
    for cim in zenekezelo.zenek:
        lista.insert(tk.END, f"{cim} - {zenekezelo.zenek[cim]} hallgatás")

def hallgatas_MLS():
    kivalasztott = lista.curselection()
    if not kivalasztott:
        messagebox.showwarning("Hiányzó kiválasztás", "Először válassz ki egy zenét a listából!")
        return
    cim = list(zenekezelo.zenek)[kivalasztott[0]]
    zenekezelo.hallgatas_MLS(cim)
    listaz_MLS()
    lista.selection_set(kivalasztott[0])

def toplista_MLS():
    rendezett = sorted(zenekezelo.zenek, key=zenekezelo.zenek.get, reverse=True)
    szoveg = ""
    for helyezes, cim in enumerate(rendezett[:10], 1):
        szoveg += f"{helyezes}. {cim} - {zenekezelo.zenek[cim]} hallgatás\n"
    toplista_cimke.config(text=szoveg)

hozzaadas_oldal, hozzaadas_mezo, hozzaadas_visszajelzo = beviteli_oldal_MLS("Zene hozzáadása", "Zene hozzáadása", hozzaadas_MLS)
kereses_oldal, kereses_mezo, kereses_visszajelzo = beviteli_oldal_MLS("Zene keresése", "Zene keresése", kereses_MLS)
torles_oldal, torles_mezo, torles_visszajelzo = beviteli_oldal_MLS("Zene törlése", "Zene törlése", torles_MLS)

lista_oldal = oldal_MLS("Zenék listázása")
lista = tk.Listbox(lista_oldal, font=("Arial", 12))
lista.pack(fill="both", expand=True, padx=20, pady=20)
ttk.Button(lista_oldal, text="Hallgatottság növelése", command=hallgatas_MLS).pack(pady=10)

toplista_oldal = oldal_MLS("Hallgatási toplista")
toplista_cimke = ttk.Label(toplista_oldal, font=("Arial", 14, "bold"))
toplista_cimke.pack(pady=20)

menu = ttk.Frame(app)
ttk.Label(menu, text="Zenei lejátszási lista", font=("Arial", 24, "bold")).pack(pady=30)

menu_gombok = [
    ("Zene hozzáadása", lambda: megnyit_MLS(hozzaadas_oldal)),
    ("Zenék listázása", lambda: (megnyit_MLS(lista_oldal), listaz_MLS())),
    ("Zene keresése", lambda: megnyit_MLS(kereses_oldal)),
    ("Zene törlése", lambda: megnyit_MLS(torles_oldal)),
    ("Hallgatási toplista", lambda: (megnyit_MLS(toplista_oldal), toplista_MLS())),
    ("Kilépés", lambda: app.destroy() if messagebox.askyesno("Kilépés", "Biztosan ki szeretnél lépni?") else None),
]

for felirat, parancs in menu_gombok:
    ttk.Button(menu, text=felirat, width=24, command=parancs).pack(pady=5)

menu.pack(fill="both", expand=True)
app.mainloop()