import requests

response = requests.get(url='https://sds.steemworld.org/communities_api/getCommunitiesByCountActivePosts').json()
cols_res = response['result']['cols']
rows_res = response['result']['rows']

print(rows_res)

