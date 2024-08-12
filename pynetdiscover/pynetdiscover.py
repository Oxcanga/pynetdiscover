from scapy.all import ARP, Ether, srp

def ag_tarama(ip_araligi):

    arp_request = ARP(pdst=ip_araligi)
    
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    yanitlar, _ = srp(arp_request_broadcast, timeout=2, verbose=False)
    
    cihazlar = []
    for yanit in yanitlar:
        cihaz = {'ip': yanit[1].psrc, 'mac': yanit[1].hwsrc}
        cihazlar.append(cihaz)
    
    return cihazlar
