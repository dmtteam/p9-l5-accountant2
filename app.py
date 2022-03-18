
from brain2 import Magazyn
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def show_index_page():
    rezultat_saldo =""
    rezultat_zakup =""
    rezultat_sprzedaz =""

    magazyn=Magazyn()
    magazyn.wczytaj("in.txt")

    if request.form.get("akcja"):
        if request.form["akcja"] == "saldo":
            status, rezultat_saldo=magazyn.saldo(int(request.form["wartosc"]), request.form["komentarz"])
        magazyn.zapisz("in.txt")

    if request.form.get("akcja"):
        if request.form["akcja"] == "zakup":
            status, rezultat_zakup=magazyn.zakup(
                                                str(request.form["produkt"]),
                                                int(request.form["cena"]),
                                                int(request.form["ilosc"])
                                                )
        magazyn.zapisz("in.txt")

    if request.form.get("akcja"):
        if request.form["akcja"] == "sprzedaz":
            status, rezultat_sprzedaz=magazyn.sprzedaz(
                                                str(request.form["produkt"]),
                                                int(request.form["cena"]),
                                                int(request.form["ilosc"])
                                                )
        magazyn.zapisz("in.txt")

# magazyn.wczytaj("in.txt")
# print(magazyn.magazyn)

    magazyn.zapisz("in.txt")
    return render_template("index.html", stan_konta=magazyn.stan_konta,
                                        magazyn=magazyn.magazyn, historia=magazyn.historia, request=request,
                                        rezultat_saldo=rezultat_saldo, rezultat_zakup=rezultat_zakup,
                                        rezultat_sprzedaz=rezultat_sprzedaz
                           )

@app.route("/history.html", methods=["GET", "POST"])
def show_history_page():
    rezultat_historia_zakresy = ""
    magazyn=Magazyn()
    magazyn.wczytaj("in.txt")
    historia=magazyn.historia

    if request.form.get("akcja"):
        if request.form["akcja"] == "historia_zakresy":
            historia=historia[int(request.form["start"]):int(request.form["end"])+1]

    return render_template("history.html", magazyn=magazyn.magazyn,
                           historia=historia, request=request,
                           rezultat_historia_zakresy=rezultat_historia_zakresy
                           )


app.run(debug=True)



