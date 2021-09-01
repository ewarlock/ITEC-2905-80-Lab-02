#create Author class

class Author:
    def __init__(self, name):
        #initialize with name and an empty book list
        self.name = name
        self.books = []

    def publish(self, book):
        if book in self.books:
            #print error message if book already published
            #& list the books already published under author
            print(f'"{book}" is already published under this author. The books published are:')
            for book in self.books:
                print(book)
            print('Please try again with a book title that is not already in this list.')
        else:
            #add to book list if book not already in list
            self.books.append(book)

    def __str__(self):
        #will do stuff only if the value is true
        #falsy values will be set to whatever is after the word 'or'
        book_list = ', '.join(self.books) or 'No published books.'
        return(f'Author: {self.name}; Books: {book_list}')


def main():
    sam = Author('Sam')
    sam.publish('Sam\'s book')
    sam.publish('Sam\'s sequel book part 2')

    print(sam)

    lisa = Author('Lisa')
    print(lisa)

    tessa_lastname = Author('Tessa Lastname')
    tessa_lastname.publish('The Best Book Ever')
    tessa_lastname.publish('Almost as Good as the Best Book Ever')
    tessa_lastname.publish('This Book is Just OK')

    print(tessa_lastname)

    lisa.publish('Lisa Finally Wrote a Book')
    print(lisa)

    #try to publish a book that is already published...
    tessa_lastname.publish('Almost as Good as the Best Book Ever')

if __name__ == '__main__':
    main()
