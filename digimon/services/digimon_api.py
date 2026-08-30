import requests

URL_BASE = 'https://digi-api.com/api/v1'


class DigimonAPIError(Exception):
    """Erro controlado ao consultar a Digi-API."""


def _get_json(endpoint, params=None):
    try:
        response = requests.get(f'{URL_BASE}{endpoint}', params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as error:
        # Trata timeout, falha de conexão, HTTP inválido e JSON malformado.
        raise DigimonAPIError from error


#Função para conseguir uma lista paginada de digimons
def get_digimons(page=0, page_size=15):
    return _get_json(
        '/digimon',
        params={
            'page': page,
            'pageSize': page_size,
        },
    )


def get_digimon(digimon_id):
    return _get_json(f'/digimon/{digimon_id}')
