# JokeAPI
API for creating jokes

## QUICK START
Clone repository from github
```Bash
git clone https://github.com/splinterpraim/JokeAPI.git
```
Create and Activate virtual environment
```Bash
python -m venv env
source env/bin/activate             (Linux)
env\Scripts\activate                (Windows)
cd JokeAPI

```
Then install dependencies
```Bash
pip install -r requirements.txt
```
Make migrate
```Bash
python manage.py migrate
```
And run server
```Bash
python manage.py runserver
```
## Endpoinds
### Actions
```
/api/v1/ - list of my jokes
/api/v1/{id}/ - Read, Delete, Update joke with {id}
/api/v1/create/ - Create your own joke
/api/v1/generate/ - Generate joke using a third party  API
```
### Authentication
```
/api/v1/rest-auth/login/ - Login user
/api/v1/rest-auth/logout/ - Logout user
/api/v1/rest-auth/registration/ - Registration user
```
### Other
```
/api/v1/schema - Show schema
/api/v1/docs - Show documetation
```
