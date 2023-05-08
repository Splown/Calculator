# Definiera funktioner för grundläggande matematiska operationer
def add(x, y):
    # Returnerar summan av x och y.
    return x + y

def subtract(x, y):
    # Returnerar differensen mellan x och y
    return x - y

def multiply(x, y):
    # Returnerar produkten av x och y
    return x * y

def divide(x, y):
    # Returnerar kvoten av x och y.
    if y == 0:
        print("Division med noll är inte tillåten.")
        return None
    return x / y

# En huvudfunktion för att hantera användarinteraktioner
def main():
    print("Välj en operation:")
    print("1. Addera")
    print("2. Subtrahera")
    print("3. Multiplicera")
    print("4. Dividera")

    operation = input("Ange ditt val: ")
    
    num1 = float(input("Ange första talet: "))
    num2 = float(input("Ange andra talet: "))

    if operation == "1":
        result = add(num1, num2)
    elif operation == "2":
        result = subtract(num1, num2)
    elif operation == "3":
        result = multiply(num1, num2)
    elif operation == "4":
        result = divide(num1, num2)
        if result is None:
            return
    else:
        print("Ogiltigt val")
        return
    
    print(f"Resultatet är {result}")

if __name__ == "__main__":
    main()