# Zenei lejátszási lista

**Hallgató:** Majerik László Sándor
**Neptun-kód:** Y3EJHF

## Feladat leírása

A program egy zenei lejátszási lista kezelő alkalmazás. A felhasználó zenéket vehet fel a listára, kereshet közöttük, törölheti őket, és növelheti a hallgatásuk számát. A program a hallgatások száma alapján toplistát készít a tíz legtöbbet hallgatott zenéről. Az adatokat a `zenek.txt` fájlban tárolja, így a program újraindítása után is megmaradnak.

## Felhasználói leírás

- Szükséges: Python 3 (a `tkinter` a Python része, külön telepíteni nem kell).
- Indítás: `python main.py`
- A `main.py`, az `MLS_modul.py`, az `icon.png` és a `zenek.txt` egy mappában legyenek. Ha a `zenek.txt` hiányzik, a program létrehozza.
- A `zenek.txt` sorai `cím|hallgatások száma` formátumúak, például `Példa zene|3`.
- A program a képernyő közepén indul, az ablak mérete fix.

## Felépítés

**Modul:** `MLS_modul.py` (saját modul)

**Osztály:** `ZeneMLS`, a zenék tárolását és a fájlkezelést végzi. A zenéket szótárban tárolja (cím: hallgatások száma).

**Az osztály metódusai:**
- `betoltes_MLS`: betölti a zenéket a fájlból
- `fajlbament_MLS`: kiírja a zenéket a fájlba
- `letezik_MLS`: megmondja, szerepel-e a zene a listában
- `mentes_MLS`: új zenét ad a listához
- `torles_MLS`: töröl egy zenét
- `hallgatas_MLS`: növeli egy zene hallgatásainak számát

**Függvények a `main.py`-ban:**
- `megnyit_MLS`, `fomenu_MLS`: oldalak közötti váltás
- `oldal_MLS`, `beviteli_oldal_MLS`: az oldalak felépítése
- `hozzaadas_MLS`, `kereses_MLS`, `torles_MLS`: a három beviteli oldal funkciója
- `listaz_MLS`, `hallgatas_MLS`: a lista megjelenítése és a hallgatás növelése
- `toplista_MLS`: a toplista összeállítása

**Grafikus felület:** `tkinter` és `ttk`. Az eseménykezelést a gombok `command` paraméterei valósítják meg.
