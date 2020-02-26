"""
File Name  : configure_server.py
Description: Configure servers based on user configuration
"""

from sys import argv

import yaml
import socket
from ssh2.session import Session


from pip._vendor.pep517.compat import FileNotFoundError


#Config params
SERVER= []
USERNAME = ""
PASSWORD = ""
TASKS = []

def configure_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER[0], 22))
    # assign to session class
    session = Session()

    # set up 3 way handshake
    session.handshake(sock)
    session.userauth_password(USERNAME, PASSWORD)

    channel = session.open_session()
    channel.execute("uname -a")
    size, data = channel.read()
    while (size > 0):
        print(data.decode())
        size, data = channel.read()

    channel.close()
    print("Exit status : {0}", format(channel.get_exit_status()))




def parse_configuration(f, docs) :
    for doc in docs:

        for key, value in doc.items():
            print(key, "->", value)

            if key == "hosts" and value[0] == "webservers":
                with open(r'C:\Users\rajpo\PycharmProjects\SlackProj\hosts')as hostfile:
                    # if 'webservers' in hostfile.read():
                    for line in hostfile:
                        if 'webservers' in line:
                            for line in hostfile:
                                SERVER.append(line)
                                print("Servers are", SERVER)

            if key == "username":
                UNAME = value
                print('Username is ',UNAME[0])
            if key == "password":
                PASSWORD = value
                print("password %s", PASSWORD)
            if key == "tasks":
                for line in f:
                    TASKS.append(line)
                    print(TASKS)

        #configure servers
      #  configure_server()



def main(var) :
    """
        main function
    """

    # access config file
    print(var)
    try :
        with open(r'C:\Users\rajpo\PycharmProjects\SlackProj\config.yml') as f:
         docs = yaml.load_all(f, Loader=yaml.FullLoader)
         # function to parse yaml file
         print(docs)
         parse_configuration(f, docs)
    except FileNotFoundError :
      
        exit()







if __name__ == "__main__" :
    
    main(argv[0])
