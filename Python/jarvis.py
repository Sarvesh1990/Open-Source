#!/usr/bin/python
import time
from slackclient import SlackClient

token = "xoxb-8492642517-kyXitQhmPyFeeUTfaN6kT8Gs"# found at https://api.slack.com/#auth)
# sc = SlackClient(token)
# if sc.rtm_connect():
#     while True:
#         print sc.rtm_read()
#         time.sleep(1)
# else:
#     print "Connection Failed, invalid token?"

sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="random")