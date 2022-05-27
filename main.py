from flask import Flask, request, jsonify

app = Flask(__name__)

user_data = [{
    "first_name": "Agasi",
    "last_name": "Bekiryan",
    "age": "21",
    "gender": "male"
},
    {
        "age": "50",
        "first_name": "Jhonny",
        "gender": "male",
        "last_name": "Depp"
    }
]


def user_filter(json: dict):
    users = []
    for user in user_data:
        for key, val in json.items():
            try:
                print(user[key], val)
                if val.lower() in user[key].lower():
                    users.append(user)
                    break
            except:
                pass
    return users


@app.route('/', methods=["POST", "GET"])
def user():
    if request.method == "GET":
        try:
            request.json
        except:
            return "Add filter body", 400

        result = user_filter(request.json)
        return jsonify(result), 200
    if request.method == "POST":
        try:
            request.json
        except:
            return "Add user data", 400

        try:
            data = {}
            data["first_name"] = request.json["first_name"]
            data["last_name"] = request.json["last_name"]
            data["age"] = request.json["age"]
            data["gender"] = request.json["gender"]
        except:
            return "User data must contain age,first_name,gender and last_name fields", 400

        user_data.append(data)
        return data, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
