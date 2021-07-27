# godaddy-ip-update
It updates the `A` record type for Godaddy's domains based on your public IP.

## Commands

> **`get_domains()`** -> get all listed domains in your account.

> **`get_records(domain_name, record_type='', name='', ttl='')`** -> get all info from a specific domain. Not all options are necessary. Only domain_name is mandatory.

> **`update_ip(ip, domains=[''])`** -> update to the desired IP and for as many domains needed.

> **`add_record(desired_name_for_domain, {'data':'IP', 'name':'Record_Type_Name', 'ttl':Seconds, 'type':'Record_Type'})`**

> **`delete_records(domain_to_be_deleted, name='')`** -> If only domain name, whole domain will be deleted. If name, just the name.
