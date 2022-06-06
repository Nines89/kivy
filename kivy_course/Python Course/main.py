
def dict_examples():
    ########################### DICTIONARY #################################à
    person = {"name": "Paolo", "age": 25, "h": 182}
    k = person["name"]
    print('prima prova: ', k)

    for i in person:
        print(i)  # print key
        print(person[i])  # print values
        print(f'key: {i} - value: {person[i]}')  # print tutto

    person_dict = {
        "Paolo": (25, 100),
        "Ciccio": (10, 123),
    }

    infos = person_dict["Paolo"]
    print(infos)
    ###########################  #################################à

class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

pizzas = [
    Pizza("Calzone", 8),
    Pizza("4 formaggi", 8.5),
    Pizza("Hawai", 18)
]

def adv_structures_examples():
    pizza_names = [i.name for i in pizzas if len(i.name) > 5 ]
    print(pizza_names)
    # any ritorna True se un elemento è True

    print(any([False, False, False]))
    print(any([False, False, True]))

    expensive_pizza_exist = any([i.price > 10 for i in pizzas])
    print("Costose? ",expensive_pizza_exist)

    #sum fa la somma di una lista di numeri
    print(sum([10, 5, 2]))
    #Questo uso è bellissimo  sommo 1 per ogni pizza il cui prezzo è sopra i 10
    expensive_pizza_numero = sum([1 for i in pizzas if i.price > 10])
    print(expensive_pizza_numero)

def zip_examples():
    #zip raggruppa più liste in un'unica lista
    #funziona anche su più liste
    pizza_names = ("Calzone", "4 formaggi", "Hawai")
    pizza_price = (10.5, 11 ,9)

    #senza list non lo stampa
    names_and_prices = list(zip(pizza_names, pizza_price))
    print(names_and_prices)

    #si può anche dezippare
    unzip = list(zip(*names_and_prices))
    print(unzip)


if __name__ == '__main__':
    zip_examples()
