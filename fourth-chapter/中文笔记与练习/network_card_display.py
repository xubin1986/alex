info='''docker0   Link encap:Ethernet  HWaddr 02:42:87:ef:c6:bc
          inet addr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

eth0      Link encap:Ethernet  HWaddr 00:0c:29:eb:d7:33
          inet addr:192.168.131.101  Bcast:192.168.131.255  Mask:255.255.255.0
          inet6 addr: fe80::20c:29ff:feeb:d733/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:7424 errors:0 dropped:0 overruns:0 frame:0
          TX packets:3978 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:625076 (625.0 KB)  TX bytes:569191 (569.1 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

'''
import subprocess,re
# info=subprocess.getoutput('ifconfig')
class NetworkCard:
    def __init__(self,info):
        self.info=info
    def split_value(self,split_str):
        try:
            res=re.split(split_str,self.value)[1].split()[0]
        except:
            res=None
        return  res
    def get_ip(self,netcard_name):
        return self.get_info()[netcard_name]['inet_addr']
    def get_hwaddr(self,netcard_name):
        return self.get_info()[netcard_name]['hw_addr']
    def get_info(self):
        network_card_info_dict = {}
        data_element=self.info.split("\n\n")
        for index,value in enumerate(data_element):
            self.value=value
            net_info_dict = {}
            if not self.value:
                continue
            self.name=self.value.split()[0]
            if self.name == "lo":
                continue
            # dic1={"link_encap":'Link\s+encap:',}
            self.link_encap = NetworkCard.split_value(self,'Link\s+encap:')
            self.hw_addr = NetworkCard.split_value(self,'HWaddr\s+')
            self.inet_addr = NetworkCard.split_value(self,'inet\s+addr:')
            self.bcast = NetworkCard.split_value(self,'Bcast:')
            self.mask = NetworkCard.split_value(self, 'Mask:')
            self.inet6_addr = NetworkCard.split_value(self,'inet6 addr:\s+')
            self.scope = NetworkCard.split_value(self, 'Scope:')
            self.mtu = NetworkCard.split_value(self, 'MTU:')
            self.metric = NetworkCard.split_value(self, 'Metric:')
            self.rx_packets=NetworkCard.split_value(self, 'RX\s+packets:')
            self.tx_packets = NetworkCard.split_value(self,'TX\s+packets:')
            self.rx_bytes = NetworkCard.split_value(self,'RX\s+bytes:')
            self.tx_bytes = NetworkCard.split_value(self,'TX\s+bytes:')
            net_info_dict={
                            "name":self.name,
                            "link_encap":self.link_encap,
                            "hw_addr":self.hw_addr,
                            "inet_addr":self.inet_addr,
                           "bcast":self.bcast,
                            "mask":self.mask,
                           "inet6_addr":self.inet6_addr,
                            "scope":self.scope,
                           # "status":self.status,
                            "stu":self.mtu,
                           "metric":self.metric,
                            "rx_packets":self.rx_packets,
                           "tx_packets":self.tx_packets,
                            "rx_bytes":self.rx_bytes,
                           "tx_bytes":self.tx_bytes
                           }
            network_card_info_dict[self.name]=net_info_dict
        return network_card_info_dict
network_card_obj=NetworkCard(info)
network_play_info=network_card_obj.get_info()
# print(network_play_info['eth0'])
print(network_card_obj.get_ip('eth0'))
print(network_card_obj.get_hwaddr('eth0'))