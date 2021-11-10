from ast import literal_eval as la


class Operand:
    def __init__(self) -> None:
        pass


class Interpreter:
    def __init__(self) -> None:
        self.buffer = []
        self.keys = {
            "string": str(),
            "integer": int(),
            "float": float()
        }
        self.var = {
            "pi": 3.14
        }

    def parse(self, file):
        with open(file, 'r') as fp:
            self.buffer = fp.read().splitlines()

    def error_check(self):
        try:
            if "#Deklarasi" not in self.buffer:
                raise SyntaxError("Harus mengetik #Deklarasi di baris pertama")
            if "#Intruksi" not in self.buffer:
                raise SyntaxError(
                    "Harus mengetik #Intruksi untuk memisahkan deklarasi")
            return True
        except Exception as e:
            print(e)
            return False

    def run(self):
        if self.error_check():
            for lines in self.buffer:
                if "=" in lines:
                    keys = lines.replace(" ", "").split("=")
                    if keys in ["+", "-", "*", "/", "%"]:
                        pass
                    else:
                        try:
                            self.var[keys[0]] = la(keys[1])
                        except KeyError as e:
                            print(e, "Variabel belum dideklarasikan")
                else:
                    keys = lines.split(" ")
                    if keys[0] == "cetak":
                        print(keys[1])
                    elif keys[0] == "input":
                        self.var[keys[1]] = input()
                    elif keys[0] == "tipe":
                        print(type(keys[1]))
                    else:
                        buffer_type = None
                        try:
                            var_type = keys[0]
                            buffer_type = self.keys[var_type]
                            self.var[keys[1]] = buffer_type
                        except IndexError as e:
                            # Bukan deklarasi
                            pass
                        except KeyError as e:
                            pass
                        # print(keys)
        # print(self.var)


def main():
    file = "TestCase/Case1.txt"
    I = Interpreter()
    I.parse(file)
    I.run()


if __name__ == "__main__":
    main()
