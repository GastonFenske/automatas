string = 'bbbba'

def proof(string: str) -> bool:
    for c in string:
        if c == 'a' or c =='c':
            pass
        else:
            return False
    return True

if __name__ == '__main__':
    proof = proof(string=string)
    if proof:
        print(f"La cadena: [{string}] esta bien ")
    else:
        print(f"La cadena: [{string}] esta mal ")

    
