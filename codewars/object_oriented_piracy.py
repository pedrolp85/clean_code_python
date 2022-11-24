class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew


    def is_worth_it(self): 
        return (self.draft - self.crew * 1.5 > 20)


Titanic = Ship(15, 10 )

print(Titanic.is_worth_it())
