from api.api_client import APIClient

client = APIClient()

payload = {
    "title": "Suspicious Activity Detected",
    "body": "Multiple failed login attempts from same IP",
    "userId": 99
}

response = client.send(
    "https://jsonplaceholder.typicode.com/posts",  # endpoint
    "POST",                                        # method
    payload,                                       # payload
    {
        "Content-Type": "application/json"
    }
)

print("Status:", response.status)
print("Response Data:", response.data)
