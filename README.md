**Python 3 script that searches for Lenovo laptop information given the serial number**

1) Ensure Python, Selenium, and the Selenium Chrome Driver are installed. The Chrome Driver download will vary (MacOS, Linux, Windows)

2) In "LenovoSearch.py", replace the following 
```
service = Service(executable_path = "./chromedriver") 
```
with the path of where your driver is installed. For Windows, it may be "chromedriver.exe"

3) Give the script executable permissions (if not already)

4) Run the script with the laptop serial number as the argument

***The script gives you information on the following***
Device Info (serial #, model)
Warranty Info (Type, Start, End)
Spec Info (processor, memory, os, etc.)

