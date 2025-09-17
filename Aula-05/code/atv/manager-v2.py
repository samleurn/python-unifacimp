import os
import json


class Modules:
    def __init__(self): ...
    def format_json(self, arr):
        return json.dumps(arr, indent=4)

    def cls(self):
        return os.system("cls")


estoque = []


class Server:
    _code = 0

    def __init__(self):
        m = Modules()
        self._format_json = m.format_json

    def add(self):

        try:
            Server._code += 1

            obj = self.model()

            atr = None
            status = None

            for key, value in obj.items():
                if key == "code":
                    atr = Server._code
                    print(f'Produto {atr}')
                else:
                    inpt = input(f"{key}: ")
                    if inpt == "":
                        if value == str:
                            atr = f"None {Server._code}"
                        elif value == int or value == float:
                            atr = 0
                    else:
                        atr = value(inpt)
                obj[key] = atr

            code = obj["code"]
            nome = obj["nome"]
            preco = obj["preco"]
            quantidade = obj["quantidade"]

            p = Product(code, nome, preco, quantidade)
            obj = p.create_obj()
            estoque.append(obj)

            status = {"status": "200"}

        except:
            status = {"status": "500"}

        return status

    def remove(self, inpt_code):
        res_search = self.search(inpt_code)
        sts = res_search["status"]

        status = None

        if sts == "200":
            index = res_search["index"]

            print(estoque[index])

            print("Deseja remover?\n 1 - Sim\n 2 - Não\n")
            selc = input("Digite uma opção: ")

            if selc == "1":
                del estoque[index]
                status = {"status": "200"}

            if selc == "2":
                status = {"status": "302"}

        elif sts == "302":
            status = {"status": "302", "action": "break"}

        elif sts == "404":
            status = res_search

        return status

    def update(self, inpt_code):
        res_search = self.search(inpt_code)
        sts = res_search["status"]

        status = None
        if sts == "200":
            index = res_search["index"]
            obj = estoque[index]

            for key, value in obj.items():
                if key == "code":
                    print(self._format_json(obj))
                else:
                    inpt = input(f"{key}: ")

                    if inpt == "":
                        atr = value
                    else:
                        if isinstance(value, float):
                            atr = float(inpt)
                        elif isinstance(value, int):
                            atr = int(inpt)
                        elif isinstance(value, str):
                            atr = str(inpt)
                        else:
                            status = {"status": "400"}
                    obj[key] = atr

            status = {"status": "200"}
        else:
            status = {"status": sts}

        return status

    def write(self):
        return self._format_json(estoque)

    def search(self, inpt):

        status = None

        if inpt == "" or inpt == "0":
            status = {"status": "302"}
        elif isinstance(int(inpt), int):
            for i, obj in enumerate(estoque, start=0):
                if obj["code"] == int(inpt):
                    status = {"status": "200", "index": i}
        else:
            status = {"status": "404"}

        return status

    def model(self):
        obj = {"code": int, "nome": str, "preco": float, "quantidade": int}
        return obj


class Product:
    _code = 0

    def __init__(self, code, nome, preco, quantidade):
        self._code = code
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def create_obj(self):
        obj = {
            "code": self._code,
            "nome": self._nome,
            "preco": self._preco,
            "quantidade": self._quantidade,
        }
        return obj


class Interface:
    def __init__(self):
        m = Modules()
        s = Server()

        self._format_json = m.format_json
        self._cls = m.cls

        self._add = s.add
        self._write = s.write
        self._update = s.update
        self._remove = s.remove
        self._model = s.model

        while True:
            self._cls()

            print("Manager\n")
            print(
                "0 - Sair\n"
                "1 - Adicionar\n"
                "2 - Listar\n"
                "3 - Remover\n"
                "4 - Atualizar\n"
            )

            opt = input("Digite um opção: ")

            if opt == "0":
                break
            if opt == "1":
                self.add_page()
            if opt == "2":
                self.write_page()
            if opt == "3":
                self.remove_page()
            if opt == "4":
                self.update_page()

    def add_page(self):
        self._cls()

        print("Manager\n")
        print("Insira os seguintes atributos:\n")

        self._add()

        input()

    def write_page(self):
        self._cls()

        print("Manager\n")
        print("Insira os seguintes atributos:\n")

        db = self._write()

        print("Estoque")
        print(db)

        input()

    def remove_page(self):
        self._cls()

        print("Manager\n")
        print("Remover:\n" "0 - Voltar\n")

        inpt_code = input("Insira o codigo: ")

        status = self._remove(inpt_code)
        code = status["status"]

        if code == "200":
            print("Elemento deletado")
        elif code == "302":
            print("Voltando")

        input()

    def update_page(self):
        self._cls()

        print("Manager\n")
        print("Alterar:\n" "0 - Voltar\n")

        inpt_code = input("Insira o codigo: ")

        status = self._update(inpt_code)
        code = status["status"]

        if code == "200":
            print("Elemento Alterado")
        elif code == "302":
            print("Voltando")

        input()


Interface()
