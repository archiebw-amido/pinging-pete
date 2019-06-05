import slack
import argparse
import requests

# Declare command-line flags.
argparser = argparse.ArgumentParser()
argparser.add_argument('slack_api_token', help='The slack API token for authentication.')
argparser.add_argument('email', help='Email of the user to send cats.')
argparser.add_argument('number_of_cats', help='The number of cats')

args = argparser.parse_args()
slack_api_token = args.slack_api_token
email = args.email
number_of_cats = args.number_of_cats

client = slack.WebClient(token=slack_api_token)

response = client.users_lookupByEmail(email=email)

id = response.data['user']['id']

channel = client.im_open(user=id).data['channel']['id']

def send_cat():
	r = requests.get('http://aws.random.cat/meow')
	img = r.json()['file']

	message = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f'<@{id}> HeY, My NaMe Is PiNgInG PeTe, NiCe To MeEt You!! :wave: :wave:'
			}
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "cat"
			},
			"image_url": f'{img}',
			"alt_text": "missing_cat"
		}
	]

	client.chat_postMessage(channel=channel, blocks=message)

for req in range(1, number_of_cats): 
	send_cat()
