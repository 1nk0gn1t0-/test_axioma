# test_axioma
Axioma test task

Follow the instructions to check the test task:

Clone this repository
```
git clone https://github.com/1nk0gn1t0-/test_axioma.git
```
Start docker-compose
```
docker-compose up -d
```
Wait start db and web services

Send requests for web services
* post 
```
http://127.0.0.1:8000/categories/
```
```json
{
    "id": 1,
    "name": "Category 1",
    "parent": null,
    "children": [
        {
            "id": 2,
            "name": "Category 1.1",
            "parent": 1,
            "children": [
                {
                    "id": 3,
                    "name": "Category 1.1.1",
                    "parent": 2,
                    "children": [
                        {
                            "id": 4,
                            "name": "Category 1.1.1.1",
                            "parent": 3,
                            "children": []
                        },
                        {
                            "id": 5,
                            "name": "Category 1.1.1.2",
                            "parent": 3,
                            "children": []
                        },
                        {
                            "id": 6,
                            "name": "Category 1.1.1.3",
                            "parent": 3,
                            "children": []
                        }
                    ]
                },
                {
                    "id": 7,
                    "name": "Category 1.1.2",
                    "parent": 2,
                    "children": [
                        {
                            "id": 8,
                            "name": "Category 1.1.2.1",
                            "parent": 7,
                            "children": []
                        },
                        {
                            "id": 9,
                            "name": "Category 1.1.2.2",
                            "parent": 7,
                            "children": []
                        },
                        {
                            "id": 10,
                            "name": "Category 1.1.2.3",
                            "parent": 7,
                            "children": []
                        }
                    ]
                }
            ]
        },
        {
            "id": 11,
            "name": "Category 1.2",
            "parent": 1,
            "children": [
                {
                    "id": 12,
                    "name": "Category 1.2.1",
                    "parent": 11,
                    "children": []
                },
                {
                    "id": 13,
                    "name": "Category 1.2.2",
                    "parent": 11,
                    "children": [
                        {
                            "id": 14,
                            "name": "Category 1.2.2.1",
                            "parent": 13,
                            "children": []
                        },
                        {
                            "id": 15,
                            "name": "Category 1.2.2.2",
                            "parent": 13,
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
}
```

* get
```
http://127.0.0.1:8000/categories/:id/
```
