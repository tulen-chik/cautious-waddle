import os

books = [os.path.splitext(book) for book in os.listdir(path="books") if os.path.splitext(book)[1] == ".txt"]

# валидация введеного пользователя номера книги
def is_invalid_num(num):
    # try обрабатывает ошибки(int("a") - вызовет ошибку, т.к. "a" не число)
    try:
         return False if 1 <= int(book_to_show) <= len(books) else True
    except Exception:
        return True


# если в папке нет книг
if not books:
    print("нет книг в наличии, положите все книги в папку books(они должны иметь разрешение .txt)")

while books:
    # печать названия книг в папке
    print("книги в наличии:")
    # enumerate возращает *(num, book) num - число по порядку(начиная с 0), book - название и разрешение файла ("book", ".txt")
    for num, book in enumerate(books):
        print(f"{num + 1} - {book[0]}")
    

    book_to_show = input("введите номер книги, которую вы хотите открыть: ")
    while is_invalid_num(book_to_show):
        book_to_show = input("вы неправильно ввели номер, введите еще раз:")
            
    # ищем в массиве всех книг нужную
    book_to_show = books[int(book_to_show) - 1]
    # with - менеджер контекста, тож самое, что открытие и закрытие файла в c++, только в одном ключевом слове
    # ну типо f = open("относительный адрес файла")
    # а потом f.close(), но мы этого не делаем, просто используем: with open("books\book.txt") - пример на python без with
    with open("books\\" + book_to_show[0] + book_to_show[1], "r") as f:
        print(f.read())
    
    # продолжать ли работу
    repeat = input("хотите открыть другую книгу(д \ н): ")
    while repeat != "н" and repeat != "д":
        repeat = input("символ не был распознан, введите \"н\" или \"д\"")
    
    # ну ты понял
    if repeat == "н":
        books = False
