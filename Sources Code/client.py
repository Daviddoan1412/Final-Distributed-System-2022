from distutils.log import error
import socket

def ClientSocket():
  port=int(input("Enter port:"))
  try:
      s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((socket.gethostname(),port))
      print("Connnect Successful")
      cmd = input("Group5:$ ")
      while True:
          s.send(cmd.encode("ascii"))
          data=s.recv(2048)
          print(data.decode("utf-8"))
          cmd=input("Group5:$")
  except socket.error as err:
      print("Not connecting",err)
  s.close()

if __name__ == '__main__':
  ClientSocket()

