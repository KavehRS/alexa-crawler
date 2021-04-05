# alexa-crawler (python 3.8.5)
 

## Introduction
A crawler that takes a list of sites and extracts information about them from the Alexa.com 



## Help

1- Update (For debian base OS) :

    sudo apt update && sudo apt -y upgrade

2- Install Python package manager :

    sudo apt install python3-pip

3- Install virtualenv :

    pip3 install virtualenv

4- Create Virtualenv:

    virtualenv crawler-env
    
5- Activate Virtualenv:

On windows:

    virtualenv crawler-env\script\activate

On Linux:

    source crawler-env/bin/activate
    
6- Install requirements:

    pip3 install -r requirements.txt
    
7- Install chromium chromedriver

	sudo apt install chromium-chromedriver


8- Create the file repository configuration:

    sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

9- Import the repository signing key:

    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

10- Update the package lists:

    sudo apt-get update

11- Install the latest version of PostgreSQL. If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':

    sudo apt-get -y install postgresql

12-  the cluster will not be running as a systemd service. Consider using systemctl:

    sudo systemctl start postgresql@13-main

Warn: You must run this program as the cluster owner (postgres) or root

13- start the database server using:

    pg_ctlcluster 13 main start

14- Install "pgadmin3" Package on Ubuntu

	sudo apt-get update -y
	sudo apt-get install -y pgadmin3

15- To connect to PostgreSQL using the postgres role, you switch over to the postgres account on your server by typing:

	sudo -i -u postgres

16- you can access the PostgreSQL using the psql by typing the following command:

	$ psql

17- create the dvdrental database using the CREATE DATABASE statement:

	postgres=# create database alexa;

18- quit the psql by using the \q command:

	postgres=# \q

19- switch to the dvdental database:

	postgres=# \c dvdrental

20- enter the following command to get the number of films in the film table:

	dvdrental=# select count(*) from film;






###   Edit  "input" path in main.py line 14

###   Edit  "webdriver.Chrome" path in main.py line 25

###  Edit  "output" path in main.py line 87

###  Run crawler.py with Python3 



## License

Kaveh RezaeiShiraz 2021 - The GNU GENERAL PUBLIC LICENSE (GPL v.3). Please see [License File](LICENSE.md) for more information.

