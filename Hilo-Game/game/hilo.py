from game.cards import Cards


class Hilo:
    """Hilo Game. 
    
    The player guesses if the next card drawn by the dealer will be higher or lower than the previous one..

    Attributes:
        cards: Cards instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score inicial is 300, Stores the player's total score..
        card (int): Stores the first number card to be shown to the user.
        next_card (int): Stores the next number card to show the user.
        higher_or_lower: Stores the letter "l" or letter "h" as the user chooses.
        play_again: Stores user response whether they want to continue playing or not.
    """

    def __init__(self):
        """Constructs a new Hilo.
        
        Args:
            self (Hilo): an instance of Hilo.
        """

        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Hilo): an instance of Hilo.
        """


    def display_card(self):
        """.It will show first random card for the game.

        Args:
            self (Hilo): an instance of Hilo.
        """
       
    def guess_next_card(self):
        """.Select the user's choice to guess whether the next card is greater or less than the first card displayed.

        Args:
            self (Hilo): an instance of Hilo.
        """       


    def display_next_card(self):
        """. It will show next random card for the game.

        Args:
            self (Hilo): an instance of Hilo.
        """       
        
    def compare_cards(self):
        """.Compare the first with the second side and assign score to the player depending on the choice the player has made to guess.

        Args:
            self (Hilo): an instance of Hilo.
        """

       
    def display_score(self):
        """. Displays the player's current score.

        Args:
            self (Hilo): an instance of Hilo.
        """

    
    def get_playing_decision(self):
        """. Allows the user to decide whether they want to continue playing or not.

        Args:
            self (Hilo): an instance of Hilo.
        """
