## dnsupdater

dnsupdater updates a given *private* DNS zone in Azure

For the code to work, you need to be logged into Azure with az cli (which needs to be installed by e.g. using  curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash)

do az login prior to starting the script

#### Other things you need:
* Python: probably installed already
* Pip: sudo apt install python-pip
* flask-restful:  pip install flask-restful

Run the script with:

**python server.py**
