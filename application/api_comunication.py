import json
import requests

def api_link():
    """ keeps the link for the API """
    link = "https://paper-api.alpaca.markets/v2/"
    return link

def authentication_header():
    with open('../key.json', 'r') as file:
        header = json.load(file)
    return header

def get_request(link):
    """ takes a str link and sends a GET request to
    the api link and gets a json response """
    url = api_link() + str(link)
    response = requests.get(url, headers=authentication_header())
    if api_check(response, url):
        json_resp = response.json()
        return json_resp
    return response


def patch_request(link, payload=None):
    """ takes a str link and a dict payload and
    makes a patch request to the link with the given payload """
    url = api_link() + str(link)
    response = requests.patch(url, json=payload, headers=authentication_header())
    api_check(response, url)
    return response


def post_request(link, payload=None):
    """ takes a str link and a dict payload and
    makes a post request to the link with the given payload """
    url = api_link() + str(link)
    response = requests.post(url, json=payload, headers=authentication_header())
    api_check(response, url)
    return response


def delete_request(link, payload=None):
    """ takes a str link and makes a delete request to the given link """
    url = api_link() + str(link)
    response = requests.delete(url, json=payload, headers=authentication_header())
    api_check(response, url)
    return response


def api_check(response, url):
    """ a test for api requests,
    takes a requests response and a str url and check's if OK,
    if not sends error msg """
    return response.status_code == 200 or response.status_code == 204
