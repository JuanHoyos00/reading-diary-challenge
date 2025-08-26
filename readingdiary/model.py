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
        if rating != Book.EXCELLENT or rating != Book.GOOD or rating != Book.BAD:
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
        pagina = 0

        if len(self.notes) == 0:
            return -1

        for note in self.notes:
            if note.page in comparar:
                comparar[note.page] += 1
            else:
                comparar[note.page] = 1
        for clave, cont in comparar.values():
            if cont > contador:
                contador = cont
                pagina = clave

        return pagina








