#MyCMTool

##Introduction
A rudimentary configuration management tool to configure two servers for production service of a simple PHP web application


##Commands
python configure_server.py


##Usage

Format : python configure_server.py

File "configuration.yml" is the the name of the file to give configurations
Format : Can change values of fields hosts,username,password and tasks.

File "hosts" is provided to define the ip addresses of servers in type of servers.
Format: [webservers]
1.1.1.1
3.3.3.3

File bootsrap.sh mentions the dependencies required in the server

