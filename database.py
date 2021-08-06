import sqlite3 as sql



class Dictionary(object):

    def __init__(self, database_name, table_name):
        self.db = sql.Connection(database_name)
        self.im = self.db.cursor()
        self.data_all = []
        self.table_name = table_name


    def read_all(self):
        code = """SELECT * FROM {}""".format(self.table_name)
        self.im.execute(code)
        self.data_all = self.im.fetchall()
        return self.data_all


    def build_file(self):
        self.im.execute(
            "CREATE TABLE IF NOT EXISTS words (Word, Turkish, Type, Ask, Answer, Score, Repeat, General_Score)")


    def read_sp(self, word, type):
        code = """SELECT * FROM {} WHERE Word = "{}" AND Type = "{}" """.format(self.table_name, word, type)
        self.im.execute(code)
        data = self.im.fetchall()
        print(data)
        return data
        

    def print_all(self):
        all = self.read_all()
        for data in all:
            print(*data)
    
    def print_sp(self):
        pass

    def add(self, word_data):
    # word data ("word", "data")
        code = """INSERT INTO {} VALUES (?,?,?,?,?,?,?,?) """.format(self.table_name)
        self.im.execute(code, word_data)
        self.db.commit()

    def update(self, new_data, data_column, word1, type1):
        #new data = Score+1 / Score-1 / Other
        code = """UPDATE {} SET {} = {} WHERE word = "{}" AND Type = "{}" """.format(self.table_name, data_column,
                                                                                     new_data, word1, type1)
        self.im.execute(code)
        self.db.commit()


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


class Game():
    def __init__(self):
        pass









 

if __name__ == '__main__':
    print("Welcome!")
    word = input("Word:")
    type = input("Type:")
    program = Main("sozluk.sql", "words" ,word, type)
    if program.controller():
        mean = input("Turkish:")
        word = (word, type, mean, "0", "0", "0", "0", "0")
        program.add(word)
    else:
        print("'{}' is already exist!".format(word))
        program.update("Ask+1", "Ask", word, type)
        pass

    