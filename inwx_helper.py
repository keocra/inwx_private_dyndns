def check_domain_existing(nameserver_check_result, domain):
    if not nameserver_check_result or not domain:
        return False, None

    if not isinstance(nameserver_check_result, dict):
        return False, None

    entry_list = nameserver_check_result["resData"]["record"]

    if not isinstance(entry_list, list):
        return False, None

    for obj in entry_list:
        if "name" in obj and obj["name"] == domain:
            return True, obj

    return False, None


def compare_ips(domain_obj, ip):
    return domain_obj["content"] == ip


def split_domain(domain):
    first_dot = domain.find(".")

    return domain[0:first_dot], domain[first_dot + 1:]
