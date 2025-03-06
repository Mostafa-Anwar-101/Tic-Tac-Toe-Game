class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name: ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use only letters.")

    def choose_symbol(self, other_symbol=None):
        while True:
            symbol = input("Enter your symbol (one letter only): ")
            if symbol.isalpha() and len(symbol) == 1:
                symbol = symbol.upper()
                if other_symbol and symbol == other_symbol:
                    print(f"Symbol '{symbol}' is already taken. Please choose a different symbol.")
                else:
                    self.symbol = symbol
                    break
            else:
                print("Invalid symbol. Please use one letter.")