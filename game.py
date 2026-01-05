import time
import threading

# Game State
money = 0
cps = 0  # Clicks per second
click_value = 1

def auto_clicker():
    """Background thread to add money automatically."""
    global money
    while True:
        money += cps
        time.sleep(1)

def game_loop():
    """Main game loop for user input."""
    global money, cps
    
    # Start the auto-clicker in the background
    threading.Thread(target=auto_clicker, daemon=True).start()
    
    while True:
        print(f"\nMoney: ${money} | CPS: {cps}")
        action = input("Press Enter to click, 'u' to upgrade (Cost $10), 'q' to quit: ").lower()
        
        if action == "":
            money += click_value
            print(f"Clicked! You now have ${money}")
        elif action == 'u':
            if money >= 10:
                money -= 10
                cps += 1
                print("Upgrade purchased! +1 CPS")
            else:
                print("Not enough money!")
        elif action == 'q':
            break

if __name__ == "__main__":
    print("Welcome to Python Idle Clicker!")
    game_loop()

