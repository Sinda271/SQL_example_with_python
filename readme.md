# An SQL example with Python

## Description
Connect to SQL server via a python script, create a table from a csv file, and select information.

## Steps

### SQL server

1. Download MySQL installer https://dev.mysql.com/downloads/installer/
<img src="images/install_mysql_server.png" width="800" /> 

2. Proceed with installation (defaut params) and choose a root password
<img src="images/sql_pwd.png" width="800" /> 

3. Install MySQL Workbench from https://dev.mysql.com/downloads/workbench/ (leave default params)

4. Launch MySQL Workbench and then start root connection (type the password you created during the installation)
<img src="images/launch_mysqlworkbench.png" width="800" /> 

5. Check that SQL server is on (Launch PowerShell and run the following command: ***Get-service -Name 'mysql*' ***) \
Output:
<img src="images/check_mysql_running.png" width="800" /> 

6. Back to MySQL Workbench, create a new schema named ***walmart***
<img src="images/create_schema.png" width="800" /> 
<img src="images/create_schema2.png" width="800" /> 

7. Remove restrictions to load data from a csv file
    - Check my.ini file path 
    <img src="images/find_myini.png" width="800" /> 

    - Open Notepad as admin, then select File>Open 
    - Paste my.ini file path in file explorer and open it 
    - Remove the restriction by setting the the variable ***secure-file-priv*** to an empty string: ***secure-file-priv=""*** 
    - Restart the root connection

### Python

1. Navigate to a working directory of your choice, open cmd in that directory, and clone the repository by running the following command line: ***git clone https://github.com/Sinda271/SQL_example_with_python.git ***

2. Navigate to the repositoty folder: ***cd SQL_example_with_python***

3. Open vscode by running: ***code .*** (for those who don't have vscode, install it. It's very simple and light)

4. Close the cmd and open a terminal in vscode 
<img src="images/open_terminal1.png" width="800" /> 
<img src="images/open_terminal2.png" width="800" /> 

5. Create python virtual environment by running the following command line: ***python -m venv env*** 

6. Activate the virtual environment by running the following command line: ***.\env\Scripts\activate***

7. Install requirements by running the following command line: ***pip install -r requirements.txt***

8. Open ***TPsql.py*** and replace your username and password in the config 
<img src="images/replace_username_pwd.png" width="800" /> 

9. Replace csv file path
<img src="images/replace_csv.png" width="800" /> 


10. In the terminal run: ***python .\TPsql.py -h*** or ***python .\TPsql.py --help*** to grasp how to run the script




