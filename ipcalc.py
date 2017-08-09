'''
Данный скрипт производит вычисление ip подсетей по Ip адресу и маске
IP
Bitmask
Netmask
Wildcard
Network
Broadcast
Hostmin
Hostmax
Hosts
Networks
'''
IP = tuple(map(int,'192.168.3.200'.split('.'))) #IP адрес хоста, рпзбитый на группы и записанный в список

BITMASK = 22 #Маска подсети (max  32, min 1)

NETMASK = [255,255,255,255] #Значение netmask по умолчанию
#Определяем netmask по bitmask
#Пример bitmask = 24, netmask = 255.255.255.0
noctet = BITMASK//8 #Кол-во групп в которых netmask равен 255 (Значение изменяется от 0-4)
foctet = noctet*8 #Кол-во разрядов в всех группах по 255
sign1 = BITMASK - foctet #Кол-во 1 в последней значащей группе (в группе где netmask между 0 и 255)
sign0 = 8 - sign1 #Кол-во 0 в последней значащей группе
mask = '1' * sign1 + '0' * sign0 #Netmask последней значащей группы

hosts_amount = pow(2,32-BITMASK) - 2
#networks_amount = pow()

#К группам где маска равна 255, маска не применяется.
#Определяем параметер Network (ip адрес сети) и Netmask
if noctet == 0 :
    NETMASK[noctet] = int(mask, 2)
    for x in range(1,4):
        NETMASK[x] = 0
elif noctet < 4:
    NETMASK[noctet] = int(mask, 2)
    for x in range(noctet+1,4):
        NETMASK[x] = 0
#Маска хостов
HOSTMASK = tuple(255 - x for x in NETMASK)

#IP адрес сети
def netip():
    netip = list(IP)
    for group in range(4):
       netip[group] &= NETMASK[group]
    #netip = [a & b for a in netip for b in NETMASK ]
    return netip
#Broadcast
def broadcastip():
    broadcastip = list(IP)
    for group in range(4):
        broadcastip[group] |= HOSTMASK[group]
    return broadcastip
#Hostmax
def hostmax():
    hostmax = broadcastip().copy()
    hostmax[3] -= 1
    return hostmax
#Hostmin
def hostmin():
    hostmin = netip().copy()
    hostmin[3] += 1
    return hostmin

class ipcalc:
    '''
    ipAddress - ip адрес хоста
    netmask - маска сети (пример 255.255.255.255)
    bitmask - разрядность маски. Маска в нотации CIDR (rfc1517)
    netAddress -
    '''
    def __init__(self,ipAddress,netmask):
        pass
    def setIpaddress(self, ipAddress):
        '''
        Метод присваивает значение для внутренней переменной ipAddress
        :return:
        '''
        self.ipAddress = ipAddress
    def getNetmask(self):
        pass
    def getHostMin(self):
        pass
    def getHostMax(self):
        pass
    def getNet(self):
        pass

print('NetIP: {0}'.format('.'.join(map(str,netip()))))
print('BroadcastIP: {0}'.format('.'.join(map(str,broadcastip()))))
print('Hostmin: {0}'.format('.'.join(map(str,hostmin()))))
print('Hostmax: {0}'.format('.'.join(map(str,hostmax()))))
print('Netmask: {0}'.format('.'.join(map(str,NETMASK))))
print('Hosts amount: {0}'.format(hosts_amount))