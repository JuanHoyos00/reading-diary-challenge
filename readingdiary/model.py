from datetime import datetime

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1
    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        self.notes.append(Note(text, page, date))
        return True

    def set_rating(self, rating: int) -> bool:
        if rating != Book.EXCELLENT and rating != Book.GOOD and rating != Book.BAD:
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page:int) -> list[Note]:
        list_of_notes: list[Note] = []
        for note in self.notes:
            if note.page == page:
                list_of_notes.append(note)
        return list_of_notes

    def page_with_most_notes(self) -> int:
        comparar: dict[int, int] = {}
        contador: int = 0
        pagina: int = 0

        if len(self.notes) == 0:
            return -1

        for note in self.notes:
            if note.page in comparar:
                comparar[note.page] += 1
            else:
                comparar[note.page] = 1
        for clave, cont in comparar.items():
            if cont > contador:
                contador = cont
                pagina = clave

        return pagina

    def __str__(self) -> str:
        if self.rating == Book.EXCELLENT:
            rating = "excellent"
        if self.rating == Book.GOOD:
            rating = "good"
        if self.rating == Book.BAD:
            rating = "bad"
        else:
            rating = "unrated"
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nRating: {rating}"

class ReadingDiary:

    def __init__(self):
        self.books: dict[str,Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn  in self.books:
            return False
        else:
            self.books[isbn] = Book(isbn, title, author,pages)
            return True

    def search_by_isbn(self, isbn: str) -> Book|None:
        for clave,valor in self.books.items():
            if isbn == clave:
                return valor
        return None

    def add_note_to_book(self,isbn: str, text: str, page: int, date: datetime) -> bool:
        book: Book = self.search_by_isbn(isbn)
        if book is None:
            return False
        else:
            return book.add_note(text,page,date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book: Book|None = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Book|None:
        mayor: int = 0
        libro: Book|None = None

        if len(self.books) == 0:
            return None

        for book in self.books.values():
            if len(book.notes) > mayor:
                mayor = len(book.notes)
                libro = book

        return libro






