def books_by_genre(books, the_genre): # Exercise 1's Function
    avg_pages = 0 # It's a sum for now
    books_from_this_genre = []

    for book in books:
        if book['genre'] == the_genre:
            books_from_this_genre.append(book['title'])
            avg_pages += book['pages']

    avg_pages = avg_pages / len(books_from_this_genre) if len(books_from_this_genre) != 0 else avg_pages # Now its the actual average

    return books_from_this_genre, avg_pages



def get_books_name_for_reader(books, readers, reader_name): # Exercise 2's Function
    leased_books = []

    for reader in readers:
        if reader['name'] == reader_name: # Found the dictionary of our reader
            for book_id in reader['borrowed']:
                for book in books:
                    if book_id == book['book_id']:
                        leased_books.append(book['title'])


    return leased_books



def most_read_book(books, readers): # Exercise 3's Function
    most_leased = set()
    highest_votes = 0

    for book in books:
        book['votes'] = 0
        for reader in readers:
            for book_id in reader['borrowed']:
                if book_id == book['book_id']:
                    book['votes'] += 1
        highest_votes = book['votes'] if book['votes'] > highest_votes else highest_votes

    for book in books:
        if book['votes'] == highest_votes:
            most_leased.add(book['title'])


    return most_leased



def loan_book(books, readers, reader_name, book_name): # Exercise 4's Function
    book_id = 0

    for book in books:
        book_id = book['book_id'] if book['title'] == book_name else book_id

    if book_id == 0:
        return False

    for reader in readers:
        if reader['name'] == reader_name:
            for existing_book in reader['borrowed']:
                if existing_book == book_id:
                    return False
            reader['borrowed'].append(book_id)
            return True
    return False



def return_book(books, readers, reader_name, book_name): # Exercise 5's Function
    book_id = 0

    for book in books:
        book_id = book['book_id'] if book['title'] == book_name else book_id

    if book_id == 0:
        return False

    for reader in readers:
        if reader['name'] == reader_name:
            for existing_book in reader['borrowed']:
                if existing_book == book_id:
                    reader['borrowed'].remove(book_id)
                    return True
            return False
    return False



def readers_having_most_read_book(readers): # Exercise 6's Function
    books_by_id = []
    possessing_readers = set()
    highest_votes = 0

    for reader in readers: # Create a list with dicts containing book ID book's vote count
        for readers_book_id in reader['borrowed']:
            books_by_id.append(dict(book_id = readers_book_id, votes = 0))

    for book in books_by_id: # Count the votes and find the highest vote count
        for reader in readers:
            for readers_book_id in reader['borrowed']:
                if readers_book_id == book['book_id']:
                    book['votes'] += 1
        highest_votes = book['votes'] if book['votes'] > highest_votes else highest_votes

    for book in books_by_id: # Check which readers have the most-leased books
        if book['votes'] == highest_votes:
            for reader in readers:
                for readers_book_id in reader['borrowed']:
                    if readers_book_id == book['book_id']:
                        possessing_readers.add(reader['name'])

    return possessing_readers



# def readers_having_most_read_bookv1(books, readers): # Exercise 6's Function
#     most_leased_names = most_read_book(books, readers)
#     most_leased_ids = set()
#     possessing_readers = set()
#
#     for popular in most_leased_names: # Create a set of the IDs of the most-leased books
#         for book in books:
#             if popular == book['title']:
#                 most_leased_ids.add(book['book_id'])
#
#     for reader in readers:
#         for readers_book_id in reader['borrowed']:
#             for popular_book_id in most_leased_ids:
#                 if readers_book_id == popular_book_id:
#                     possessing_readers.add(reader['name'])
#
#     return possessing_readers



if __name__ == '__main__':
    choice = -1
    while choice != 0:
        print('\nWhat would you like to do? \
        \n1: Find books from a specific genre \
        \n2: Get the list of leased books of a specific reader \
        \n3: Find the most-leased books \
        \n4: Lease a book \
        \n5: Return a book \
        \n6: Find which readers have the most-leased books \
        \n0: Exit')
        choice = int(input('\nEnter your choice: '))

        # Books List
        books = [dict(book_id=1001, title="Harry Potter", genre="fantasy", pages=500),
                 dict(book_id=1002, title="A song of Ice and Fire", genre="fantasy", pages=700),
                 dict(book_id=1003, title="1984", genre="classic", pages=800),
                 dict(book_id=1004, title="Attack on Titan", genre="manga", pages=1400),
                 dict(book_id=1005, title="One Piece", genre="manga", pages=12000)
        ]

        # Readers List
        readers = [{"name": "Ichi", "borrowed": [1001, 1003]},
                   {"name": "Ni", "borrowed": [1002]},
                   {"name": "San", "borrowed": [1005, 1002]},
                   {"name": "Yon", "borrowed": [1005, 1002]},
                   {"name": "Go", "borrowed": [1005]}
        ]


        if choice == 1:
            genre = 'classic'

            print(f'\nList of {genre} books, and their average page count:')

            print(books_by_genre(books, genre)) # Exercise 1's Function


        elif choice == 2:
            reader_name = 'Yon'

            print(f'\n{reader_name}\'s leased books:')

            print(get_books_name_for_reader(books, readers, reader_name)) # Exercise 2's Function


        elif choice == 3:
            print(f'\nThe most leased book/s are:')


            print(most_read_book(books, readers)) # Exercise 3's Function


        elif choice == 4:
            book_name   = 'One Piece'
            reader_name = 'San'

            print(f'\n{reader_name} wants to lease the book \'{book_name}\'.')

            print(loan_book(books, readers, reader_name, book_name))  # Exercise 4's Function


        elif choice == 5:
            book_name   = 'Attack on Titan'
            reader_name = 'Yon'

            print(f'\n{reader_name} wants to return the book \'{book_name}\'.')

            print(return_book(books, readers, reader_name, book_name)) # Exercise 5's Function


        elif choice == 6:
            print(f'\nFinding which readers have the most-leased books')


            print(readers_having_most_read_book(readers))  # Exercise 6's Function


        elif choice == 0:
            print('Goodbye!')
            exit()

        else:
            print('Invalid Input. Please try again.')
            choice = int(input('\nEnter your choice: '))

        break
