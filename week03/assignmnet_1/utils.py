import re
import socket
import struct
import time
from socket import timeout

from ping3 import ping


def is_port_open(ip: str, port: int) -> bool:
    # 创建一个套接字对象 s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 套接字的阻塞操作设置超时时间，单位为秒
    s.settimeout(5)
    # loc 为地址簇。
    loc = (ip, port)
    # 如果连接失败则返回错误指示器，返回值为 0
    result = s.connect_ex(loc)
    # 关闭一个套接字文件描述符
    s.close()
    return result == 0


def ping_host(ip):
    # ping 的返回值是 ping 的时延，大于零则证明可以 ping 通。
    result = ping(ip, timeout=1)
    return type(result) == float and result > 0.0
 

def ip2int(addr):
    return struct.unpack("!L", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!L", addr))


def parse_ip_range(ip_range):
    matches = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\-(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$", ip_range)

    if matches is None:
        raise ValueError('bad format of ip range')

    ips = matches.groups()
    ip_int32_from = ip2int(ips[0])
    ip_int32_to = ip2int(ips[1])
    if ip_int32_from > ip_int32_to:
        raise ValueError('bad ip range')

    return ip_int32_from, ip_int32_to


def measure_time(func, *args):
    start_time = time.time()
    ret = func(*args)
    elapsed = time.time() - start_time
    return ret, elapsed
