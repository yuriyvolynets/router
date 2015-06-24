# !/usr/bin/python

class TestRouter(object):
    def test_1(self, router_app):
        ip_addr = "192.168.1.1"
        router_app.set_ip_addr(ip_addr)

    def test_2(self, router_app):
        router_app.add_route()
        router_app.enable_dhcp()
