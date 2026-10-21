import sys


def get_student_key():
    while True:
        student_key = input("Student key: ").strip()
        if student_key:
            return student_key
        print("Student key cannot be empty. Please try again.")


def get_item_name():
    while True:
        item_name = input("Item name: ").strip()
        if item_name:
            return item_name
        print("Item name cannot be empty. Please re-enter it.")


def get_price():
    while True:
        try:
            price = float(input("Unit price: "))
        except ValueError:
            print("Invalid price. Please enter a positive number.")
            continue
        if price <= 0:
            print("Unit price must be greater than 0.")
            continue
        return price


def get_quantity():
    while True:
        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a whole number greater than or equal to 1.")
            continue
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue
        return quantity


def main():
    student_key = get_student_key()
    seed = sum(ord(ch) for ch in student_key.strip())

    subtotal = 0.0
    total_units = 0

    while True:
        item_name = input("Item name (type DONE to finish): ").strip()
        if item_name.upper() == "DONE":
            break

        if not item_name:
            print("Item name cannot be empty. Please try again.")
            continue

        try:
            unit_price = float(input("Unit price: "))
        except ValueError:
            print("Invalid price. Please enter a positive number.")
            continue
        if unit_price <= 0:
            print("Unit price must be greater than 0.")
            continue

        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Invalid quantity. Please enter a whole number greater than or equal to 1.")
            continue
        if quantity < 1:
            print("Quantity must be at least 1.")
            continue

        subtotal += unit_price * quantity
        total_units += quantity

    if total_units >= 10 or subtotal >= 100:
        discount_percent = 10
    else:
        discount_percent = 0

    discounted_total = subtotal * (1 - discount_percent / 100)

    perk_applied = seed % 2 == 1
    if perk_applied:
        discounted_total -= 3.00

    if discounted_total < 0:
        discounted_total = 0.0

    print(f"Seed: {seed}")
    print(f"Units: {total_units}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Perk applied: {'YES' if perk_applied else 'NO'}")
    print(f"Total: ${discounted_total:.2f}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye.")
        sys.exit(0)
