import sys
from wit import Wit

# Usage: python manual.py YOURACCESSCODEFROMYOURACCOUNT

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + ' <wit-token>')
    exit(1)
access_token = sys.argv[1]

def send(request, response):
    print(response['text'])

actions = {
    'send': send,
}

client = Wit(access_token=access_token, actions=actions)
#client.interactive()

# each message being sent below should be configured in the online session

json = client.converse(access_token, 'Hi', {})
print('Yay, got Wit.ai response: ' + str(json))

json = client.converse(access_token, 'Shutup', {})
print('Yay, got Wit.ai response: ' + str(json))

# for more details on parsing, check wit.py __run_actions
print('Response type: %s' % resp['type'])
print("Response: %s" % json.get('msg').encode('utf8'))


# the below call run_actions which will print the response on the console (but doesn't return it back - TBD)

# context0 = {}
# context1 = client.run_actions(access_token, 'Hi', context0)
# print('The session state is now: ' + str(context1))
# context2 = client.run_actions(access_token, 'shutup', context1)
# print('The session state is now: ' + str(context2))

#context = client.run_actions(access_token, "shutup")
