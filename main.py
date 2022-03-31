from bs4 import BeautifulSoup
import requests

def main():

    site_input = input("Digite o site que deseja fazer scrapping: ")

    req = requests.get(site_input).content
    # recebe o conteúdo da requisição http do site
    soup = BeautifulSoup(req, "html.parser")

    print("Html da página:", soup.title.string)

    #printando o html do site
    print(soup.prettify())

if __name__ == '__main__':
    main()

