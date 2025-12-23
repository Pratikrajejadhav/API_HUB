from api.api_client import APIClient
print(APIClient().send('https://jsonplaceholder.typicode.com/posts/1','GET').data)
