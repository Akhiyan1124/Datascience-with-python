import time

def countdown(seconds):
    while seconds > 0:
        print(f"{seconds} seconds remaining")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    try:
        duration = int(input("Enter countdown time in seconds: "))
        if duration > 0:
            countdown(duration)
        else:
            print("Enter positive number.")
    except ValueError:
        print("Invalid input.")
