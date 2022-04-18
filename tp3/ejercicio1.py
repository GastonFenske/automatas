from estadosej1 import estados
 
class Automata:

    def __init__(self, string: str) -> None:
        self.string = string

    def proof(self) -> bool:
        correct = False
        index = 0
        accept_states = [1, 2]
        for c in self.string:
            try:
                index = estados[index][c]
            except KeyError:
                """Aca solo entra si esa opcion no esta disponible en el estado actual"""
                correct = False
                return correct
            if index in accept_states:
                """Aca entra si se llego al estado de aceptacion"""
                correct = True
        return correct

if __name__ == '__main__':
    automata = Automata(string='aaaaa')
    proof = automata.proof()
    if proof:
        print(f"La cadena: [{automata.string}] esta bien ")
    else:
        print(f"La cadena: [{automata.string}] esta mal ")
