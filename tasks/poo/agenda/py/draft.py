class Fone:
    def __init__(self, id: str, number: str):
        self.id: str = id
        self.number: str = number

    def getId(self) -> str:
        return self.id
    
    def getNumber(self) -> str:
        return self.number
    
    