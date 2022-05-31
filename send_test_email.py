import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox3ecb5d24f9a3481b8c0039be6af2bf02.mailgun.org/messages",
        auth=("api", "0ca046a74f8caa9e28c86a896e737105-27a562f9-181f912a"),
        data={"from": 'applesupport@apple.com',
            "to": ['victorofish@gmail.com'],
            "subject": "Atualize seus dados de pagamento",
            "html": "<html> esteve presente hj!. </html>"})
                      


# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandbox3ecb5d24f9a3481b8c0039be6af2bf02.mailgun.org/messages",
# 		auth=("api", "0ca046a74f8caa9e28c86a896e737105-27a562f9-181f912a"),
# 		data={"from": "Excited User <mailgun@sandbox3ecb5d24f9a3481b8c0039be6af2bf02.mailgun.org>",
# 			"to": ["vitormiura3@gmail.com"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})

request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))