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

    def run_old(self):
        output = ""
        error = False
        for mode in [self.modul["Deklarasi"], self.modul["Intruksi"]]:
            for parsed in mode:
                if not error:
                    idx = parsed[0]
                    line = parsed[1]
                    # print(idx, line)

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
                                output += f"ERROR Baris ke-{idx} : Variabel {e} belum dideklarasikan\n"
                                error = True
                                break
                            except TypeError as e:
                                print(
                                    f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}")
                                output += f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}\n"
                                error = True
                                break
                        # print(keys)
                    else:
                        keys = line.split(" ")
                        if keys[-1] == "Maka":
                            # this is for the loop and if/else
                            pass
                            if keys[0] == "Jika":
                                pass
                            elif keys[0] == "Untuk":
                                pass
                            elif keys[0] == "UlangJika":
                                pass
                        if keys[0] == "Cetak":
                            print(self.var[keys[1]].value)
                            output += str(self.var[keys[1]].value)+"\n"
                        elif keys[0] == "Input":
                            self.var[keys[1]].value = input()
                        elif keys[0] == "Tipe":
                            print(self.var[keys[1]].type)
                            output += str(self.var[keys[1]].type)+"\n"
                        else:
                            try:
                                var_type = keys[0]
                                self.var[keys[1]] = Var(var_type)
                            except:
                                print("error")
                                error = True
                                break
                e = 1
        return output

    def run(self, text):
        self.output = ""
        self.parse(text)
        self.strip()
        self.output = self.run_old()
        self.output += "\n\n\n\n\n"


def main():
    file = "TestCase/Case1.txt"
    I = Interpreter()
    I.parse(file)
    I.strip()
    I.run()


if __name__ == "__main__":
    main()
