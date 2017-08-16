from socket import AF_INET, AF_INET6, getaddrinfo, SOCK_STREAM, inet_pton


def is_ipv4(address):
    try:
        inet_pton(AF_INET, address)
    except:
        return False
    return True


def is_ipv6(address):
    if is_ipv4(address):
        return True
    try:
        inet_pton(AF_INET6, address)
    except:
        return False
    return True

is_ip = is_ipv6