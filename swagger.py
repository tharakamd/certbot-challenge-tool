swagger_json = {
    "swagger": "2.0",
    "info": {
        "description": "This is certbot client helper for renewing certificates",
        "version": "1.0.0",
        "title": "Certbot Client Oracle Kubernetes RnD"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "tags": [
        {
            "name": "challenges",
            "description": "Manage slackbot challenges"
        },
        {
            "name": "wellknown",
            "description": "Access to Petstore orders"
        }
    ],
    "schemes": [
        "http"
    ],
    "paths": {
        "/challenges": {
            "post": {
                "tags": [
                    "challenges"
                ],
                "summary": "Add a new challenge",
                "description": "",
                "operationId": "addChallenge",
                "consumes": [
                    "application/json"
                ],
                "produces": [
                    "application/json"
                ],
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Challenge object to add",
                        "required": "true",
                        "schema": {
                            "$ref": "#/definitions/Challenge"
                        }
                    }
                ],
                "responses": {
                    "403": {
                        "description": "Invalid input"
                    }
                }
            },
            "get": {
                "tags": [
                    "challenges"
                ],
                "summary": "Get all challenges",
                "description": "",
                "operationId": "getChallenges",
                "produces": [
                    "application/json"
                ],
                "responses": {
                    "403": {
                        "description": "Invalid input"
                    }
                }
            }
        },
        "/.well-known/acme-challenge/{challenge_id}": {
            "get": {
                "tags": [
                    "wellknown"
                ],
                "summary": "Download relevent file for challenge",
                "description": "Returns a file with challenge text",
                "operationId": "return_file",
                "produces": [
                    "text/csv"
                ],
                "parameters": [
                    {
                        "name": "challenge_id",
                        "in": "path",
                        "description": "ID of the challenge",
                        "required": "true",
                        "type": "string"
                    }
                ],
                "responses": {
                    "403": {
                        "description": "Invalid ID"
                    }
                }
            }
        }
    },
    "definitions": {
        "Challenge": {
            "type": "object",
            "properties": {
                "challenge_content": {
                    "type": "string"
                },
                "challenge_id": {
                    "type": "string"
                }
            }
        }
    },
    "externalDocs": {
        "description": "Find out more about Swagger",
        "url": "http://swagger.io"
    }
}
