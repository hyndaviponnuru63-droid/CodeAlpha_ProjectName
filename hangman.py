import random

print("Welcome to Hangman!")

# Step 1: Take dynamic word list input
words_input = input("Enter words separated by spaces (or press Enter for default list): ").strip()

# Default words if nothing entered
if words_input:
    words = words_input.split()
else:
    words = ["python", "hangman", "developer", "computer", "program"]

# Step 2: Randomly pick a word
word = random.choice(words).lower()

# Step 3: Ask user for attempts (default = 6)
attempts_input = input("Enter number of attempts (default 6): ").strip()
attempts = int(attempts_input) if attempts_input.isdigit() else 6

# Step 4: Initialize
guessed = ["_"] * len(word)
used_letters = set()

# Step 5: Main game loop
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", ", ".join(sorted(used_letters)) or "None")

    guess = input("Guess a letter: ").lower().strip()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue
    if guess in used_letters:
        print("⚠️ You already guessed that letter.")
        continue

    used_letters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

# Step 6: Result
if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)


