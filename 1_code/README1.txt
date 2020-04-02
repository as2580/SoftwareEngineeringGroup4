Running Task Manager/Task Board/Check Out App
 
Ensure Python3 and Django are installed
Navigate to DjangoApp folder
In DjangoApp folder modify ALLOWED_HOSTS in settings.py to include {serverIP}
If you want to be able to access the App from other computers on the same network, ensure {port} is allowed through firewall
If you want to be able to access the App from over the internet, ensure {serverIP}:{port} allows port forwarding
run "python3 manage.py runserver 0.0.0.0:{port}"

To access desired app (task_manager, task_board, check_out) on a browser navigate to "http://{serverIP}:{port}/{app}/"


Running Price Checker

run "pricecheckertest.py"
input RFIDs found in user documentation


Running Item Locator

Ensure Python3 and HTML
run "getLocation.py"
input an item 
Than,
run "itemFinder.html"
