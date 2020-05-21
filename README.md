# integer_increment_service
This service is using Flask framework and REST architecture for implementing a on request incremental integer service.

****It is advised to create a virtual environment for this project****

Python - 2.7
Flask - 1.1.2
PyJWT - 1.7.1

Install Dependencies:
    pip install -r requirements.txt
    
Run the Server
    - Go to project directory
    - run -> "python main.py"
    - server will start on localhost on port 5000 by default


Assumptions while implementing the service:
  - No checking of valid email, it can be any random string
  - No validation on password, it can also be any random string
  - No database is used. A hash-map/dictionary is used for storing users data and current value of integer.
  - Server restart will cause loss of data.
  - basic error handling
  - No UI
  - I completed it in around 3 hours
  - main.py is the main server file. Execute it to start the server. command - > python main.py
    

CURL commands to interect with the server:

1. Sign Up:
    - If you haven't registered a user then execute this command first.
    - curl --location --request POST 'localhost:5000/sign_up' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "email": "vvknain@gmail.com",
          "password": "1234"
        }'
    - JWT will be returned. copy it and replace "XXXXXX" in next CURL commands
    
2. Login:
    - If user is already registered and logged out
    - curl --location --request POST 'localhost:5000/login' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "email": "vvknain@gmail.com",
          "password": "1234"
        }'
    - JWT will be returned. copy it and replace "XXXXXX" in next CURL commands
    
3. Get current value of integer:
    - curl --location --request GET 'localhost:5000/current' --header 'Authorization: Bearer XXXXXX'

4. Set particular value of integer:
    - curl --location --request PUT 'localhost:5000/current' \
        --header 'Authorization: Bearer XXXXXX' \
        --header 'Content-Type: application/json' \
        --data-raw '{
          "current": 20(put any value here)
        }'
        
5. Increment value of integer:
     - curl --location --request GET 'localhost:5000/next' --header 'Authorization: Bearer XXXXXX'
    
6. Sign Out:
    - curl --location --request GET 'localhost:5000/sign_out' --header 'Authorization: Bearer XXXXXX'




