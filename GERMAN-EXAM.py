import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# =========================
# SUONI (compatibili)
# =========================
try:
    import winsound
    def suono_corretto():
        winsound.Beep(1000, 200)

    def suono_sbagliato():
        winsound.Beep(400, 400)
except:
    def suono_corretto():
        root.bell()

    def suono_sbagliato():
        root.bell()

# =========================
# VERBI
# =========================
verbi = {
    "andare": ("gehen", "ging", "ist gegangen"),
    "essere": ("sein", "war", "ist gewesen"),
    "avere": ("haben", "hatte", "hat gehabt"),
    "diventare": ("werden", "wurde", "ist geworden"),
    "venire": ("kommen", "kam", "ist gekommen"),
    "vedere": ("sehen", "sah", "hat gesehen"),
    "dare": ("geben", "gab", "hat gegeben"),
    "prendere": ("nehmen", "nahm", "hat genommen"),
    "mangiare": ("essen", "aß", "hat gegessen"),
    "bere": ("trinken", "trank", "hat getrunken"),
    "parlare": ("sprechen", "sprach", "hat gesprochen"),
    "leggere": ("lesen", "las", "hat gelesen"),
    "scrivere": ("schreiben", "schrieb", "hat geschrieben"),
    "dormire": ("schlafen", "schlief", "hat geschlafen"),
    "correre": ("laufen", "lief", "ist gelaufen"),
    "trovare": ("finden", "fand", "hat gefunden"),
    "rimanere": ("bleiben", "blieb", "ist geblieben"),
    "chiamare": ("rufen", "rief", "hat gerufen"),
    "aiutare": ("helfen", "half", "hat geholfen"),
    "pensare": ("denken", "dachte", "hat gedacht"),
    "sapere": ("wissen", "wusste", "hat gewusst"),
    "conoscere": ("kennen", "kannte", "hat gekannt"),
    "portare": ("tragen", "trug", "hat getragen"),
    "cadere": ("fallen", "fiel", "ist gefallen"),
    "iniziare": ("beginnen", "begann", "hat begonnen"),
    "vincere": ("gewinnen", "gewann", "hat gewonnen"),
    "perdere": ("verlieren", "verlor", "hat verloren"),
    "decidere": ("entscheiden", "entschied", "hat entschieden"),
    "guidare": ("fahren", "fuhr", "ist gefahren"),
    "incontrare": ("treffen", "traf", "hat getroffen"),
    "stare (in piedi)": ("stehen", "stand", "hat gestanden"),
    "sedersi": ("sitzen", "saß", "hat gesessen"),
    "mentire": ("lügen", "log", "hat gelogen"),
    "cantare": ("singen", "sang", "hat gesungen"),
    "nuotare": ("schwimmen", "schwamm", "ist geschwommen"),
    "tagliare": ("schneiden", "schnitt", "hat geschnitten"),
    "offrire": ("bieten", "bot", "hat geboten"),
    "chiudere": ("schließen", "schloss", "hat geschlossen"),
    "aprire": ("öffnen", "öffnete", "hat geöffnet"),
    "comprare": ("kaufen", "kaufte", "hat gekauft"),
    "bruciare": ("brennen", "brannte", "hat gebrannt"),
    "portare (trasporto)": ("bringen", "brachte", "hat gebracht"),
    "tenere": ("halten", "hielt", "hat gehalten"),
    "lasciare": ("lassen", "ließ", "hat gelassen"),
    "chiamarsi": ("heißen", "hieß", "hat geheißen"),
    "salire": ("steigen", "stieg", "ist gestiegen"),
    "affondare": ("sinken", "sank", "ist gesunken"),
    "tirare": ("ziehen", "zog", "hat gezogen"),
    "crescere": ("wachsen", "wuchs", "ist gewachsen")
}

lista_verbi = list(verbi.keys())
random.shuffle(lista_verbi)

indice = 0
punti = 0
totale = len(lista_verbi)

# =========================
# FUNZIONI
# =========================
def aggiorna_progress():
    progress["value"] = (indice / totale) * 100
    punteggio_label.config(text=f"Punteggio: {punti}/{totale}")

def animazione_flash(colore):
    original = root["bg"]
    root.config(bg=colore)
    root.after(200, lambda: root.config(bg=original))

def nuova_domanda():
    if indice < totale:
        verbo_label.config(text=lista_verbi[indice])
        entry_inf.delete(0, tk.END)
        entry_praet.delete(0, tk.END)
        entry_perf.delete(0, tk.END)
        risultato_label.config(text="")
        aggiorna_progress()
    else:
        mostra_risultato()

def controlla():
    global indice, punti

    italiano = lista_verbi[indice]
    infinito, praet, perf = verbi[italiano]

    if (entry_inf.get() == infinito and
        entry_praet.get() == praet and
        entry_perf.get() == perf):
        punti += 1
        risultato_label.config(text="✅ CORRETTO!", fg="#00ff88")
        suono_corretto()
        animazione_flash("#003300")
    else:
        risultato_label.config(
            text=f"❌ {infinito} | {praet} | {perf}",
            fg="#ff4444"
        )
        suono_sbagliato()
        animazione_flash("#330000")

    indice += 1
    root.after(1200, nuova_domanda)

def mostra_risultato():
    percentuale = (punti / totale) * 100

    if percentuale == 100:
        livello = "🏆 LEGGENDARIO"
    elif percentuale >= 80:
        livello = "🥇 ESPERTO"
    elif percentuale >= 60:
        livello = "🥈 BUONO"
    else:
        livello = "📚 STUDIA DI PIÙ"

    messagebox.showinfo(
        "RISULTATO FINALE",
        f"Punteggio: {punti}/{totale}\n"
        f"Percentuale: {round(percentuale,2)}%\n\n"
        f"{livello}\n\n"
        "Creato da Astra (Alex) 🚀"
    )

    root.quit()

# =========================
# FINESTRA PRINCIPALE
# =========================
root = tk.Tk()
root.title("QUIZ VERBI TEDESCHI - IMPERIAL EDITION")
root.geometry("550x600")
root.config(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", thickness=20)

# =========================
# LOGO PERSONALIZZATO
# =========================
try:
    logo_img = tk.PhotoImage(file="logo.png")
    logo = tk.Label(root, image=logo_img, bg="#121212")
    logo.pack(pady=10)
except:
    pass  # Se non trova il logo, continua senza

titolo = tk.Label(
    root,
    text="QUIZ VERBI TEDESCHI 🇩🇪",
    font=("Helvetica", 20, "bold"),
    bg="#121212",
    fg="#00ccff"
)
titolo.pack(pady=10)

verbo_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 24, "bold"),
    bg="#121212",
    fg="white"
)
verbo_label.pack(pady=15)

entry_inf = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_inf.pack(pady=5)

entry_praet = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_praet.pack(pady=5)

entry_perf = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry_perf.pack(pady=5)

btn = tk.Button(
    root,
    text="Controlla",
    font=("Helvetica", 14, "bold"),
    bg="#00ccff",
    fg="black",
    command=controlla
)
btn.pack(pady=20)

risultato_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 14),
    bg="#121212"
)
risultato_label.pack()

progress = ttk.Progressbar(root, length=400)
progress.pack(pady=20)

punteggio_label = tk.Label(
    root,
    text="Punteggio: 0/0",
    font=("Helvetica", 12),
    bg="#121212",
    fg="white"
)
punteggio_label.pack()

nuova_domanda()

root.mainloop()
