import random
import string

def generate_password(length=12, mode="normal"):
    if mode == "normal":
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
    
    elif mode == "absurd":
        words = ["mangga", "durian", "kopi", "sosis", "otak-otak", "robot", "meong", "dragon", "bucin", "pinguin"]
        random_word = random.choice(words).capitalize()
        numbers = str(random.randint(100, 999))
        symbols = ''.join(random.choice("!@#$%^&*") for _ in range(3))
        return f"{random_word}{numbers}{symbols}"

    else:
        raise ValueError("Mode harus 'normal' atau 'absurd'.")

if __name__ == "__main__":
    print("=== Password Generator ===")
    mode = input("Pilih mode (normal/absurd): ").strip().lower()
    if mode == "normal":
        length = int(input("Panjang password: "))
        print("Password kamu:", generate_password(length, mode))
    elif mode == "absurd":
        print("Password absurd kamu:", generate_password(mode="absurd"))
    else:
        print("Mode tidak dikenal.")
