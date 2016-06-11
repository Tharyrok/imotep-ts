#!/usr/bin/python3

import time
import ts3

groups = { 'general': 13, 'visitor': 8, 'host': 22, 'overwatch': 51 }


with ts3.query.TS3Connection("195.154.68.61") as ts3conn:
	ts3conn.login(
		client_login_name="YOUR LOGIN",
		client_login_password="YOUR PASSWORD"
	)
	ts3conn.use(sid=1)

	# Register for events
	ts3conn.servernotifyregister(event="server")
	ts3conn.clientupdate(client_nickname="Robot de la team2")

	while True:
		ts3conn.send_keepalive()
		try:
			event = ts3conn.wait_for_event(timeout=150)
		except ts3.query.TS3TimeoutError:
			pass
		else:
			if str("reasonid") in event[0]:
				if event[0]["reasonid"] is str('0'):
					if event[0]["client_servergroups"] in str(groups['visitor']) :
						ts3conn.clientmove(clid=event[0]["clid"], cid=10)
						ts3conn.sendtextmessage(targetmode=3, target=event[0]["clid"], msg="Bonjour, merci de patienter le temps qu'un responsable vienne vous voir.")
						for client in ts3conn.clientlist(groups=True):
							if client['client_type'] is str('0'):
								if str(groups['general']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
								elif str(groups['host']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
								elif str(groups['overwatch']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
