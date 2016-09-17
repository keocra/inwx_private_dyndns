# Simple DynDNS update tool for self-owned INWX domains

Usage:
* Run get-dependencies.sh to clone the inwx python library (Commit #af81cb860b9226354efc8984de08ad101795227d)
* Run ```python inwx_dyndns.py```
* Access your device ip at port 4321 (could be changed in the inwx_dyndns.py file)
    with get params username=\<INWX_USERNAME>, password=\<INWX_PASSWORD>, ip=\<IP TO SET>,
    domain=\<SUBDOMAIN TO UPDATE>
    i.e.: http://\<DEVICE IP>:4321?username=\<INWX_USERNAME>&password=\<INWX_PASSWORD>&ip=\<IP TO SET>&domain=\<SUBDOMAIN TO UPDATE>
