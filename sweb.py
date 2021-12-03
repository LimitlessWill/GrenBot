import socket

class hweb:
  result = "ok"
  def __init__(self,url="google.com"):
    self.host = url
    self.port = 80
    self.request = b"GET / HTTP/1.0\r\n\r\n"
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.ip = socket.gethostbyname(self.host)
    try:
      self.s.connect((self.ip , self.port))
    except:
      result = "connection error"

  def get_data(self):
    self.s.send(self.request)
    reply = ""
    while True:
      reply += self.s.recv(80**4)
      if(len(reply) <= 0):
          break
    result = "data"
    self.s.close()
    return reply
