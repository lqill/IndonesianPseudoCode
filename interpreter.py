from ast import literal_eval as la
from enum import Enum


class InterpreterState(Enum):
    NORMAL = "normal"
    IFELSE = "ifelse"
    FOR = "for"
    WHILE = "while"


class VarType(Enum):
    STRING = str
    INTEGER = int
    FLOAT = float
    TRUE = bool
    FALSE = bool
    BOOL = bool
    LIST = list


class CustomError(Exception):
    pass


class Var:
    '''
    Class Var ini berfungsi sebagai memori penyimpanan satu variabel
    dengan inisiasi TIPE variabel dan VALUE variabel.
    '''

    def __init__(self, var_type, value=None) -> None:
        self.value = value
        self.type = VarType[var_type.upper()]

    def set(self, new_value):
        '''
        Set digunakan untuk mengisi value variabel dengan tipe yang sama dengan deklarasi variabel.
        Mengkonversi variabel apabila beda tipe dan bisa dikonversi.
        '''
        var_type = VarType(self.type)
        if type(new_value) == var_type.value:
            self.value = new_value
        elif type(new_value) == str:
            raise TypeError("Salah Type")
        else:
            self.value = var_type.value(new_value)


class Interpreter:
    '''
    Class Interpreter membaca pseudocode dan diproses dengan backend python.
    '''

    def __init__(self) -> None:
        self.lines = []
        self.output = ""
        self.keys = {
            "STRING": str(),
            "INTEGER": int(),
            "FLOAT": float(),
            "TRUE": True,
            "FALSE": False,
            "BOOL": bool(),
            "LIST": list()
        }
        self.var = {
            "PI": Var("FLOAT", 3.14)
        }
        self.modul = {
            "DEKLARASI": [],
            "INTRUKSI": []
        }
        self.state = InterpreterState.NORMAL

    def error_check(self):
        try:
            lowercase_lines = [line.lower() for line in self.lines]
            if "#deklarasi" not in lowercase_lines:
                raise CustomError("Harus mengetik #DEKLARASI di baris pertama")
            if "#intruksi" not in lowercase_lines:
                raise CustomError(
                    "Harus mengetik #INTRUKSI untuk memisahkan deklarasi")
            return True
        except Exception as e:
            print(e)
            return False

    def run_one_line(self, idx, line):
        '''
        Operasi satu baris dari pseudocode
        '''
        # TODO Too many if/elif(s), mau coba pakai dictionary
        keys = line.lower().split()

        if "=" in line and "==" not in line:  # Apabila ada = pada baris pseudocode yang artinya assignment
            keys = line.replace(" ", "").split("=")
            if any(c in keys[1] for c in ["+", "-", "*", "/", "%"]):
                pass  # TODO Buat Operasi bilangan matematika atau string
                try:
                    _ = keys[1].replace(" ", "").split("+")
                    self.var[keys[0]] = _
                except:
                    pass
            else:
                try:
                    _ = self.var[keys[0]]
                    self.var[keys[0]].set(eval(keys[1]))
                except KeyError as e:
                    print(
                        f"ERROR Baris ke-{idx} : Variabel {e} belum dideklarasikan")
                    self.output += f"ERROR Baris ke-{idx} : Variabel {e} belum dideklarasikan\n"
                    raise NameError()
                except TypeError as e:
                    print(
                        f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}")
                    self.output += f"ERROR Baris ke-{idx} : Variabel {keys[0]} bertipe {type(self.var[keys[0]].type)} sedangkan {e} bertipe {type(e.args[0])}\n"
                    raise TypeError()
        else:
            if keys[-1].upper() == "MAKA":
                self.handle_control_flow(keys, idx)
                # TODO Buat sistem if/else disini
            elif keys[0].upper() == "CETAK" and len(keys) == 2:
                print(self.var[keys[1]].value)
                self.output += str(self.var[keys[1]].value) + "\n"
            elif keys[0].upper() == "INPUT" and len(keys) == 2:
                self.var[keys[1]].value = input()
            elif keys[0].upper() == "TIPE" and len(keys) == 2:
                print(self.var[keys[1]].type)
                self.output += str(self.var[keys[1]].type) + "\n"
            else:
                try:
                    var_type, var_name = keys[0], keys[1]
                    self.var[var_name] = Var(var_type)
                except Exception:
                    print(
                        f"ERROR Baris ke-{idx}: Salah pengetikan atau menyalahi aturan syntax")
                    self.output += f"ERROR Baris ke-{idx}: Salah pengetikan atau menyalahi aturan syntax\n"
                    raise SyntaxError()

    def handle_control_flow(self, keys, idx):
        # TODO Buat JikaTidak (ELSE)
        if keys[0] == "JIKA":
            self.state = InterpreterState.IFELSE
        elif keys[0] == "UNTUK":
            self.state = InterpreterState.FOR
        elif keys[0] == "ULANGJIKA":
            self.state = InterpreterState.WHILE

    def run(self, text):
        self.output = ""
        self.lines = text.splitlines()
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
                    self.modul[modul_name.upper()].append([idx+1, line])
        error = False
        for mode in [self.modul["DEKLARASI"], self.modul["INTRUKSI"]]:
            for parsed in mode:
                if not error:
                    idx = parsed[0]
                    line = parsed[1]
                    if self.state == InterpreterState.NORMAL:
                        self.run_one_line(idx, line)
                    elif self.state == InterpreterState.IFELSE:
                        self.ifelse(idx, mode)
                    elif self.state == InterpreterState.FOR:
                        self.for_loop(idx, mode)
                    elif self.state == InterpreterState.WHILE:
                        self.while_loop(idx, mode)

    # Logic

    def ifelse(self, start_idx, lines):
        idx = start_idx + 1
        while True:
            line = lines[idx]
            if line == "SELESAI":
                break
            # Lakukan sesuatu dengan baris pseudocode if-else
            idx += 1

    def for_loop(self, start_idx, lines):
        idx = start_idx + 1
        while True:
            line = lines[idx]
            if line == "SELESAI":
                break
            # Lakukan sesuatu dengan baris pseudocode for
            idx += 1

    def while_loop(self, start_idx, lines):
        idx = start_idx + 1
        while True:
            line = lines[idx]
            if line == "SELESAI":
                break
            # Lakukan sesuatu dengan baris pseudocode
            idx += 1


def main():
    file = "TestCase/case2.txt"
    with open(file, 'r') as fp:
        I = Interpreter()
        I.run(fp.read())


if __name__ == "__main__":
    main()
    # var = Var("INTEGER", "12")
    # print("test")
    # print("test")
