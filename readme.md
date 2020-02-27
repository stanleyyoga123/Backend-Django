### Setting Environment
I've set the virtual environment that include Django and Djangorestframework
```bash
venv\Scripts\activate
``` 

### Make Migration
Simply just run this command with the virtual environment activated
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

### Run Local Server
```bash
python manage.py runserver
```

### Get Users Data
You can use postman to get data by send GET request
```bash
{url}/users/
```
Where url is from heroku

### Post Users Data
POST method and fill the body with username, no_hp, password, first_name, and alamat

### Get Orders Data
```bash
{url}/orders/
```

### Post Orders Data
POST method and fill the body with order_trash_paper, order_trash_food, order_trash_plastic, user
default value of order_trash_paper, order_trash_food, order_trash_plastic are 0

### Get Collected Data
```bash
{url}/orders/
```

### Post Collected Data
Post method and fill the body with collected_trash_paper, collected_trash_food, collected_trash_plastic, user (foreign key from user)
default value of collected_trash_food, collected_trash_plastic, collected_trash_paper are 0
