
class Automata:

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
            if c == 'a' or c =='c':
                pass
            else:
                return False
        return True

if __name__ == '__main__':
    automata = Automata(string='aacc')
    proof = automata.proof()
    if proof:
        print(f"La cadena: [{automata.string}] esta bien ")
    else:
        print(f"La cadena: [{automata.string}] esta mal ")

    
