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
    # def split_value(self,split_str):
    #     try:
    #         res=re.split(split_str,self.value)[1].split()[0]
    #     except:
    #         res=None
    #     return  None
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
            print(self.value)
            hw_addr=re.findall('[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}',value)
            print(hw_addr)
            data1=re.findall('(\w|\s)+:[^:]]',value)
            print(data1)
            self.link_encap   =re.split(r'Link\s+encap:',self.value)[1].split()[0]
            self.hw_addr      =re.split('HWaddr\s+',self.value)[1].split()[0]
            self.inet_addr    =re.split('inet\s+addr:',self.value)[1].split()[0]
            self.bcast        =re.split('Bcast:',self.value)[1].split()[0]
            self.mask         =re.split('Mask:',self.value)[1].split()[0]
            # self.inet6_addr   =re.split('inet6 addr:\s+',self.value)[1].split()[0]
            # self.scope        =re.split('Scope:',self.value)[1].split()[0]
            # self.scope = split_value(self, 'Scope:')
            self.mtu          =re.split('MTU:',self.value)[1].split()[0]
            self.metric       =re.split('Metric:',self.value)[1].split()[0]
            self.rx_packets   =re.split('RX\s+packets:',self.value)[1].split()[0]
            self.tx_packets   =re.split('TX\s+packets:',self.value)[1].split()[0]
            self.rx_bytes     =re.split('RX\s+bytes:',self.value)[1].split()[0]
            self.tx_bytes     =re.split('TX\s+bytes:',self.value)[1].split()[0]
            net_info_dict={
                            "name":self.name,
                            "link_encap":self.link_encap,
                            "hw_addr":self.hw_addr,
                            "inet_addr":self.inet_addr,
                           "bcast":self.bcast,
                            "mask":self.mask,
                           # "inet6_addr":self.inet6_addr,
                           #  "scope":self.scope,
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
print(network_play_info)