import requests

url = 'https://api.chucknorris.io/jokes/random'
#url = 'https://api.chucknorris.io/jokes/categories'

def conn_api_and_get_data(url):
    res = requests.get(url)
    if res.status_code < 400:
        data = res.json()
        return data
    else:
        return None

def conn_api_and_get_data_by_query(query):
    url = (f'https://api.chucknorris.io/jokes/search?query={query}')
    res = requests.get(url)
    if res.status_code < 400:
        data = res.json()
        return data
    else:
        return None

print(conn_api_and_get_data(url)['id'])
print(conn_api_and_get_data(url)['value'])
#get_num_categories = conn_api_and_get_data(url)
#print(conn_api_and_get_data_by_query(get_num_categories[2]))

