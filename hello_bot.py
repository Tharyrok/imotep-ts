#!/usr/bin/python3

import time
import ts3
import pprint
import * from passwd.py

groups = { 'general': 13, 'visitor': 8, 'host': 22, 'overwatch': 51 }


with ts3.query.TS3Connection("ts.imotep-gaming.fr") as ts3conn:
		ts3conn.login(
			client_login_name=login,
			client_login_password=password
		)
		ts3conn.use(sid=1)

		# Register for events
		ts3conn.servernotifyregister(event="server")

		while True:
				event = ts3conn.wait_for_event()

				# Greet new clients.
				if event[0]["reasonid"] is "0":
					if event[0]["client_servergroups"] in str(groups['visitor']) :
						ts3conn.clientmove(clid=event[0]["clid"], cid=10)
						for client in ts3conn.clientlist(groups=True):
							if client['client_type'] is '0':
								if str(groups['general']) in client['client_servergroups'] :
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["clid"])
								elif str(groups['host']) in client['client_servergroups'] :
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["clid"])
								elif str(groups['overwatch']) in client['client_servergroups'] :
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["clid"])
