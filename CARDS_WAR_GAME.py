### OOP PROJECT #####
# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

card_decks = {'SPADE':'black','DIAMOND':'red','HEART':'red','CLUB':'black'}
card_values = {'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9,'TEN':10,'JACK':11,'QUEEN':12,'KING':13,'ACE':13}

class Card():
    """Individual Card class"""

    def __init__(self, deck, value):
        self.deck, self.color = deck
        self.card, self.value = value

    def __str__(self):
        return f"{self.card} of {self.deck}"

class Player():
    """Individual Player class"""

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.on_table = []

    def add_card_top(self,card):
        self.hand.append(card)

    def num_cards(self):
        return len(self.hand)

    def pull_card(self):
        card = self.hand.pop()
        self.on_table.append(card)
        return card

    def take_on_table(self,others_on_table):
        self.hand = others_on_table + self.on_table + self.hand
        self.clear_on_table()

    def clear_on_table(self):
        self.on_table = []

class Table():
    """Table class"""

    def __init__(self, table_name):
        self.table_name = table_name
        self.table_deck = []
        self.table_players = []

    def create_deck(self):
        print(f"Table {self.table_name} deck is ready.")
        for deck, color in card_decks.items():
            for card, value in card_values.items():
                #print(card)
                self.table_deck.append(Card( (deck, color),(card, value) ))
        random.shuffle(self.table_deck)

    def pull_one_card(self,first,second):
        print(f"\n...PULLING ONE CARD EACH... {self.table_players[first].name} ({self.table_players[first].num_cards()}) {self.table_players[second].name} ({self.table_players[second].num_cards()})")
        c1 = self.table_players[first].pull_card()
        print(f"{self.table_players[first].name} pulled {c1}")
        c2 = self.table_players[second].pull_card()
        print(f"{self.table_players[second].name} pulled {c2}")
        print(f"{self.table_players[first].name} ({self.table_players[first].num_cards()}) {self.table_players[second].name} ({self.table_players[second].num_cards()})")
        return c1.value, c2.value

    def pull_four_card(self,first,second):
        print(f"\n...PULLING FOUR CARDS EACH... {self.table_players[first].name} ({self.table_players[first].num_cards()}) {self.table_players[second].name} ({self.table_players[second].num_cards()})")
        c1 = self.table_players[first].pull_card()
        c1 = self.table_players[first].pull_card()
        c1 = self.table_players[first].pull_card()
        c1 = self.table_players[first].pull_card()
        print(f"{self.table_players[first].name} last pulled {c1}")
        c2 = self.table_players[second].pull_card()
        c2 = self.table_players[second].pull_card()
        c2 = self.table_players[second].pull_card()
        c2 = self.table_players[second].pull_card()
        print(f"{self.table_players[second].name} last pulled {c2}")
        print(f"{self.table_players[first].name} ({self.table_players[first].num_cards()}) {self.table_players[second].name} ({self.table_players[second].num_cards()})")
        return c1.value, c2.value

    def continue_game(self,first,second,num):
        if self.table_players[first].num_cards() <= num or self.table_players[second].num_cards() <= num:
            return False
        return True
    
    def start_game(self):
        Player1 = Player(input("Player enter your name : "))
        self.table_players.append(Player1)
        Player2 = Player("computer")
        self.table_players.append(Player2)

        first = random.randint(0,1)
        second = 0
        if first:
            second = 0
        else:
            second = 1

        print(f"Players ready... {self.table_players[first].name} goes first")

        print("Creating, Shuffling and distributing cards...")
        self.create_deck()

        #print(f"deck size {len(self.table_deck)}")

        for x in range(52//2):
            #print(f"{card.card} of {card.deck} deck size {len(self.table_deck)}")
            self.table_players[first].add_card_top(self.table_deck.pop())
            self.table_players[second].add_card_top(self.table_deck.pop())

        #print(f"deck size {len(self.table_deck)}")

        print(f"{self.table_players[first].name} got {self.table_players[first].num_cards()} cards and {self.table_players[second].name} got {self.table_players[second].num_cards()} cards")

        #print(self.continue_game(first,second,1))

        while self.continue_game(first,second,1):
            c1, c2 = self.pull_one_card(first,second)
            
            while c1 == c2 and self.continue_game(first,second,4):
                print("...tie...")
                c1, c2 = self.pull_four_card(first,second)

            if c1 > c2:
                print(f"{self.table_players[first].name} takes the hand")
                self.table_players[first].take_on_table(self.table_players[second].on_table)
                self.table_players[second].clear_on_table()
            elif c1 < c2:
                print(f"{self.table_players[second].name} takes the hand")
                self.table_players[second].take_on_table(self.table_players[first].on_table)
                self.table_players[first].clear_on_table()
            else:
                break
            

                
        if self.table_players[first].num_cards() < self.table_players[second].num_cards():
            print(f"\n{self.table_players[second].name} wins \n{self.table_players[first].name} looses the match")
        else:
            print(f"\n{self.table_players[first].name} wins \n{self.table_players[second].name} looses the match")


table_one = Table("table_one")
table_one.start_game()
