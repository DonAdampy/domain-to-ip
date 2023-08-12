import requests

def main():
    url = input("Entrez l'URL du site : ")
    response = requests.get(url)

    if response.status_code == 200:
        ip_address = response.headers.get('X-Forwarded-For')
        page_content = response.text

        print(f"Adresse IP du site : {ip_address}")
        print("Contenu de la page :")
        print(page_content)
    else:
        print("La requête n'a pas abouti.")

if __name__ == "__main__":
    main()
