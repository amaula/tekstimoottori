# coding: utf-8
"""
"""
ohjelma = {
    "mene_huoneeseen_2": {
        "tarina": "saavut huoneeseen kaksi huone on keittiö näet oven joka vie ruoka saliin",
        "vaihtoehdot": [("mene ruoka saliin", None),
                        ("poistu huoneesta kaksi", None),
                        ("", None)]
    },
    "mene_huoneeseen_1": {
        "tarina": "saavut ensimmäiseen huoneeseen näet siellä tauluja linnan herttuoista.",
        "vaihtoehdot": [("mene takaisin linnan porteille", "mene_yksin_tutkimaan_linnaa"),
                        ("mene huoneeseen 2", "mene_huoneeseen_2"),
                        ("mene huoneeseen 3", "mene_huoneeseen_3")]
    },
    "heita_kivi_huoneeseen_3": {
        "tarina": "Otat maasta kiven ja heität huoneeseen. Kivi kolahtaa seinään, putoaa lattialle ja vierii\n"
                  "eteenpäin. Vierintä pysähtyy pehmään tömähdykseen ja tulee taas hiljaista.",
        "vaihtoehdot": "mene_huoneeseen_3"
    },
    "kavele_huoneeseen_3": {
        "tarina": "Päätät kulkea kolmannen huoneen läpi kohti huoneen takana näkyvää vaimeaa valoa.\n"
                  "Kävelet varovasti eteenpäin, samalla tunnustellen käsilläsi mahdollisia esteitä.\n"
                  "Yhtäkkiä osut lattiassa olevaan koloon, kompastut ja lyöt polvesi. Polveesi sattuu\n"
                  "joten päätät lopettaa tutkimusmatkasi ja palata kotiin laastaroitavaksi.",
        "vaihtoehdot": None
    },
    "mene_huoneeseen_3": {
        "tarina": "Otat kiinni kolmannen huoneen ovenkahvasta ja vedät varovasti. \n"
                  "Ovi pistää vastaan mutta aukeaa viimein ilkeästi narahtaen. Edessäsi\n"
                  "aukeava huone on täysin pimeä etkä näe yhtään eteesi. Huoneessa leijuu \n"
                  "lievä homeen tuoksu joka viittaa siihen että huone on ollut pitkään \n"
                  "käyttämättä. Astut varovasti huoneen sisäpuolelle ja tunnet kuinka lattia\n"
                  "narisee pahaenteisesti jalkojesi alla. Näet huoneen toisessa päässä vaimeaa\n"
                  "valonkajoa.",
        "vaihtoehdot": [("Suuntaat varovasti kävellen kohti valonkajoa hapuillen käsilläsi pimeyttä.",
                         "kavele_huoneeseen_3"),
                        ("Otat maasta kiven ja heität huoneeseen", "heita_kivi_huoneeseen_3"),
                        ("Mielestäni huone näyttää liian vaaralliselta ja peräännyt takaisin linnan portille.",
                         "mene_yksin_tutkimaan_linnaa")]
    },
    "mene_yksin_tutkimaan_linnaa": {
        "tarina": "menet yksin tutkimaan linnaa ja huomaat kolme ränsistynyttä ovea\n"
                  "jotka vievät eri huoneisiin.",
        "vaihtoehdot": [("mene huoneeseen 1", "mene_huoneeseen_1"),
                        ("mene huoneeseen 2", "mene_huoneeseen_2"),
                        ("mene huoneeseen 3", "mene_huoneeseen_3")]
    },
    "soita_kavereita": {
        "tarina": "soitat jokaiselle kaverillesi mutta kaikilla on muita menoja.\n"
                  "Päätät että et mene linnaan ilman kavereita ja lähdet kotiin.",
        "vaihtoehdot": None
    },
    "soita_isasi_mukaan": {
        "tarina": "Otat puhelimen taskustasi ja soitat isällesi. Isäsi vastaa puhelimeen.\n"
                  "Kerrot että näit kukkulan laella kiinnostavan näköisen linnan ja\n"
                  "haluaisit mennä tutkimaan sitä. Odotat innostuneena, mutta isä vastaakin että:\n'"
                  "Hylätty linna? Liian hurjaa! Et saa mennä! Nyt heti kotiin!'\n"
                  "Mutiset vastaan mutta toeat että ehkä on parempi olla menemättä yksin\n"
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
