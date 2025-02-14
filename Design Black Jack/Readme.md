🎲 Blackjack - Object-Oriented Design
🃏 Background
Blackjack is a classic casino card game where players aim to get a hand value as close to 21 as possible without exceeding it. The player competes against the dealer, with the following rules:

Initial Hands: Both the player and the dealer receive two cards.
The player sees both their cards.
The dealer’s second card is hidden.
Player's Turn: The player can hit (draw a card) or stand (stop).
Dealer's Turn: The dealer must keep drawing until they reach a value of at least N, where N = player's hand value.
Winning Conditions:
If the player exceeds 21, they lose.
If the dealer exceeds 21, the player wins.
The higher hand (≤ 21) wins.
A tie results in a push (no winner).

📌 Key Requirements
✅ Two Players: Dealer and User
✅ One Deck of 52 Cards: Refilled after each round
✅ Betting System: The player can wager money, but the dealer never runs out of funds 

🛠 Requirements & Game Rules
🔎 Clarifying Questions
Before designing, some important questions to clarify:
✅ How many players? → Two (Player vs. Dealer)
✅ How many decks? → One (Refilled after each round)
✅ Is gambling involved? → Yes, the player starts with an initial balance
✅ Are suits relevant? → No (only card values matter)

🃏 Cards & Deck Structure
52 cards in a deck (Hearts ♦️, Spades ♠️, Diamonds ♦️, Clubs ♣️)
13 cards per suit
Card Values:
Numbered (2-10) → Face value
Face Cards (J, Q, K) → 10 points
Ace (A) → Can be 1 or 11, whichever benefits the player

🎲 Gameplay Mechanics
1️⃣ Starting a Round

The dealer and player each receive two cards
The dealer's second card is hidden
2️⃣ Player's Turn

Choose to Hit (draw a card) or Stand (stop)
If total exceeds 21, the player loses immediately
3️⃣ Dealer's Turn

The dealer must draw until reaching at least the player’s total
If the dealer exceeds 21, the player wins
4️⃣ Win Conditions

Player wins if their hand value is higher than the dealer's
Dealer wins if their hand is higher than the player's
Tie if both values are equal
💰 Gambling System
The player starts with a balance
The player places a bet each round
The dealer never runs out of money
🏗 Object-Oriented Design
📌 Classes & Responsibilities
Class	Responsibility
Card	Represents a playing card with suit and value
Deck	Manages the shuffling and drawing of cards
Player (Abstract)	Represents both Dealer and UserPlayer
Dealer	Draws cards following game rules
UserPlayer	Places bets, makes moves, tracks balance
Game	Controls the flow of gameplay

🚀 How to Run
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Object-Oriented-Design.git
cd Object-Oriented-Design/Blackjack
2️⃣ Run the game

bash
Copy
Edit
python Game.py
