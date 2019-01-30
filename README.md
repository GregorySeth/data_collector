# data_collector

To see how this app work visit - https://gregorydatacollector.herokuapp.com/


To make application work smoothly, you need to create file 'password.py' with your credentials for mail account (tested only on gmail)

It should look like:

"
from_email = "youremail@gmail.com"
from_password = "your password (in gmail you need to activate two-step verification and add new application - there you'll get the temporary password to put in here)"
"

and it should be put where collector.py file is located
