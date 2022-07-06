import json

import requests

response = requests.get(url='https://sds0.steemworld.org/feeds_api/getActiveCommunityAuthorReport/hive-101145/skuld2000').json()
result = response['result']
comments_count = result["total_comment_count"]


print(comments_count)
