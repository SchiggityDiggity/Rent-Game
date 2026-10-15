# Each choice that utilizes a function in choices.py listed below

## twih_stream

Function includes:
- Random hype train event with a 1 in 6 odds of occuring
- Lists choices of what to stream, with each having a certain cash multiplier with user being limited to 3 different options to choose from
- A party raid event where viewership gets boosted by a random amount
- Amount of viewers is default 14, with each viewer possibly "donating" money to the streamer (user) with the amount being chosen randomly from $6, $1$0, or $25
- When option selected in main.py (choice #2), it consumes 2 energy

## pray_2_gods

Function includes:
- 12 different outcomes that randomly get selected
- Each choice affects a different aspect of the game
- Nothing does nothing, zeus is an instant loss, doublem is doubling their money, halfm is losing half their money, sleep is losing a day, 100 dollars is adding 100 dollars to budget, energy drink is a power up giving energy, energy refill refills energy, taxes reduced budget by 20%, and half rent is halving rent
- Consumes 1 energy and can only be used once

## ask_4_money

Function includes:
- Money received that choses default from 1-300 dollars
- After each round/rent payed increases max_money threshold by 125 for each round passed
- Fifty-fifty odds to receive money

## games.py

### Summary - black_jack:

- Takes it a bet they set beforehand in main.py
- Creates tuple with card suit and number, adds to deck, and shuffles them
- Draws 2 cards for player and draws/shows one of the dealer's cards
- Utilizes calculate_hand to calculate total, and it then prints it
- Prompts user to hit, stand, or double down after showing them their total
- If hit, adds a card and its value to total; if stand, player stays at their total; if double down, player draws one more card and doubles their intial bet
- Does final checks to see if player won or dealer won

### Summary - calculate_hand:

- Helper function that takes in dealer's hand and player's hand
- Checks whether the value/rank is one of the three ranks that equal ten: king, jack, and queen
- Also checks for aces using a ace counter that checks whether it being 11 would cause the player or dealer to bust, if it does it sets ace value to 1
- Adds total up and returns it back to black_jack

### Summary - dice_game:

- Creates dice roll possibilities as a tuple using a nested for loop that then adds the possibilities to dice
- Randomly selects winning combination, after shuffling dice
- Rolls dice and prints user's roll, it then checks whether it matches the selected winning combination
- If it doesn't match, returns 0, and if they win they multiply their bet by 10 and add it to budget

### Summary - rps:

- Creates the 3 choices and asks for user's input on their choice
- Goes through to checks to see whether user or cpu won, once player or cpu wins twice the game ends
- If player wins they double their bet and add it to their total


## main.py

main.py includes the main game with most of the text-based console that allows the user to control it.

- Imports each function and games required for main game
- Runs in main while loop (play_again) to keep game going until user quits
- Day while loop that keeps the menu options going until their energy runs out
- Energy while loop shows user menu options while their energy is greater than zero
- Option 1 - Gambling/games to make money, includes 3 games: Black Jack, Rock Paper Scissors, Dice Rolling
- Option 2 - stream on twih, utilizes twih_stream function
- Option 3 - pray to gods, utilizes pray_2_gods function
- Option 4 - Ask parents for money, utilizes ask_4_money function
- Option 5 - Accept you're done for, gives up/ends game
- Option 6 - Energy drink?, allows user to search for energy drinks if they do not have one, with it being a fifty-fifty chance on finding a random amount from 1-3. If they have one they get offered to drink it or not
- Final check that checks whether rent can be paid, if it cannot the player loses and is prompted if they want to continue to play
- Has more features that will have to discovered otherwise/not listed!