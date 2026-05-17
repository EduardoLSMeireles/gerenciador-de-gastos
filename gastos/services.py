import requests

def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()

        return {
            "dollar": float(dados["USDBRL"]["bid"]),
            "euro": float(dados["EURBRL"]["bid"]),
        }

    except requests.RequestException:
        return None
