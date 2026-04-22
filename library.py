books = [
    "The Great Gatsby — F. Scott Fitzgerald",
    "To Kill a Mockingbird — Harper Lee",
    "1984 — George Orwell",
    "Pride and Prejudice — Jane Austen",
    "Moby-Dick — Herman Melville",
    "War and Peace — Leo Tolstoy",
    "The Catcher in the Rye — J.D. Salinger",
    "The Hobbit — J.R.R. Tolkien",
    "Brave New World — Aldous Huxley",
    "Crime and Punishment — Fyodor Dostoevsky",
    "Jane Eyre — Charlotte Brontë",
    "The Lord of the Rings — J.R.R. Tolkien",
    "Animal Farm — George Orwell",
    "Wuthering Heights — Emily Brontë",
    "The Odyssey — Homer",
    "The Brothers Karamazov — Fyodor Dostoevsky",
    "One Hundred Years of Solitude — Gabriel García Márquez",
    "The Picture of Dorian Gray — Oscar Wilde",
    "Fahrenheit 451 — Ray Bradbury",
    "Dracula — Bram Stoker",
    "The Iliad — Homer",
    "Les Misérables — Victor Hugo",
    "A Tale of Two Cities — Charles Dickens",
    "Don Quixote — Miguel de Cervantes",
    "Ulysses — James Joyce",
    "The Divine Comedy — Dante Alighieri",
    "Hamlet — William Shakespeare",
    "Macbeth — William Shakespeare",
    "The Alchemist — Paulo Coelho",
    "The Little Prince — Antoine de Saint-Exupéry",
    "Slaughterhouse-Five — Kurt Vonnegut",
    "Catch-22 — Joseph Heller",
    "The Sun Also Rises — Ernest Hemingway",
    "The Old Man and the Sea — Ernest Hemingway",
    "Anna Karenina — Leo Tolstoy",
    "Madame Bovary — Gustave Flaubert",
    "The Stranger — Albert Camus",
    "The Metamorphosis — Franz Kafka",
    "Siddhartha — Hermann Hesse",
    "Heart of Darkness — Joseph Conrad",
    "The Sound and the Fury — William Faulkner",
    "Lolita — Vladimir Nabokov",
    "Beloved — Toni Morrison",
    "Invisible Man — Ralph Ellison",
    "The Road — Cormac McCarthy",
    "Life of Pi — Yann Martel",
    "The Kite Runner — Khaled Hosseini",
    "A Thousand Splendid Suns — Khaled Hosseini",
    "The Book Thief — Markus Zusak",
    "The Fault in Our Stars — John Green",
    "Gone with the Wind — Margaret Mitchell",
    "The Hunger Games — Suzanne Collins",
    "Harry Potter and the Sorcerer’s Stone — J.K. Rowling",
    "The Da Vinci Code — Dan Brown",
    "Angels & Demons — Dan Brown",
    "The Girl with the Dragon Tattoo — Stieg Larsson",
    "The Shining — Stephen King",
    "It — Stephen King",
    "Misery — Stephen King",
    "Dune — Frank Herbert",
    "Ender’s Game — Orson Scott Card",
    "Neuromancer — William Gibson",
    "Snow Crash — Neal Stephenson",
    "Foundation — Isaac Asimov",
    "I, Robot — Isaac Asimov",
    "The Martian — Andy Weir",
    "Ready Player One — Ernest Cline",
    "Jurassic Park — Michael Crichton",
    "The Time Machine — H.G. Wells",
    "The War of the Worlds — H.G. Wells",
    "Frankenstein — Mary Shelley",
    "The Handmaid’s Tale — Margaret Atwood",
    "Oryx and Crake — Margaret Atwood",
    "The Giver — Lois Lowry",
    "The Maze Runner — James Dashner",
    "Divergent — Veronica Roth",
    "Twilight — Stephenie Meyer",
    "The Chronicles of Narnia — C.S. Lewis",
    "Alice’s Adventures in Wonderland — Lewis Carroll",
    "Through the Looking-Glass — Lewis Carroll",
    "Peter Pan — J.M. Barrie",
    "Treasure Island — Robert Louis Stevenson",
    "Robinson Crusoe — Daniel Defoe",
    "Gulliver’s Travels — Jonathan Swift",
    "The Secret Garden — Frances Hodgson Burnett",
    "Little Women — Louisa May Alcott",
    "Anne of Green Gables — L.M. Montgomery",
    "Heidi — Johanna Spyri",
    "Black Beauty — Anna Sewell",
    "Charlotte’s Web — E.B. White",
    "Matilda — Roald Dahl",
    "The BFG — Roald Dahl",
    "Charlie and the Chocolate Factory — Roald Dahl",
    "The Wind in the Willows — Kenneth Grahame",
    "Watership Down — Richard Adams",
    "The Call of the Wild — Jack London",
    "White Fang — Jack London",
    "Of Mice and Men — John Steinbeck",
    "East of Eden — John Steinbeck",
    "The Grapes of Wrath — John Steinbeck"
]

borrowed = []

for i in range(len(books)):
    for j in range(len(books) - 1):
        count = 0
        while count < len(books[j]) and count < len(books[j+1]):
            if ord(books[j][count]) > ord(books[j+1][count]):
                books[j], books[j+1] = books[j+1], books[j]
                break
            elif ord(books[j][count]) < ord(books[j+1][count]):
                break
            count += 1

while True:
    userInput = input("Enter one of these options: borrow, return, exit --> ")
    userInput = userInput.strip()

    if userInput == "borrow":
        taken = True
        searchBorrowed = True
        bookToBorrow = input("Enter the name of the book or author's name --> ")
        bookToBorrow = bookToBorrow.strip()
        for i in range(len(books)):
            if bookToBorrow in books[i]:
                borrowed.append(books[i])
                del books[i]
                print("Borrowed")
                searchBorrowed = False
                taken = False
                break
        if searchBorrowed:
            for i in range(len(borrowed)):
                if bookToBorrow in borrowed[i]:
                    print("Sorry, it is taken.")
                    taken = False
                    break
        if taken:
            print("No such book or author.")

    elif userInput == "return":
        searchInBooks = True
        invalidInput = True
        bookToReturn = input("Enter the name of the book or author's name --> ")
        bookToReturn = bookToReturn.strip()
        for i in range(len(borrowed)):
            if bookToReturn in borrowed[i]:
                print("Returned")
                searchInBooks = False
                invalidInput = False
                break
        if searchInBooks:
            for i in range(len(books)):
                if bookToReturn in books[i]:
                    print("It is available.")
                    invalidInput =  False
                    break
        if invalidInput:
            print("No such book or author.")

    elif userInput == "exit":
        break

    else:
        print("Enter commands exactly as listed.")