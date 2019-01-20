def krw_to_usd(won):
    return won / 1000
def usd_to_jpy(dollars):
    return dollars * 1000 / 8

amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국화폐 : " + str(amounts))

i = 0
while i < len(amounts):
    amounts[i] = int(krw_to_usd(amounts[i]))
    i += 1
print("미국화폐 : " + str(amounts))

i = 0
while i < len(amounts):
    amounts[i] = int(usd_to_jpy(amounts[i]))
    i += 1
print("일본화폐 : " + str(amounts))
