#create Author class

class Author:
    def __init__(self, name):
        #initialize with name and an empty book list
        self.name = name
        self.books = []

    def publish(self, book):
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

if __name__ == '__main__':
    main()
