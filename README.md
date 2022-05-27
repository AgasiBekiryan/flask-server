# flask-server
Simple Flask Server for getting users info with filter and creating new users:

# Requests
GET 'http://localhost:5000'
Body
{
  "first_name": "A"
}

POST 'http://localhost:5000'
Body
{
        "first_name": "Andrea",
        "last_name": "Bell",
        "age": "22",
        "gender": "female"
}
