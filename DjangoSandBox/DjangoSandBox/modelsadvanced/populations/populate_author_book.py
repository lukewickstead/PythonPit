from os import environ

environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSandBox.settings')

import django

django.setup()

from modelsadvanced.models import Author, Book

author_names = {"George Orwell", "W. Somerset Maugham", "Aldous Huxley"}
book_names = {"1984", "Of Human Bondage", "Brave New World"}


def populate():
    for author_name in author_names:
        an_author = save_author(author_name)
        for book_name in book_names:
            save_book(book_name, an_author)


def print_data():
    for anAuthor in Author.objects.all():
        for a_book in anAuthor.book_set.all():
            print("{0} --> {1}".format(anAuthor, a_book))

    for a_book in Book.objects.all():
        for anAuthor in a_book.author.all():
            print("{0} --> {1}".format(a_book, anAuthor))


def save_author(name):
    return Author.objects.get_or_create(name=name)[0]


def save_book(name, author):
    a_book = Book.objects.get_or_create(name=name)[0]
    a_book.authors.add(author)

# Execution
if __name__ == '__main__':
    populate()
    print_data()
