#!/usr/bin/python3
#
# ----------------------------------------------------------------------------
# "LICENCE BEERWARE" (Révision 42):
# <dev@tharyrok.eu> a créé ce fichier. Tant que vous conservez cet avertissement,
# vous pouvez faire ce que vous voulez de ce truc. Si on se rencontre un jour et
# que vous pensez que ce truc vaut le coup, vous pouvez me payer une bière en
# retour. Tharyrok
# ----------------------------------------------------------------------------
#
import time
import ts3
from config import *

groups = { 'general': 13, 'visitor': 8, 'host': 22, 'overwatch': 51 }


with ts3.query.TS3Connection(server) as ts3conn:
	ts3conn.login(
		client_login_name=username,
		client_login_password=password
	)
	ts3conn.use(sid=1)

	# Register for events
	ts3conn.servernotifyregister(event="server")
	ts3conn.clientupdate(client_nickname=nickname)

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
						ts3conn.clientpoke(msg="Bonjour, merci de patienter le temps qu'un responsable vienne vous voir.", clid=event[0]["clid"])
						for client in ts3conn.clientlist(groups=True):
							if client['client_type'] is str('0'):
								if str(groups['general']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
								elif str(groups['host']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
								elif str(groups['overwatch']) in client['client_servergroups']:
									ts3conn.sendtextmessage(targetmode=1, target=client["clid"], msg="Hey il y a %s qui viens d'arriver comme visteur" % event[0]["client_nickname"])
