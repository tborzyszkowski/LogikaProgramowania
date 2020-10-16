class Szyfr:

    def __init__(self, nazwa_oryginalna, nazwa_szyfr):
        self.oryginal = nazwa_oryginalna
        self.szyfr = nazwa_szyfr

    def szyfruj(self):
        f_oryginal = open(self.oryginal, 'r')
        lines = f_oryginal.readlines()
        out_lines = []
        for line in lines:
            out_lines.append("")
            for znak in line:
                if znak == "\n":
                    out_lines[len(out_lines) - 1] += znak
                else:
                    out_lines[len(out_lines)-1] += chr(ord(znak[0])+2)
        f_oryginal.close()
        print(out_lines)
        f_szyfr = open(self.szyfr, 'w')
        for line in out_lines:
            f_szyfr.write(line)
        f_szyfr.close()

    def odszyfruj(self):
        pass


szyfr = Szyfr("plik.txt", "szyfr.txt")
szyfr.szyfruj()
szyfr.odszyfruj()