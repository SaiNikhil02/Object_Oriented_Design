 # 🎲 Blackjack - Object-Oriented Design

## 🃏 Background
Blackjack is a classic casino card game where players aim to get a hand value as close to **21** as possible **without exceeding** it. The game is played between a **player** and a **dealer**, with the following rules:

1. **Initial Hands**: Both the **player** and the **dealer** receive two cards.
   - The **player sees both their cards**.
   - The **dealer’s second card is hidden**.
2. **Player's Turn**: The player can **hit (draw a card)** or **stand (stop)**.
3. **Dealer's Turn**: The dealer must keep drawing until they reach a value of at least **N**, where **N = player's hand value**.
4. **Winning Conditions**:
   - If the **player exceeds 21**, they **lose**.
   - If the **dealer exceeds 21**, the **player wins**.
   - The **higher hand (≤ 21) wins**.
   - A **tie results in a push** (no winner).

---

## 📌 Key Requirements
✅ **Two Players**: **Dealer** and **User**  
✅ **One Deck of 52 Cards**: Refilled after each round  
✅ **Betting System**: The **player can wager money**, but the **dealer never runs out of funds**  

---

## 🛠 Object-Oriented Design

### 🔹 Classes Overview
| **Class**       | **Responsibility** |
|----------------|------------------|
| **Card**       | Represents a playing card with a suit and value. |
| **Deck**       | Manages shuffling and dealing of cards. |
| **Player**     | Abstract class for both the dealer and user. |
| **Dealer**     | Implements dealer logic for drawing cards. |
| **UserPlayer** | Handles player actions, betting, and balance. |
| **BlackjackGame** | Manages the full game flow and user interaction. |

---

## 🎮 Game Flow
1. **Betting Phase**:  
   - The player places a bet before the round starts.
   
2. **Card Distribution**:  
   - The player and dealer each receive two cards.
   - One dealer card remains hidden.

3. **Player's Turn**:  
   - The player can **hit** (draw) or **stand** (stop drawing).

4. **Dealer's Turn**:  
   - The dealer must draw until they reach or exceed the player's hand value.

5. **Winning Logic**:  
   - **Bust Condition**: If the player exceeds **21**, they **lose** instantly.
   - **Dealer Busts**: If the dealer exceeds **21**, the **player wins**.
   - **Higher Hand Wins**: If neither busts, the highest valid hand wins.
   - **Tie Condition**: The bet is returned to the player.

---

## 💰 Betting System
- The **player starts with an initial balance**.
- The **player can bet** as much money as they have.
- If the **player wins**, they receive **double their bet**.
- If the **player loses**, the bet is deducted.
- The **dealer never runs out of money**.

---

## 🏆 How to Play
1. Run the Blackjack game.
2. Place your bet.
3. Choose to **hit** or **stand**.
4. The dealer plays.
5. Win, lose, or tie based on the rules above!

---

