# To start flask in windows power shell

open the power shell in the folder where your project resides, create and activate virtual environment then install flask inside the virtual environment, and finally run the flask app

```
PS D:\projects\myproject> py -m venv env
PS D:\projects\myproject> env\Scripts\activate
(env) PS D:\projects\myproject> pip install flask
(env) PS D:\projects\myproject> $env:FLASK_APP ="app.py"
(env) PS D:\projects\myproject> set FLASK_ENV =development
(env) PS D:\projects\myproject> flask run
```

# Preparing files

add the .txt files of the show running configurations to the same folder of the "app.py" to let the application extract the IP Helper details and but it in a table
