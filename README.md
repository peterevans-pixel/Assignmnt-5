# Assignment 5

This repository includes the two Python programs for Assignment 5.

## Files
- `pos_checkout.py` — point-of-sale checkout system with validation, totals, discount logic, and seed-based perk.
- `inventory_spotcheck.py` — inventory reorder analyzer with input validation and an iTunes Search API spot check.

## Install dependency
Install `requests` before running the inventory analyzer:

```bash
pip install requests
```

## Run the programs
```bash
python pos_checkout.py
python inventory_spotcheck.py
```

## Example run: `pos_checkout.py`
Example inputs: student key `abc`, Notebook at `$12.50` quantity `2`, Coffee at `$4.50` quantity `3`, then `DONE`.

```text
Seed: 294
Units: 5
Subtotal: $38.50
Discount: 0%
Perk applied: NO
Total: $38.50
```

## Example run: `inventory_spotcheck.py`
Example inputs: student key `abc`, SKU `A101` with `10` on hand, SKU `B205` with `20` on hand, then `DONE`.
The API song count can vary depending on the response from iTunes.

```text
REORDER
OK
Seed: 294
Threshold: 15
SKUs entered: 2
Reorder flagged: 1
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
