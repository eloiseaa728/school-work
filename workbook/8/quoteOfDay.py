import random
def RandomQuote():
    Quote = [["" for X in range(2)] for Y in range(3)]
    Quote[0][0] = "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."
    Quote[0][1]="Martin Fowler"
    Quote[1][0] = "Code is like humor. When you have to explain it, it's bad."
    Quote[1][1] = "Cory House"
    Quote[2][0] = "Simoplicity is the soul of efficiency."
    Quote[2][1] = "Austin Freeman"
    Index = random.randint(0,2)
    return Quote[Index][0], Quote[Index][1]

random.seed()
Quote, Author = RandomQuote()
print("{} - {}".format(Quote, Author))
