from bs4 import BeautifulSoup
import requests
import json


def main():
    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # <--- Úkol: popiš krátce, co tohle dělá
    # Je to funkce která přeloží stránku pro kód do html

    cesnecka = soup.find_all("h2")

    list = []
    finale = []

    for ingredient in cesnecka:
        list.append(ingredient.text)

    finale.append(list[0])
    finale.append(list[1])
    finale.append(list[2])
    finale.append(list[3])
    # U: nebyl by cyklus elegantnější?

    print(finale)

    with open("recept.json", mode="w") as file:
        json.dump(finale, file)


if __name__ == "__main__":
    main()
