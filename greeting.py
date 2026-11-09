WHO_TO_GREET = "GitHub Actions Student"

def greet(name=WHO_TO_GREET):
    print(f"Hello {name}!")
    print("This program is running inside GitHub Actions.")

greet()