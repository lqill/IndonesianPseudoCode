from ast import literal_eval as la


class Var:
    def __init__(self, type, value=None) -> None:
        self.value = value
        keys = {
            "String": str(),
            "Integer": int(),
            "Float": float(),
            "Benar": True,
            "Salah": False,
            "Bool": bool()
        }
        self.type = keys[type]

    def set(self, value):
        if type(value) == type(self.type):
            self.value = value
        else:
            self.value = self.check(value)

    def check(self, value):
        if self.type == int():
            return int(value)
        elif self.type == float():
            return float(value)
        elif self.type == bool():
            return bool(value)
        elif self.type == str():
            raise TypeError(value)


class Interpreter:
    def __init__(self) -> None:
        self.lines = []
        self.output = ""
        self.keys = {
            "String": str(),
            "Integer": int(),
            "Float": float(),
            "Benar": True,
            "Salah": False,
            "Bool": bool()
        }
        self.var = {
            "PI": Var("Float", 3.14)
        }
        self.modul = {
            "Deklarasi": [],
            "Intruksi": []
        }

    def parse(self, text: str):
        self.lines = text.splitlines()

    def open(self, file):
        with open(file, 'r') as fp:
            self.lines = fp.read().splitlines()

    def error_check(self):
        try:
            if "#Deklarasi" not in self.lines:
                raise SyntaxError("Harus mengetik #Deklarasi di baris pertama")
            if "#Intruksi" not in self.lines:
                raise SyntaxError(
                    "Harus mengetik #Intruksi untuk memisahkan deklarasi")
            return True
        except Exception as e:
            print(e)
            return False

    def strip(self):
        if self.error_check():
            for idx, line in enumerate(self.lines):
                if line == "":
                    continue
                if line.replace(" ", "")[0] == "#":
                    try:
                        modul_name = line.split(" ")[0].replace("#", "")
                    except KeyError as e:
                        pass
                else:
                    self.modul[modul_name].append([idx+1, line])

    def process(self, idx, line):
        if "=" in line:
            keys = line.replace(" ", "").split("=")
            if any(c in keys[1] for c in ["+", "-", "*", "/", "%"]):
                pass
            else:
                try:
                    _ = self.var[keys[0]]
                    self.var[keys[0]].set(eval(keys[1]))
                except KeyError as e:
                    print(
                        f"ERROR Baris ke-{idx} : Variabel {e} belum dideklarasikan")
                    self.output += f"ERROR Baris ke-{idx} : Variabel {e} belum dideklarasikan\n"
                    error = True
                    raise NameError()
                except TypeError as e:
                    print(
                        f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}")
                    self.output += f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}\n"
                    error = True
                    raise TypeError()
            # print(keys)
        else:
            keys = line.split(" ")
            if keys[-1] == "MAKA":
                # this is for the if/else,for, while
                if keys[0] == "JIKA":
                    self.state = "ifelse"
                    print(keys)
                elif keys[0] == "UNTUK":
                    self.state = "for"
                elif keys[0] == "ULANGJIKA":
                    self.state = "while"
            if keys[0] == "SELESAI":
                # TODO ENDIF ENDFOR ENDWHILE
                pass
            if keys[0] == "CETAK":
                print(self.var[keys[1]].value)
                self.output += str(self.var[keys[1]].value)+"\n"
            elif keys[0] == "INPUT":
                # TODO:TAMBAHI TEXT BOX UNTUK INPUT
                self.var[keys[1]].value = input()
            elif keys[0] == "TIPE":
                print(self.var[keys[1]].type)
                self.output += str(self.var[keys[1]].type)+"\n"
            else:
                try:
                    var_type = keys[0]
                    self.var[keys[1]] = Var(var_type)
                except:
                    print(
                        f"ERROR Baris ke-{idx} : Salah pengetikan atau menyalahi aturan syntax")
                    self.output += f"ERROR Baris ke-{idx} : Salah pengetikan atau menyalahi aturan syntax"
                    error = True
                    raise SyntaxError()

    def run(self, text):
        self.output = ""
        self.condition = False
        self.parse(text)
        self.strip()
        error = False
        self.state = "normal"
        for mode in [self.modul["DEKLARASI"], self.modul["INTRUKSI"]]:
            for parsed in mode:
                if not error:
                    idx = parsed[0]
                    line = parsed[1]
                    # print(idx, line)
                    if self.state == "normal":
                        self.process(idx, line)
                    elif self.state == "ifelse":
                        pass
                    elif self.state == "for":
                        pass
                    elif self.state == "while":
                        loop = []
                        for i in mode[idx-mode[0][0]:]:
                            if i[1] == "SELESAI":
                                while True:
                                    break
                                    # for j in

    # Logic

    def ifelse(self):
        pass

    def for_loop(self):
        pass

    def while_loop(self):
        pass


def main():
    file = "TestCase/case1.txt"
    I = Interpreter()
    with open(file, 'r') as fp:
        I.run(fp.read())


if __name__ == "__main__":
    main()
