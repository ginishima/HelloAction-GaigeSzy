from datetime import datetime

WHO_TO_GREET = "GitHub Actions Student"
now = datetime.now()

def greet(name=WHO_TO_GREET):
    print(f"Hello {name}!")
    print("This program is running inside GitHub Actions.")
    print(f"Current date and time: {now:%Y-%m-%d %H:%M}")

greet()