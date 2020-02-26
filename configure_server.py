"""
File Name  : configure_server.py
Description: Configure servers based on user configuration
"""

from sys import argv

import yaml
import socket
import logging
from ssh2.session import Session

#set up log level
logging.basicConfig(level=logging.INFO)



# Config params
SERVER = []
USERNAME = " "
PASSWORD = " "
TASKS = []

def listToString(s):
    """
           Function to convert list to string
           :param : list
           :return: string
    """
    str1 = ""
    #traverse in list
    for ele in s:
        str1 += ele
        str1.strip('\n')

    return str1


def configure_server():
    """
        Function to configure servers
        :param :

    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    sock.connect((listToString(SERVER[0]), 22))
    # assign to session class
    session = Session()

    # set up 3 way handshake
    logging.info('Setting up 3-way handshake')
    session.handshake(sock)
    logging.debug('Username is %s', USERNAME)
    logging.debug('password %s', PASSWORD)


    session.userauth_password(USERNAME, PASSWORD)
    channel = session.open_session()
    channel.execute("apt-get update -y; apt-get install apache2 -y; systemctl start apache2.service")
    size, data = channel.read()
    # while (size > 0):
    #     print(data.decode())
    #     size, data = channel.read()

    channel.close()
    print("Exit status : {0}", format(channel.get_exit_status()))


def parse_configuration(f, docs):
    """
               Function to parse yaml configuration file
               :param : file,attributes

    """

    global USERNAME
    global PASSWORD
    for doc in docs:

        for key, value in doc.items():
            logging.debug(key, "->", value)

            if key == "hosts" and value[0] == "webservers":
                with open(r'C:\Users\rajpo\PycharmProjects\SlackProj\hosts')as hostfile:
                    # if 'webservers' in hostfile.read():
                    for line in hostfile:
                        if 'webservers' in line:
                            for line in hostfile:
                                SERVER.append(line.strip().split('\t'))

                                logging.debug('Servers are %s', SERVER)

            if key == "username":
                USERNAME = listToString(value)
                logging.debug('Username is %s', USERNAME)

            if key == "password":
                PASSWORD = listToString(value)

            if key == "tasks":
                for line in f:
                    TASKS.append(line)
                    logging.debug('Tasks are %s', TASKS)

        # configure servers
    configure_server()


def main():
    """
            main function
    """

    # access config file

    try:

        with open(r'configuration.yml') as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            # function to parse yaml file
            print(docs)
            parse_configuration(f, docs)
    except IOError:
        logging.error('Cannot find Configuration file -configuration.yml')

        exit()


if __name__ == "__main__":
    main()
