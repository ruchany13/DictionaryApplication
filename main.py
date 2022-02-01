#The application can use with this file.
# TODO you can use design pattern.

from database import Dictionary

class Main(Dictionary):
    def __init__(self, database_name, table_name,word, type, ):
        super().__init__(database_name, table_name)
        self.word = word
        self.type = type
        self.mean = None

    
    def controller(self):
        data = self.read_sp(self.word, self.type)
        if data == []:
            return True
        else:
            return False

if __name__ == '__main__':
    print("Welcome!")
    while True: 
        word = input("Word:")
        type = input("Type:")
        program = Main("sozluk.sql", "words" ,word, type)
        if program.controller():
            mean = input("Turkish:")
            word = (word, mean, type, "0", "0", "0", "0", "0")
            program.add(word)

        elif word == "q":
            break
        else:
            print("'{}' is already exist!".format(word))
            program.update("Ask+1", "Ask", word, type)
            pass
