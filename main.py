# ran using bash: | python main.py | to avoid errors
import csv
import matplotlib.pyplot as plt
import numpy as np

ratings = []
page = []
with open("YA_Books.csv", mode="r") as bookFile:
    books = csv.reader(bookFile)
    next(books) # skip 1st row/ header

    most_recent_published = 0
    worst_rating = 5.0
    best_rating = 0.0
    highest_rating = 0.0
    most_pages = 0

    for book in books:
        title = book[0]
        author = book[1]
        year = int(book[2])
        publisher = book [3]
        genre = book[4]
        pages = int(book[5])
        rating = float(book[6])
        ratings.append(rating)
        page.append(pages)
        print(f"{title} by {author} on {year}. Published by {publisher}, it belongs to the {genre} genre. Contains{pages} pages and a {rating} Goodreads rating.")

        if author.startswith("M"):
            print(author)

        if year > most_recent_published:
            most_recent_published = year
            most_recent_book = book

        if rating < worst_rating:
            worst_rating = rating
            worst_rated_book = book

        if year <= 2000:
            if pages > most_pages:
                most_pages = pages
                most_pages_book = book

        if rating > best_rating:
            best_rating = rating
            best_rated_book = book

        
print(f"Book with most pages is before 2000 {most_pages_book}")
print(f"Most recently published{most_recent_book}")
print(f"Highest rated book is {best_rated_book}")
print(f"Book with worst rating{worst_rated_book}")

x = np.array(ratings)
y = np.array(page)

plt.bar(x, y, color="#CF63CA", width=0.0125)
plt.xlabel("Rating")
plt.ylabel("Pages")
plt.show()

