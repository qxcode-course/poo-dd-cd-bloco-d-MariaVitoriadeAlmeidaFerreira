class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number
    
    def isValid(self) -> bool:
        valid: str = "1234567890()."
        for c in self.__number:
            if c not in valid:
                return False
        return True
    
    def __str__(self) -> str:
        return f"{self.__id}:{self.__number}"
    
class Contato:
    def __init__(self, name: str):
        self.__name: str = name
        self.__fone: list[Fone] = []
        self.__favorito: bool = False

    def addFone(self, id: str, number: str) -> None:
        tel = Fone(id, number)

        if tel.isValid():
            self.__fone.append(tel)
        else:
            raise Exception ("fail: telefone invalido")
        
    def rmFone(self, index: int):
        if index < len(self.__fone):

            self.__fone.pop(index)

    def toogleFone(self) -> None:
        if self.__favorito == False:
            self.__favorito = True
        else:
            self.__favorito = False
        
    def isFavorito(self) -> bool:
        return self.__favorito

    def getFone(self) -> list[Fone]:
        return self.__fone
    
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> None:
        self.__name = name 

    def __str__(self) -> str:
        fones = ", ".join([str(x) for x in self.__fone])

        return f"- {self.__name} [{fones}]"
    
class Agenda:
    def __init__(self):
        self.__contato: list[Contato] = []

    def __acharPosDoNome(self, name: str) -> int:
        for i in range (0, len(self.__contato)-1):
            if name == self.__contato[i].getName:
                return i
        return -1
    
    def addcontato(self, name: str, fones: list[Fone]) -> None:
        index = self.__acharPosDoNome(name)

        if index != -1:
            cont_existe = self.__contato[index]
            for f in fones:
                if f.isValid():
                    cont_existe.addFone(f.getId(), f.getNumber())
            
        else:
            contato_novo = Contato(name)
            for f in fones:
                if f.isValid():
                    contato_novo.addFone(f.getId(), f.getNumber())
            self.__contato.append(contato_novo)
            self.__contato.sort(key=lambda c: c.getName())
        
    #def getContato(self):


    def __str__(self) -> str:
        return f"\n".join(str(contato) for contato in self.__contato)

def main():
    agenda = Agenda()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "add":
            name = args[1]
            fones = []
            for f in args[2:]:
                id, num = f.split(":")
                fones.append(Fone(id, num))
            agenda.addcontato(name, fones)
        elif args[0] == "show":
            print(agenda)
        

main()

