from estados import estados
 
class Automata:

    __alphabet = ['a', 'b', None]

    def __init__(self, string: str) -> None:
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, data):
        self.__string = data

    def proof(self) -> bool:
        for c in self.string:
            if c not in self.__alphabet:
                return False

        index = 0
        for c in self.string:
            try:
                index = estados[index][c]
            except KeyError:
                """Aca solo entra si esa opcion no esta disponible en el estado actual"""
                return False
            if index == 3:
                """Aca entra si se llego al estado de aceptacion 3"""
                return True
            if self.string.index(c) + 1 == len(self.string):
                """Aca entra a la ultima letra de la cadena"""
                c = None
        return False


if __name__ == '__main__':
    automata = Automata(string='aab')
    proof = automata.proof()
    if proof:
        print(f"La cadena: [{automata.string}] esta bien ")
    else:
        print(f"La cadena: [{automata.string}] esta mal ")
