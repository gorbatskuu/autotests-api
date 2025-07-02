import httpx

data = {
    "email": "test@gmail.com",
    "password": "test"
}
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=data)

print(response.status_code)  # 201 (Created)
print(response.json())
token = response.json()['token']['accessToken']

headers = {"Authorization": f"Bearer {token}"}

response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)
print(response.status_code)
print(response.json())

