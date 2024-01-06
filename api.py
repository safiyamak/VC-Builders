import requests

url = "https://chatgpt146.p.rapidapi.com/q"

payload = { "prompt": "What is the meaning of life?" } #include the prompt here
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "5af49fa643mshe938c5f470d795ep1043e7jsnc7b149f729ee",
	"X-RapidAPI-Host": "chatgpt146.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())