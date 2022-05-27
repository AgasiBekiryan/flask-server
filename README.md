# flask-server
Simple Flask Server for getting users with filter and creating new users:

# Requests
GET 'http://localhost:5000'
{
  "first_name": "A"
}

POST 'http://localhost:5000'
{
        "age": "22",
        "first_name": "Andrea",
        "gender": "female",
        "last_name": "Bell"
}
