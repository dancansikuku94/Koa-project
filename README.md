## Koa-project
Django application with an API that receives a set of points on a grid as semicolon separated values. And then it finds the points that are closest to each other. Store the received set of points and the closest points on a DB.

An example input would look like this:
2,2;-1,30;20,11;4,5

And then in this case the result would be:
2,2;4,5

# How to run the code (Closest Points API)

This is a Django application with an API that receives a set of points on a grid as semicolon-separated values and finds the two points that are closest to each other. The application also provides an admin interface for viewing the stored values in the database.

## Installation

1. Clone the repository:
2. Install the dependencies:

     ```pip install django```

     ```pip install djangorestframework```

3. Run database migration:
       ```python manage.py makemigrations & migrate ```
4. Start the Django development server:
        ```python manage.py runserver```
  
## Usage 

The API provides the following endpoints:
  ```http://localhost:8000/closest_points/```

## Example requests:

**POST** /closest_points/
Content-Type: application/json

```
{
  "points": "2,2;-1,30;20,11;4,5"
}
````



**Response**
HTTP/1.1 200 OK
Content-Type: application/json

```

{
    "closest_points": "2.0,2.0;4.0,5.0"
}
  
  ```

        



