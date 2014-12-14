# coding: utf-8
"""

"""

ohjelma = {
    "soita_kavereita": {
        "tarina": "soitat jokaiselle kaverillesi mutta kaikilla on muita menoja",
        "vaihtoehdot": [None]
    },
    "mene_yksin_tutkimaan_linnaa": {
        "tarina": "menet yksin tutkimaan linnaa ja huomaat kolme ränsistynyttä ovea jotka viävät eri huoneisiin",
        "vaihtoehdot": [("mene huoneeseen 1", None),
                        ("mene huoneeseen 2", None),
                        ("mene huoneeseen 3", None)]
    },
    "soita_isasi_mukaan": {
        "tarina": "Otat puhelimen taskustasi ja soitat isällesi. Isäsi vastaa puhelimeen. "
                  "Kerrot että näit kukkulan laella kiinnostavan näköisen linnan ja "
                  "haluaisit mennä tutkimaan sitä. Odotat innostuneena, mutta isä vastaakin että:\n'"
                  "Hylätty linna? Liian hurjaa! Et saa mennä! Nyt heti kotiin!'\n"
                  "Mutiset vastaan mutta toeat että ehkä on parempi olla menemättä yksin "
                  "epäilyttävän näköiseen linnaan.",
        "vaihtoehdot": None
    },
    "alkutila": {
        "tarina": "näet korkealla kukkulalla hylätyn linnan ja haluat mennä tutkimaan sitä",
        "vaihtoehdot": [("soita kavereita mukaan tutkimaan linnaa", "soita_kavereita"),
                        ("mene yksin tutkimaan linnaa", "mene_yksin_tutkimaan_linnaa"),
                        ("soita isäsi mukaan", "soita_isasi_mukaan")]
    }
}

def main():
    vaihtoehtokirjaimet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    tila = ohjelma["alkutila"]

    try:
        while True:
            tarina = tila["tarina"]
            vaihtoehdot = tila["vaihtoehdot"]
            print("\nTilanne:\n%s" % tarina)

            if vaihtoehdot is None:
                print("Peli loppui!")
                break
            print("\nVaihtoehdot:")
            for index, vaihtoehto in enumerate(vaihtoehdot):
                kirjain = vaihtoehtokirjaimet[index]
                print("%s: %s" % (kirjain, vaihtoehto[0]))
            input = raw_input("Mitä haluat tehdä? ")
            try:
                newindex = vaihtoehtokirjaimet.index(input)
            except ValueError:
                print("Tuntematon syöte, valitse joku arvoista: %s" % ', '.join(vaihtoehtokirjaimet))
                continue

            tila = ohjelma[vaihtoehdot[newindex][1]]

    except KeyboardInterrupt:
        print("\n\nKeskeytit pelin.\n")

if __name__ == "__main__":
    main()