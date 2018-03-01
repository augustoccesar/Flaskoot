get_users = {
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string"
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "A list of users",
            "schema": {
                "$ref": "#/definitions/User"
            },
            "examples":
            [
                {
                    "_links": {
                        "self": "/users/<id:String>"
                    },
                    "id": "String",
                    "username": "String"
                }
            ]
        }
    }
}

get_user = {
    "definitions": {
        "User": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string"
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "Selected user by its id",
            "schema": {
                "$ref": "#/definitions/User"
            },
            "examples":
            {
                "_links": {
                    "self": "/users/<id:String>"
                },
                "id": "String",
                "username": "String"
            }
        }
    }
}
