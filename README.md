# alexa-crawler

1- Update (For debian base OS) :

    sudo apt update && sudo apt -y upgrade

2- Install Python package manager :

    sudo apt install python3-pip

3- Install virtualenv :

    pip install virtualenv

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

8-   Edit  "input" path in main.py line 14

9-   Edit  "webdriver.Chrome" path in main.py line 25

10-  Edit  "output" path in main.py line 87


