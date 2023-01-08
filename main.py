first = float(input("Zadejte cislo"))
second = float(input("Zadejte druhe cislo"))

print("Vyberte jednu z operaci")
print("[1] scitáni")
print("[2] odcitáni")
print("[3] nasobeni")
print("[4] deleni")
avadakabra = int(input(""))

if (avadakabra == 1):
    result = first + second
elif (avadakabra == 2):
    result = first - second
elif (avadakabra == 3):
    result = first * second
elif (avadakabra == 4):
    result = first / second
if avadakabra < 5 or avadakabra > 1:
    print("Vysledek: %f" % (result))
else:
    print("Musite vybrat operaci pro zadane cisla")