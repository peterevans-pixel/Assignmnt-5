import sys

import requests


def get_inventory_count():
    while True:
        try:
            on_hand = int(input("On hand: "))
        except ValueError:
            continue
        if on_hand < 0:
            continue
        return on_hand


def get_api_status(term):
    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params={"entity": "song", "limit": 5, "term": term},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        return "FAILED", None

    try:
        data = response.json()
    except (ValueError, TypeError):
        return "INVALID_RESPONSE", None

    if not isinstance(data, dict):
        return "INVALID_RESPONSE", None

    results = data.get("results")
    if not isinstance(results, list):
        return "INVALID_RESPONSE", None

    songs_returned = 0
    for result in results:
        if not isinstance(result, dict) or not isinstance(result.get("kind"), str):
            return "INVALID_RESPONSE", None
        if result["kind"] == "song":
            songs_returned += 1

    return "OK", songs_returned


def main():
    student_key = input("Student key: ").strip()
    seed = sum(ord(ch) for ch in student_key)

    if seed % 3 == 0:
        threshold = 15
    elif seed % 3 == 1:
        threshold = 12
    else:
        threshold = 9

    total_skus = 0
    reorder_count = 0

    while True:
        sku = input("SKU: ").strip()
        if sku.upper() == "DONE":
            break
        if not sku:
            continue

        on_hand = get_inventory_count()
        total_skus += 1
        if on_hand < threshold:
            reorder_count += 1
            print("REORDER")
        else:
            print("OK")

    term = "weezer" if seed % 2 == 0 else "drake"
    api_status, songs_returned = get_api_status(term)
    songs_output = songs_returned if api_status == "OK" else "N/A"

    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"SKUs entered: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {term}")
    print(f"Songs returned: {songs_output}")
    print(f"API status: {api_status}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye.")
        sys.exit(0)
