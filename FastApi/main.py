from fastapi import FastAPI,Body
app=FastAPI()
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]
@app.get("/api/")
async def First_api_ReadAll_books():
    return BOOKS
@app.get("/books/bytitle/")
async def read_books_by_title(title:str):
    book_title=[]
    for book in BOOKS:
        if book.get('title').casefold()==title.casefold():
            book_title.append(book)
    return book_title
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/bycategory/")
async def read_books_by_category_path(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS
@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==update_book.get('title').casefold():
            BOOKS[i]=update_book
@app.delete("/books/{book_title}")
async def delete_book_by_title(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('category').casefold()==book_title.casefold():
            BOOKS.pop(i)
            break
@app.get("/books/byauthor/{read_author}")
async def read_allbook_by_author(book_author:str):
    author=[]
    for book in BOOKS:
        if book.get('author').casefold() ==book_author.casefold():
            author.append(book)
    return author




