# Django USDA Demo
A demo project using [Django USDA][2].

## Installation
1. Create a new directory and open it:
  ```
    mkdir ~/django-usda
    cd ~/django-usda
  ```

2. Clone this repository:
  ```
    git clone https://github.com/Zundrium/django-usda-demo.git
  ```
  
3. Create a virtual enviornment and activate it:
  ```
    virtualenv demoenv
    source demoenv/bin/activate
  ```

4. Go into the project directory:
  ```
    cd django-usda-demo
  ```

5. Install required packages:
  ```
    pip install -r requirements.txt
  ```
  
6. Install Django USDA
  ```
    pip install git+https://github.com/zundrium/django-usda.git
  ```

7. [Download][1] the ASCII version of the 27th release of the USDA Nutrient Database.

8. Create the tables and import the zip file (This can take up to 10 minutes): 
  ```
    python manage.py migrate
    python manage.py import_r27 <path_to_zipfile>
  ```

9. Run the development server
  ```
    python manage.py runserver
  ```

10. Go to `http://localhost:8000/demo/` to see the demo. 

[1]: http://www.ars.usda.gov/Services/docs.htm?docid=24912
[2]: https://github.com/Zundrium/django-usda
