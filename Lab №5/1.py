class Book:
    def __init__(self,title, author,year):
        self.title = title
        self.author = author
        self.year = year

    #title = "Ведьмак. Последнее желание"
    #author = "Анджей Сапковский"
    #year = "1986"

    def get_info(self):
        print(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")


b1 = Book('1','2','3')
b1.get_info()