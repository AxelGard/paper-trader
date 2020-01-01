import json
import requests

def api_link():
    """ main the link for the API """
    link = "https://paper-api.alpaca.markets/"
    return link

def authentication_header():
    with open('key.json', 'r') as file:
        header = json.load(file)
    return header

def get_request(link):
    """ takes a str link and sends a GET request to
    the api return then the response """
    url = api_link() + str(link)
    response = requests.get(url, headers=authentication_header())
    return response


def patch_request(link, payload=None):
    """ takes a str link and a dict payload that has the defult value none
    and makes a patch request to the link with the given payload """
    url = api_link() + str(link)
    response = requests.patch(url, json=payload, headers=authentication_header())
    return response


def post_request(link, payload=None):
    """ takes a str link and a dict payload that has the defult value none and
    makes a post request to the link with the given payload """
    url = api_link() + str(link)
    response = requests.post(url, json=payload, headers=authentication_header())
    return response


def delete_request(link, payload=None):
    """ takes a str link can take a payload with defult value of none and makes a delete request to the given link """
    url = api_link() + str(link)
    response = requests.delete(url, json=payload, headers=authentication_header())
    return response

"""
data API
"""

def data_api_link():
    """ second api link """
    endpoint = "https://data.alpaca.markets/v1/bars/day"
    return endpoint

def get_data(params):
    """  """
    url = data_api_link()
    header = authentication_header()
    response = requests.get(url, params=params, headers=header)
    return response
