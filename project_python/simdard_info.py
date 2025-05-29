class Simcard:

    def __init__(self,id,numbers,operator,price,charge,owner):
        self.id=id
        self.numbers=numbers
        self.operator=operator
        self.price = price
        self.charge = charge
        self.owner = owner

    def save_simcard_info(self):
        print(f"{self.id}-{self.numbers}-{self.operator}-{self.price}-{self.charge}-{self.owner} saved")