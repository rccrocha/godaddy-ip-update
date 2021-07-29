from godaddypy import Client, Account
from requests import get

my_acct = Account(api_key='YOUR-ACCESS-KEY', api_secret='YOUR-SECRET-KEY')
client = Client(my_acct)

publicIP = get('https://api.ipify.org').text

domains = []

domains.append(client.get_domains())

for a in domains:
	get_records = client.get_records(a, record_type='A')
	if get_records[0]['data'] == publicIP:
		print (f"Domain: {a} -> record type A IP is not different from {publicIP}")
	else:
		print (f"""Current record type A IP for {a} is not equal to {publicIP}

Current {a}'s IP: {get_records[0]['data']}
""")
    
		update_ip       = client.update_ip(publicIP, domains=[a])
		get_updated_rec = client.get_records(a, record_type='A')
    
		print (f"New {a}'s IP: {get_updated_rec[0]['data']}")
