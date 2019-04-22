# TODO App in Django
Sample Todo App using Django REST Framework and DJango

## Functionalities
- Perform CRUD operations using Django Admin Dashboard and web api

# Sample API response
http://hsekin.pythonanywhere.com/todoapp/api/todos/

    {
    "data": {
        "notes": [
            {
                "id": 1,
                "todo_title": "This is test",
                "todo_desc": "hahahah\r\nhahahhaha\r\nI told u man !!! its so funny",
                "created_date": "2019-02-06",
                "updated_date": "2019-02-06",
                "todo_status": true,
                "created_by": 1,
                "category": 1
            },
            {
                "id": 2,
                "todo_title": "Call",
                "todo_desc": "Call Rajan today to talk about job. \r\nIts important.",
                "created_date": "2019-02-06",
                "updated_date": "2019-02-06",
                "todo_status": false,
                "created_by": 1,
                "category": 1
            }
           ]
        }
      }      
