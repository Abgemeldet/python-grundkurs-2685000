#!/usr/bin/env python3
# Testen des JugendBankAccounts

from bank_account import JugendBankAccount

jugend_konto = JugendBankAccount("Max Mustermann Junior", "50")
print(jugend_konto)
jugend_konto.einzahlen(100)

try:
    jugend_konto.abheben(30)
except ValueError as e:
    print(e)

try:
    jugend_konto.abheben(20)
except ValueError as e:
    print(e)

print(jugend_konto.get_kontostand())