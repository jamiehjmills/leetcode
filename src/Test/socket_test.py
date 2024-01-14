# import socket
#
# target_host = "www.google.com"
#
# target_port = 80
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# client.connect((target_host, target_port))
# print("Connected...")
#
#
# request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
#
# response = client.recv(4096)
# http_response = repr(response)
# http_response_len = len(http_response)
#
# print("[+RECV+] - length %d" % http_response_len)
# print(http_response)
#
# client.send(request.encode())
