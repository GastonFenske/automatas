    

class Utils:        

    @staticmethod
    def input_function(*args) -> dict:
        inputs: list = {}
        for arg in args:
            user_input = input(f"Ingrese {arg}: ")
            inputs[arg] = user_input
        return inputs