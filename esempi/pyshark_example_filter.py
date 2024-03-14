#esempio di utilizzo di pyshark per aprile un file pcap e filtrare i pacchetti

import pyshark

#apre il file pcap
cap = pyshark.FileCapture('test.pcap')
#filtra i pacchetti con protocollo HTTP
http = [pkt for pkt in cap if 'http' in pkt]
#stampo il contenuto dei pacchetti
for pkt in http:
    print(pkt.http.body)