# The code below shows how to keep name and votes inside one object
# It explains how to increase the vote count by one
# It explains how to show the final vote number in a simple line
# You can use this structure in small voting simulations or training exercises

class Candidate:
    def __init__(self, name):      # creates a new candidate with a name
        self.name = name           # saves candidate name
        self.votes = 0             # sets initial votes

    def add_vote(self):            # adds a single vote
        self.votes += 1            # increases vote count

    def display(self):             # shows candidate data
        print(f"Candidate: {self.name}, Votes: {self.votes}")  # prints name and votes

# Example usage
candidate1 = Candidate("Alice")    # creates first candidate
candidate2 = Candidate("Bob")      # creates second candidate

candidate1.add_vote()              # vote one for Alice
candidate1.add_vote()              # vote two for Alice
candidate2.add_vote()              # vote one for Bob

candidate1.display()               # prints Alice votes
candidate2.display()               # prints Bob votes