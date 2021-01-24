# ***PUR BEURRE***

## ***(Create a platform for Nutella lovers)***  

## PROJECT PRESENTATION

This project is a web plateform that will allow anyone to find a healthy substitute for a food considered "Too fatty, too sweet, too salty". It's my realization of project 8 of the python application developer path from [openclassrooms](https://openclassrooms.com/).

## DOWNLOAD AND RUN THE PROJECT

1.  Clone the project
    
    git clone https://github.com/vector22/projet8

2.  Create a virtual environment and activate it

    cd projet8 && virtualenv -p python3.7 env  
    source env/bin/activate

3. Install requirements file

    pip install -r requirements.txt

4. Migrate the database
    
    ./manage.py migrate

5.  Create a super user

    ./manage.py createsuperuser

6.  Load demo data for development use

    ./manage.py loaddata food/dumps/food.json

7. Run the development server

    ./manage.py runserver


## DOWNLOAD DATAS MANUALY FROM OPEN FOOD FACT
