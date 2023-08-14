import tkinter as tk
from tkinter import simpledialog, messagebox


class Stalvirsis:
    def __init__(self, tipas, ilgis, plotis):
        self.tipas = tipas
        self.ilgis = ilgis
        self.plotis = plotis


class Bortelis:
    def __init__(self, tipas, ilgis):
        self.tipas = tipas
        self.ilgis = ilgis


class Kriaukle:
    def __init__(self, tipas):
        self.tipas = tipas


class Palange:
    def __init__(self, ilgis, plotis):
        self.ilgis = ilgis
        self.plotis = plotis


class SieninisSkydas:
    def __init__(self, tipas, ilgis, plotis):
        self.tipas = tipas
        self.ilgis = ilgis
        self.plotis = plotis


class KrastinesApdirbimas:
    def __init__(self, ilgis):
        self.ilgis = ilgis


class Montavimas:
    def __init__(self, tipas):
        self.tipas = tipas


class Pristatymas:
    def __init__(self, tipas):
        self.tipas = tipas


class GaminioSkaiciuokle:
    def __init__(self):
        self.stalvirsiai = []
        self.borteliai = []
        self.kriaukles = []
        self.palanges = []
        self.sieniniai_skydai = []
        self.krastines_apdirbimai = []
        self.montavimai = []
        self.pristatymai = []

    def ivesti_stalvirsi(self, tipas, ilgis, plotis=0):
        stalvirsis = Stalvirsis(tipas, ilgis, plotis)
        self.stalvirsiai.append(stalvirsis)

    def ivesti_borteli(self, tipas, ilgis):
        bortelis = Bortelis(tipas, ilgis)
        self.borteliai.append(bortelis)

    def ivesti_kriaukle(self, tipas):
        kriaukle = Kriaukle(tipas)
        self.kriaukles.append(kriaukle)

    def ivesti_palange(self, ilgis, plotis):
        palange = Palange(ilgis, plotis)
        self.palanges.append(palange)

    def ivesti_sienini_skyda(self, tipas, ilgis, plotis):
        sieninis_skydas = SieninisSkydas(tipas, ilgis, plotis)
        self.sieniniai_skydai.append(sieninis_skydas)

    def ivesti_krastines_apdirbima(self, ilgis):
        krastines_apdirbimas = KrastinesApdirbimas(ilgis)
        self.krastines_apdirbimai.append(krastines_apdirbimas)

    def ivesti_montavima(self, tipas):
        montavimas = Montavimas(tipas)
        self.montavimai.append(montavimas)

    def ivesti_pristatyma(self, tipas):
        pristatymas = Pristatymas(tipas)
        self.pristatymai.append(pristatymas)

    def gauti_gaminio_kaina(self):
        total_kaina = 0

        for stalvirsis in self.stalvirsiai:
            if stalvirsis.tipas == 1:  # Standartas
                total_kaina += 235 * stalvirsis.ilgis
            if stalvirsis.tipas == 2:  # Nestandartas
                total_kaina += 350 * stalvirsis.ilgis * stalvirsis.plotis

        for bortelis in self.borteliai:
            if bortelis.tipas == 1:  # Status
                total_kaina += 40 * bortelis.ilgis
            if bortelis.tipas == 2:  # Monolitinis
                total_kaina += 65 * bortelis.ilgis

        for kriaukle in self.kriaukles:
            if kriaukle.tipas == 1:  # Maža plautuvė
                total_kaina += 205
            if kriaukle.tipas == 2:  # Vidutinė plautuvė
                total_kaina += 340
            if kriaukle.tipas == 3:  # Didelė plautuvė
                total_kaina += 445
            if kriaukle.tipas == 4:  # Plautuvių komplektas
                total_kaina += 535
            if kriaukle.tipas == 5:  # Kliento plautuvė
                total_kaina += 180
            if kriaukle.tipas == 6:  # Quadro kriauklė
                total_kaina += 340
            if kriaukle.tipas == 7:  # Elipse kriauklė
                total_kaina += 200
            if kriaukle.tipas == 8:  # Kriauklė su paslėptu nubėgimu
                total_kaina += 720

        for palange in self.palanges:
            total_kaina += 350 * palange.ilgis * palange.plotis

        for sieninis_skydas in self.sieniniai_skydai:
            if sieninis_skydas.tipas == 1:  # Status sieninis skydas
                total_kaina += 205 * sieninis_skydas.ilgis * sieninis_skydas.plotis
            if sieninis_skydas.tipas == 2:  # Monolitinis sieninis skydas
                total_kaina += 310 * sieninis_skydas.ilgis * sieninis_skydas.plotis

        for krastine_apdirbimas in self.krastines_apdirbimai:
            total_kaina += 21 * krastine_apdirbimas.ilgis

        for montavimas in self.montavimai:
            if montavimas.tipas == 1:  # Lieto marmuro kriauklės
                total_kaina += 200
            if montavimas.tipas == 2:  # Tiesus stalviršis
                total_kaina += 300
            if montavimas.tipas == 3:  # Kampinis stalviršis
                total_kaina += 350
            if montavimas.tipas == 4:  # Stalviršis su palange/sala
                total_kaina += 400
            if montavimas.tipas == 5:  # Stalviršis su stačiais sieniniais skydais
                total_kaina += 450
            if montavimas.tipas == 6:  # Stalviršis su monolitiniais sieniniais skydais
                total_kaina += 500

        for pristatymas in self.pristatymai:
            if pristatymas.tipas == 1:  # Standartinis pristatymas
                total_kaina += 100
            if pristatymas.tipas == 2:  # Pristatymas Neringoje
                total_kaina += 150

        return total_kaina


class GaminioSkaiciuokleApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gaminio Skaičiuoklė")

        self.gaminio_skaiciuokle = GaminioSkaiciuokle()

        self.iveskite_frame = tk.Frame(self)
        self.iveskite_frame.pack(padx=10, pady=10)

        self.pasirinkimas_label = tk.Label(self.iveskite_frame, text="Pasirinkite veiksmą:")
        self.pasirinkimas_label.pack()

        self.mygtukas_prideti_stalvirsi = tk.Button(self.iveskite_frame, text="Pridėti stalviršį",
                                                    command=self.prideti_stalvirsi)
        self.mygtukas_prideti_stalvirsi.pack()

        self.mygtukas_prideti_borteli = tk.Button(self.iveskite_frame, text="Pridėti bortelį",
                                                  command=self.prideti_borteli)
        self.mygtukas_prideti_borteli.pack()

        self.mygtukas_prideti_kriaukle = tk.Button(self.iveskite_frame, text="Pridėti kriauklę",
                                                   command=self.prideti_kriaukle)
        self.mygtukas_prideti_kriaukle.pack()

        self.mygtukas_prideti_palange = tk.Button(self.iveskite_frame, text="Pridėti palangę",
                                                  command=self.prideti_palange)
        self.mygtukas_prideti_palange.pack()

        self.mygtukas_prideti_sienini_skyda = tk.Button(self.iveskite_frame, text="Pridėti sieninį skydą",
                                                        command=self.prideti_sienini_skyda)
        self.mygtukas_prideti_sienini_skyda.pack()

        self.mygtukas_prideti_krastines_apdirbima = tk.Button(self.iveskite_frame, text="Pridėti kraštinės apdirbimą",
                                                              command=self.prideti_krastines_apdirbima)
        self.mygtukas_prideti_krastines_apdirbima.pack()

        self.mygtukas_prideti_montavima = tk.Button(self.iveskite_frame, text="Pridėti montavimą",
                                                    command=self.prideti_montavima)
        self.mygtukas_prideti_montavima.pack()

        self.mygtukas_prideti_pristatyma = tk.Button(self.iveskite_frame, text="Pridėti pristatymą",
                                                     command=self.prideti_pristatyma)
        self.mygtukas_prideti_pristatyma.pack()

        self.tarpas_label = tk.Label(self.iveskite_frame, text="")
        self.tarpas_label.pack()

        self.mygtukas_apskaiciuoti_kaina = tk.Button(self.iveskite_frame, text="Apskaičiuoti kainą",
                                                     command=self.apskaiciuoti_kaina)
        self.mygtukas_apskaiciuoti_kaina.pack()

        self.rezultatu_frame = tk.Frame(self)
        self.rezultatu_frame.pack(padx=10, pady=10)

        self.rezultatai_text = tk.Text(self.rezultatu_frame, height=2, width=40)
        self.rezultatai_text.pack()

        menu = tk.Menu(self)
        self.config(menu=menu)

        sub_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Meniu", menu=sub_menu)

        sub_menu.add_command(label="Išvalyti", command=self.isvalyti_duomenis)

        sub_menu.add_separator()
        sub_menu.add_command(label="Išeiti", command=self.iseiti)

    def isvalyti_duomenis(self):
        self.gaminio_skaiciuokle = GaminioSkaiciuokle()
        self.rezultatai_text.delete(1.0, tk.END)
        messagebox.showinfo("Pranešimas", "Duomenys išvalyti sėkmingai!")

    def iseiti(self):
        self.destroy()

    def prideti_stalvirsi(self):
        tipas = simpledialog.askinteger("Stalviršio tipas",
                                        "Pasirinkite stalviršio tipą:\n1-Standartas, 2-Nestandartas")

        if tipas is not None:
            if tipas == 1:
                ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite stalviršio ilgį (metrais):")
                if ilgis is not None:
                    self.gaminio_skaiciuokle.ivesti_stalvirsi(tipas, ilgis)
                    messagebox.showinfo("Pranešimas", "Stalviršis pridėtas sėkmingai!")
            elif tipas == 2:
                ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite stalviršio ilgį (metrais):")
                if ilgis is not None:
                    plotis = simpledialog.askfloat("Įveskite plotį", "Įveskite stalviršio plotį (metrais):")
                    if plotis is not None:
                        self.gaminio_skaiciuokle.ivesti_stalvirsi(tipas, ilgis, plotis)
                        messagebox.showinfo("Pranešimas", "Stalviršis pridėtas sėkmingai!")
            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingąi. Bandykite dar kartą.")

    def prideti_borteli(self):
        tipas = simpledialog.askinteger("Bortelio tipas", "Pasirinkite bortelio tipą:\n1-Status, 2-Monolitinis")

        if tipas is not None:
            if tipas == 1 or tipas == 2:
                ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite bortelio ilgį (metrais):")
                if ilgis is not None:
                    self.gaminio_skaiciuokle.ivesti_borteli(tipas, ilgis)
                    messagebox.showinfo("Pranešimas", "Bortelis pridėtas sėkmingai!")
            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingai. Bandykite dar kartą.")

    def prideti_kriaukle(self):
        tipas = simpledialog.askinteger("Kriauklės tipas", "Pasirinkite kriauklės tipą:\n1-Maža plautuvė, 2-Vidutinė "
                                                           "plautuvė, 3-Didelė plautuvė,\n4-Plautuvių komplektas, "
                                                           "5-Kliento plautuvė,\n6-Quadro kriauklė, "
                                                           "7-Elipse kriauklė, 8-Kriauklė su paslėptu nubėgimu")
        if tipas is not None:
            if tipas in range(1, 9):
                self.gaminio_skaiciuokle.ivesti_kriaukle(tipas)
                messagebox.showinfo("Pranešimas", "Kriauklė pridėta sėkmingai!")

            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingai. Bandykite dar kartą.")

    def prideti_palange(self):
        ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite palangės ilgį (metrais):")
        if ilgis is not None:
            plotis = simpledialog.askfloat("Įveskite plotį", "Įveskite palangės plotį (metrais):")
            if plotis is not None:
                self.gaminio_skaiciuokle.ivesti_palange(ilgis, plotis)
                messagebox.showinfo("Pranešimas", "Palangė pridėta sėkmingai!")

    def prideti_sienini_skyda(self):
        tipas = simpledialog.askinteger("Sieninio skydo tipas",
                                        "Pasirinkite sieninio skydo tipą:\n1-Status sieninis skydas, 2-Monolitinis "
                                        "sieninis skydas")
        if tipas is not None:
            if tipas == 1 or tipas == 2:
                ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite sieninio skydo ilgį (metrais):")
                if ilgis is not None:
                    plotis = simpledialog.askfloat("Įveskite plotį", "Įveskite sieninio skydo plotį (metrais):")
                    if plotis is not None:
                        self.gaminio_skaiciuokle.ivesti_sienini_skyda(tipas, ilgis, plotis)
                        messagebox.showinfo("Pranešimas", "Sieninis skydas pridėtas sėkmingai!")
            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingai. Bandykite dar kartą.")

    def prideti_krastines_apdirbima(self):
        ilgis = simpledialog.askfloat("Įveskite ilgį", "Įveskite kraštinės apdirbimo ilgį (metrais):")
        if ilgis is not None:
            self.gaminio_skaiciuokle.ivesti_krastines_apdirbima(ilgis)
            messagebox.showinfo("Pranešimas", "Kraštinės apdirbimas pridėtas sėkmingai!")

    def prideti_montavima(self):
        tipas = simpledialog.askinteger("Montavimo tipas",
                                        "Pasirinkite montavimo tipą:\n1-Lieto marmuro kriauklės, 2-Tiesus stalviršis,"
                                        "\n3-Kampinis stalviršis, 4-Stalviršis su palange/sala,\n5-Stalviršis su "
                                        "stačiais sieniniais skydais, 6-Stalviršis su monolitiniais sieniniais skydais")
        if tipas is not None:
            if tipas in range(1, 7):
                self.gaminio_skaiciuokle.ivesti_montavima(tipas)
                messagebox.showinfo("Pranešimas", "Montavimas pridėtas sėkmingai!")
            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingai. Bandykite dar kartą.")

    def prideti_pristatyma(self):
        tipas = simpledialog.askinteger("Pristatymo tipas",
                                        "Pasirinkite pristatymo tipą:\n1-Standartinis pristatymas, 2-Pristatymas "
                                        "Neringoje")
        if tipas is not None:
            if tipas == 1 or tipas == 2:
                self.gaminio_skaiciuokle.ivesti_pristatyma(tipas)
                messagebox.showinfo("Pranešimas", "Pristatymas pridėtas sėkmingai!")
            else:
                messagebox.showinfo("Klaida", "Įvedėte neteisingai. Bandykite dar kartą.")

    def apskaiciuoti_kaina(self):
        kaina = self.gaminio_skaiciuokle.gauti_gaminio_kaina()
        self.rezultatai_text.delete(1.0, tk.END)
        self.rezultatai_text.insert(tk.END, f"Galutinė gaminio kaina: {kaina} €")


if __name__ == "__main__":
    app = GaminioSkaiciuokleApp()
    app.mainloop()
