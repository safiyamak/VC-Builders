import requests

url = "https://chatgpt146.p.rapidapi.com/q"

payload = { "prompt": "What is the meaning of life?" } #include the prompt here
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "chatgpt146.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())