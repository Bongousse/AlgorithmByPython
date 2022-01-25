#
# Complete the 'getVoteCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING cityName
#  2. INTEGER estimatedCost
#  API URL: https://jsonmock.hackerrank.com/api/food_outlets?city=<cityName>&estimated_cost=<estimatedCost>
#
import json

from pip._vendor import requests


def getVoteCount(cityName, estimatedCost):
    # Write your code here
    uri = f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost{estimatedCost}"
    response = requests.get(uri)
    result = json.loads(response.content)
    total_pages = result["total_pages"]
    sum_vote_count = 0
    for page_index in range(1, total_pages + 1):
        uri = f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost{estimatedCost}&page={page_index}"
        response = requests.get(uri)
        result = json.loads(response.content)
        data = result["data"]
        for record in data:
            if record["estimated_cost"] == estimatedCost:
                sum_vote_count += record["user_rating"]["votes"]
    return sum_vote_count if sum_vote_count != 0 else -1


print(getVoteCount("Seattle", 110))