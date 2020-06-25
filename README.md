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
  "name": "Category 1",
  "children": [
    {
      "name": "Category 1.1",
      "children": [
        {
          "name": "Category 1.1.1",
          "children": [
            {
              "name": "Category 1.1.1.1"
            },
            {
              "name": "Category 1.1.1.2"
            },
            {
              "name": "Category 1.1.1.3"
            }
          ]
        },
        {
          "name": "Category 1.1.2",
          "children": [
            {
              "name": "Category 1.1.2.1"
            },
            {
              "name": "Category 1.1.2.2"
            },
            {
              "name": "Category 1.1.2.3"
            }
          ]
        }
      ]
    },
    {
      "name": "Category 1.2",
      "children": [
        {
          "name": "Category 1.2.1"
        },
        {
          "name": "Category 1.2.2",
          "children": [
            {
              "name": "Category 1.2.2.1"
            },
            {
              "name": "Category 1.2.2.2"
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
