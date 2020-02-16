### Setting Environment
I've set the virtual environment that include Django and Djangorestframework
```bash
venv\Scripts\activate
``` 

### Make Migration
Simply just run this command with the virtual environment activated
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server
```bash
python manage.py runserver
```

### Get Users Data
You can use postman to get data by send GET request
```bash
localhost/users/
```
Where localhost is your local server

### Post Users Data
On the postman, you can change into the POST method and fill the body with username, email, and password
