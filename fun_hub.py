import time
import sys
import random

def loading_screen():
    messages = [
        "Filling up web shooster...",
        "Charging memes...",
        "Warming up AI roast engine...",
        "Calibrating compliments...",
        "Summoning fake therapist...",
        "Calculating love percentage...",
        "Tracking faces...",
        "Pranking autotypers...",
        "Ghost cursor activated...",
        "Loading fake blue screen..."
    ]

    bar_length = 30
    for i in range(bar_length + 1):
        percent = int((i / bar_length) * 100)
        bar = "#" * i + "-" * (bar_length - i)
        message = random.choice(messages)
        sys.stdout.write(f"\r[{bar}] {percent}% - {message}    ")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nLoading complete! Starting the app...\n")

def ai_roast_bot():
    print("Welcome to AI Roast Bot! (feature coming soon)\n")

def meme_generator():
    print("Welcome to Meme Generator! (feature coming soon)\n")

def compliment_generator():
    print("Welcome to Compliment Generator! (feature coming soon)\n")

def fake_therapist():
    print("Welcome to Fake Therapist! (feature coming soon)\n")

def love_calculator():
    print("Welcome to Love Calculator! (feature coming soon)\n")

def face_tracker():
    print("Welcome to Face Tracker! (feature coming soon)\n")

def auto_typer_prank():
    print("Welcome to Auto Typer Prank! (feature coming soon)\n")

def ghost_cursor():
    print("Welcome to Ghost Cursor! (feature coming soon)\n")

def fake_webcam_flash():
    print("Welcome to Fake Webcam Flash! (feature coming soon)\n")

def fake_blue_screen():
    print("Welcome to Fake Blue Screen! (feature coming soon)\n")

def main_menu():
    while True:
        print("=== Fun Hub ===")
        print("1. AI Roast Bot")
        print("2. Meme Generator")
        print("3. Compliment Generator")
        print("4. Fake Therapist")
        print("5. Love Calculator")
        print("6. Face Tracker")
        print("7. Auto Typer Prank")
        print("8. Ghost Cursor")
        print("9. Fake Webcam Flash")
        print("10. Fake Blue Screen")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        print()

        if choice == '1':
            ai_roast_bot()
        elif choice == '2':
            meme_generator()
        elif choice == '3':
            compliment_generator()
        elif choice == '4':
            fake_therapist()
        elif choice == '5':
            love_calculator()
        elif choice == '6':
            face_tracker()
        elif choice == '7':
            auto_typer_prank()
        elif choice == '8':
            ghost_cursor()
        elif choice == '9':
            fake_webcam_flash()
        elif choice == '10':
            fake_blue_screen()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    loading_screen()
    main_menu()
