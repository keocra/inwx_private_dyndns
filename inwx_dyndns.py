from flask import Flask, request

import json
import logging

from inwx_calls import inwx
import inwx_helper


IP = "0.0.0.0"
PORT = 4321

flask_log = logging.getLogger('werkzeug')
flask_log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
def catch_all(path):
	get_params = request.args

	username = get_params.get("username")
	password = get_params.get("password")
	domain = get_params.get("domain")
	ip = get_params.get("ip")

	inwx_conn = inwx()
	inwx_conn.login(username, password)

	domain, tld = inwx_helper.split_domain(domain)
	domain_info = inwx_conn.get_domain_info(tld)
	domain_existing, domain_obj = inwx_helper.check_domain_existing(domain_info, domain + "." + tld)

	if not domain_existing or not inwx_helper.compare_ips(domain_obj, ip):
		if domain_existing:
			inwx_conn.update_sub_domain(domain, tld, domain_obj["id"], ip)
			print "Subdomain %s.%s updated with ip %s" % (domain, tld, ip)
		else:
			inwx_conn.create_sub_domain(domain, tld, ip)
			print "Subdomain %s.%s created with ip %s" % (domain, tld, ip)
	else:
		print "No update needed for %s.%s" % (domain, tld)

	return ('', 204)


if __name__ == '__main__':
	print " * Running on http://%s:%s/ (Press CTRL+C to quit)" % (IP, PORT) 
	app.run(host=IP, port=PORT)
