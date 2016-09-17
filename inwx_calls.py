# TODO: delete, create domain entry, update (delete+create)
from inwx_managed_python_lib.inwx import domrobot, prettyprint, getOTP


api_url = "https://api.domrobot.com/xmlrpc/"

class inwx:
    def __init__(self):
        self.inwx_conn = None

    def login(self, username, password):
        self.inwx_conn = domrobot(api_url, False)
        self.inwx_conn.account.login({'lang': 'en', 'user': username, 'pass': password})

        return True # TODO: check if login was successful

    def create_sub_domain(self, domain, tld, ip):
        create_result = self.inwx_conn.nameserver.createRecord({
            "type": "A",
            "content": ip,
            "name": domain,
            "domain": tld
        })

        print create_result

        return True # TODO: check if creation was successful

    def delete_sub_domain(self, domain_id):
        delete_result = self.inwx_conn.nameserver.deleteRecord({
            "id": domain_id
        })

        return True # TODO: check if delete was successful

    def update_sub_domain(self, domain, tld, domain_id, ip):
        if self.delete_sub_domain(domain_id):
            self.create_sub_domain(domain, tld, ip)

        return True # TODO: check if update was successful

    def get_domain_info(self, tld):
        return self.inwx_conn.nameserver.info({'domain': tld})
