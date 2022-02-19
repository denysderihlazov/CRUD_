CRUD

This is a CRUD application based on Django(backend) and Vue.js(frontend). 
CRUD is short of Create Read Update Delete.

### How to run frontend:
```
cd ./client
npm install
npm run serve
```

### How to run backend:
- First activate python env (if you are using one)
```
cd ./env/Scripts
activate
```
- Then run:
```
pip install -r requirements.txt
cd server
python manage.py runserver
```
- To see the project in your browser
```
http://localhost:8080/
```
- Here is an example of how this application should look like:
![preview](https://i.imgur.com/H91uH7E.png)

 The program will display different text depending on the day of the week. Just refresh the page and you will see that.
If you edit an item by button, time column will change data.
