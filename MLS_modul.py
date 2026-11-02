class ZeneMLS:
    def __init__(self):
        self.fajl = "zenek.txt"
        with open (self.fajl, "a", encoding="utf-8"):
            pass
        self.zenek = self.betoltes_MLS()
    def betoltes_MLS(self):
        zenek = {}
        with open (self.fajl, "r", encoding="utf-8") as f:
            for sor in f:
                cim, hallgatas = sor.strip().split("|")
                zenek[cim] = int(hallgatas)
        return zenek

    def fajlbament_MLS(self):
        with open (self.fajl, "w", encoding="utf-8") as f:
            for cim in self.zenek:
                f.write(f"{cim}|{self.zenek[cim]}\n")

    def letezik_MLS(self, cim):
        return cim in self.zenek

    def mentes_MLS(self, cim, hallgat):
        if self.letezik_MLS(cim):
            return False
        self.zenek[cim] = hallgat
        self.fajlbament_MLS()
        return True

    def torles_MLS(self, cim):
        if not self.letezik_MLS(cim):
            return False
        del self.zenek[cim]
        self.fajlbament_MLS()
        return True

    def hallgatas_MLS(self, cim):
        if not self.letezik_MLS(cim):
            return False
        self.zenek[cim] += 1
        self.fajlbament_MLS()
        return True
