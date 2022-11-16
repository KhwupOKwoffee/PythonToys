import random
import tkinter as tk


class BlackjackWindow(tk.Tk):

    def __init__(self):

        # Window properties
        super().__init__()
        self.title("Blackjack")
        self.geometry("280x260")
        self.resizable(width = False, height = False)

        # Status label
        self.status = tk.Label(self, text = "\n")
        self.status.grid(row = 0)

        # Player & dealer value labels
        self.player_value = tk.Label(self, text = "\n")
        self.player_value.grid(row = 1)

        self.dealer_value = tk.Label(self, text = "\n")
        self.dealer_value.grid(row = 2)

        # Play button
        self.play_button = tk.Button(
            self,
            width = 31,
            height = 2,
            text = "Play",
            command = self.play
        )
        self.play_button.grid(row = 3)

        # Hit button
        self.hit_button = tk.Button(
            self,
            width = 31,
            height = 2,
            text = "Hit",
            command = self.hit,
            state = "disabled"
        )
        self.hit_button.grid(row = 4)

        # Stand button
        self.stand_button = tk.Button(
            self,
            width = 31,
            height = 2,
            text = "Stand",
            command = self.stand,
            state = "disabled"
        )
        self.stand_button.grid(row =5)

    def play(self):

        # Creates a deck & hands
        self.deck = [card for card in "A23456789TJQK"] * 4
        random.shuffle(self.deck)

        self.player_stood = False
        self.dealer_stood = False

        self.player_hand = []
        self.dealer_hand = []

        self.status["text"] = "\n"
        self.play_button["state"] = "disabled"

        # Deals two cards each to the player & dealer
        self.player_hand = self.deal_card(self.player_hand)
        self.player_postturn()
        self.dealer_hand = self.deal_card(self.dealer_hand)
        self.dealer_postturn()
        self.player_hand = self.deal_card(self.player_hand)
        self.player_postturn()
        self.dealer_hand = self.deal_card(self.dealer_hand)
        self.dealer_postturn()

    def deal_card(self, hand):

        hand += self.deck[-1]
        self.deck.pop()
        return hand

    def get_hand_value(self, hand, ace_value = "dynamic"):

        value, aces = 0, 0
        for card in hand:
            if card in "23456789":
                value += int(card)
            elif card in "TJQK":
                value += 10
            else:
                if ace_value != "dynamic":
                    value += ace_value
                    continue
                aces += 1
        if aces:
            if value < 11:
                aces -= 1
                value += 11
            value += 1 * aces
        return value

    def hit(self):

        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"
        self.player_hand = self.deal_card(self.player_hand)
        self.player_postturn()

    def stand(self):

        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"
        while not self.dealer_stood:
            self.player_postturn()

        # Calculates the closest to blackjack if both stand
        player_hand_value = self.get_hand_value(self.player_hand)
        dealer_hand_value = self.get_hand_value(self.dealer_hand)
        if self.status["text"] == "\n":
            if player_hand_value > dealer_hand_value:
                self.status["text"] = "You're Closest To Blackjack!\nYou Win!"
                self.end_game()
            elif player_hand_value < dealer_hand_value:
                self.status["text"] = "You're Furthest From Blackjack!\nYou Lose!"
                self.end_game()
            else:
                self.status["text"] = "It's a Tie!\n"
                self.end_game()

    def dealer_turn(self):

        if not self.dealer_stood:
            if self.dealer_decide():
                self.dealer_hand = self.deal_card(self.dealer_hand)
            else:
                self.dealer_stood = True
        self.dealer_postturn()

    def dealer_decide(self):

        # Logic dictating whether the dealer hits or stands
        value = self.get_hand_value(self.dealer_hand)
        lvalue = self.get_hand_value(self.dealer_hand, 1)
    
        if value == lvalue:
            if value >= 17:
                output = False
            else:
                output = True
        elif value >= 18:
            output = False
        else:
            output = True
        return output

    def player_postturn(self):

        # Checks if the player has busted or reached blackjack
        player_hand_value = self.get_hand_value(self.player_hand)
        self.player_value["text"] = f"Your Hand Is {self.player_hand}" +\
            f"\nYour Hand Is Worth {player_hand_value}"
        if player_hand_value == 21:
            self.status["text"] = "You've Reached Blackjack!\nYou Win!"
            self.end_game()
        elif player_hand_value > 21:
            self.status["text"] = "You've Gone Bust!\nYou Lose!"
            self.end_game()
        else:
            if len(self.dealer_hand) >= 2:
                self.dealer_turn()

    def dealer_postturn(self):

        # Checks if the dealer has busted or reached blackjack
        dealer_hand_value = self.get_hand_value(self.dealer_hand)
        self.dealer_value["text"] = f"The Dealer Has {len(self.dealer_hand)} Cards\n"
        if dealer_hand_value == 21:
            self.status["text"] = "The Dealer's Reached Blackjack!\nYou Lose!"
            self.end_game()
        elif dealer_hand_value > 21:
            self.status["text"] = "The Dealer's Gone Bust!\nYou Win!"
            self.end_game()
        else:
            if len(self.dealer_hand) >= 2:
                self.hit_button["state"] = "normal"
                self.stand_button["state"] = "normal"

    def end_game(self):

        # Displays the dealer's cards and allows a new game to start
        dealer_hand_value = self.get_hand_value(self.dealer_hand)
        self.dealer_value["text"] = f"The Dealer's Hand Is {self.dealer_hand}" +\
            f"\nThe Dealer's Hand Is Worth {dealer_hand_value}"
        self.play_button["state"] = "normal"
        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"

