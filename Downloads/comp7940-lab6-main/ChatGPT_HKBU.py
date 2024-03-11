import configparser
import requests

class HKBU_ChatGPT():
	def submit(self,message):
		conversation = [{"role": "user", "content": message}]
		url = "https://chatgpt.hkbu.edu.hk/general/rest/deployments/gpt-4-turbo/chat/completions/?api-version=2023-12-01-preview"
		headers = { 'Content-Type': 'application/json', 'api-key':'9f72f5f8-fcdc-4052-a80c-cf8c906b1955' }
		payload = { 'messages': conversation }
		response = requests.post(url, json=payload, headers=headers)
		if response.status_code == 200:
			data = response.json()
			return data['choices'][0]['message']['content']
		else:
			return 'Error:', response


if __name__ == '__main__':
	ChatGPT_test = HKBU_ChatGPT()

	while True:
		user_input = input("Typing anything to ChatGPT:\t")
		response = ChatGPT_test.submit(user_input)
		print(response)
