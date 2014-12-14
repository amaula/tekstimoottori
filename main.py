# coding: utf-8
"""
"""
import sys

vaihtoehtokirjaimet = [chr(ord('a') + i) for i in range(10)]


def aja(ohjelma):
    tila = ohjelma["alkutila"]
    try:
        while True:
            tarina = tila["tarina"]
            vaihtoehdot = tila["vaihtoehdot"]
            print("Tilanne:\n%s" % tarina)

            if vaihtoehdot is None:
                print("Peli loppui!")
                break

            elif isinstance(vaihtoehdot, basestring):
                print("\nSiirryt suoraan toiseen tilanteeseen:")
                tila = ohjelma[vaihtoehdot]

            else:
                print("\nVaihtoehdot:")
                try:
                    for index, vaihtoehto in enumerate(vaihtoehdot):
                        kirjain = vaihtoehtokirjaimet[index]
                        print("%s: %s" % (kirjain, vaihtoehto[0]))
                    input = raw_input("Mitä haluat tehdä? ")
                    newindex = vaihtoehtokirjaimet.index(input)
                    if newindex >= len(vaihtoehdot):
                        raise StandardError()
                except StandardError:
                    print("Tuntematon syöte, valitse joku arvoista: %s" %
                          ', '.join(vaihtoehtokirjaimet[0:len(vaihtoehdot)]))
                    continue

                tila = ohjelma[vaihtoehdot[newindex][1]]
                print "\n" * 100

    except KeyboardInterrupt:
        print("\n\nKeskeytit pelin.\n")


def main():
    try:
        ohjelman_nimi = sys.argv[1]
        mod = __import__(ohjelman_nimi, fromlist=[''])
        aja(mod.ohjelma)
    except IndexError:
        print("Käyttö: main.py <tehtävä>")
    except ImportError:
        print("Tehtävää '%s' ei löydy!" % sys.argv[1])

if __name__ == "__main__":
    main()