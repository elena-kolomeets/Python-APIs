# Meals API

## Meals API

This Web API serves data from a restaurant database which contains records about meals and users. 

A user can signup, login, save and edit their details, and keep a list of their favourite meals. 

Some users will be allowed to do administrative tasks like accessing, updating and deleting records about users and meals.

## Sign up

```
POST http://127.0.0.1:5000/auth/signup
```

Create a user profile.

### Request

 
 **Body**
 
 ```
 {

     "email": "example@email.com",

     "password": "example", 

     "name": "Example" 

 }
 ```
 

### Examples:

 
 **Example: Sign up - short password**
 
  
  ```
  POST http://127.0.0.1:5000/auth/signup
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "short@email.com",

       "password": "short"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 
 **Example: Sign up - success**
 
  
  ```
  POST http://127.0.0.1:5000/auth/signup
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example@email.com",

       "password": "example",

       "name": "Example"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "new_user_id": "60634af83ef5cdcf24a6d96d"
     }
   }
   ```
   
  
 

## Log in

```
POST http://127.0.0.1:5000/auth/login
```

Log in with user credentials to get an authorisation token.

### Request

 
 **Body**
 
 ```
 {

     "email": "example@email.com",

     "password": "example"

 }
 ```
 

### Examples:

 
 **Example: Log in - success**
 
  
  ```
  POST http://127.0.0.1:5000/auth/login
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example@email.com",

       "password": "example"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNzEyMDY3OSwianRpIjoiMWIxYmEzNzMtODlkMS00NzVlLWI0ODYtNzRjM2RhNjIxYjY0IiwibmJmIjoxNjE3MTIwNjc5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiNjA2MzRhZjgzZWY1Y2RjZjI0YTZkOTZkIiwiZXhwIjoxNjE3NTUyNjc5fQ.EstMp0IaU-1b3_oP84oj5UFiyild2rWBK5l-H2U_lIQ",
       "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNzEyMDY3OSwianRpIjoiZmJhNzNlNmEtZDE5ZS00MDg1LThjNDYtNjJkZjZkY2JhMTA3IiwibmJmIjoxNjE3MTIwNjc5LCJ0eXBlIjoicmVmcmVzaCIsInN1YiI6IjYwNjM0YWY4M2VmNWNkY2YyNGE2ZDk2ZCIsImV4cCI6MTYxOTcxMjY3OX0.sE0db0cNeTg8HLHyRXH2i43balpeKRfHi_TKVOK-kPc",
       "user_id": "60634af83ef5cdcf24a6d96d"
     }
   }
   ```
   
  
 
 **Example: Log in - wrong password**
 
  
  ```
  POST http://127.0.0.1:5000/auth/login
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example@email.com",

       "password": "wrongpass"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Invalid email or password."
     }
   }
   ```
   
  
 

## Meals

```
GET http://127.0.0.1:5000/meals
```

Get all meals records.

### Examples:

 
 **Example: Get Meals - success**
 
  
  ```
  GET http://127.0.0.1:5000/meals
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": [
       {
         "_id": {
           "$oid": "603519dc7d2b69804a4edfa5"
         },
         "description": "Not even the baker knows what's inside...",
         "image_url": "",
         "name": "Mystery Pie",
         "price": 0
       },
       {
         "_id": {
           "$oid": "603519f07d2b69804a4edfa6"
         },
         "description": "A delicious, home-made apple pie. Best served on a window sill in the summer.",
         "image_url": "",
         "name": "Apple Pie",
         "price": 10
       },
       {
         "_id": {
           "$oid": "60351a447d2b69804a4edfa7"
         },
         "description": "These crisp veggie rolls are filled with cabbage, peppers, cucumber, and home-made peanut sauce.",
         "image_url": "",
         "name": "Vegetable Spring Rolls",
         "price": 0
       },
       {
         "_id": {
           "$oid": "6046589eed8d550213ca4c19"
         },
         "description": "A delicious small hollow case of puff pastry filed with a combination of chicken, mushrooms, and small meatballs",
         "image_url": "",
         "name": "Vol-au-vent",
         "price": 20
       },
       {
         "_id": {
           "$oid": "604658fced8d550213ca4c1a"
         },
         "description": "Special Belgian recepy with speculoos bottom",
         "name": "Cherry cheesecake",
         "price": 19
       },
       {
         "_id": {
           "$oid": "604b3bcfc5bc5594786fde3d"
         },
         "description": "Classical cheesecake recepy",
         "image_url": null,
         "name": "Philadelphia cheesecake",
         "price": 15
       }
     ]
   }
   ```
   
  
 
 **Example: Get Meals - not logged in (no token)**
 
  
  ```
  GET http://127.0.0.1:5000/meals
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "msg": "Missing Authorization Header"
   }
   ```
   
  
 

## Meal

```
POST http://127.0.0.1:5000/meals
```

Create a meal record.

Admin access required.

### Request

 
 **Body**
 
 ```
 {

     "name": "Example Meal",

     "description": "Just an example meal",

     "price": 1.5,

     "image_url": "https://pixabay.com/images/id-2009590/"

 }
 ```
 

### Examples:

 
 **Example: Post Meal - not admin**
 
  
  ```
  POST http://127.0.0.1:5000/meals
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "name": "Another Example Meal",

       "description": "Yet another example meal"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Unauthorized action."
     }
   }
   ```
   
  
 
 **Example: Post Meal - success**
 
  
  ```
  POST http://127.0.0.1:5000/meals
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "name": "Example Meal",

       "description": "Just an example meal",

       "price": 1.5,

       "image_url": "https://pixabay.com/images/id-2009590/"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "new_meal_id": "6063508ba4ea681a192c19e3"
     }
   }
   ```
   
  
 

## Meal

```
GET http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
```

Get a single meal record.

### Examples:

 
 **Example: Get Meal - wrong meal id**
 
  
  ```
  GET http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e34
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "No meal with id=6063508ba4ea681a192c19e34"
   }
   ```
   
  
 
 **Example: Get Meal - success**
 
  
  ```
  GET http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "_id": {
         "$oid": "6063508ba4ea681a192c19e3"
       },
       "description": "Just an example meal",
       "image_url": "https://pixabay.com/images/id-2009590/",
       "name": "Example Meal",
       "price": 1.5
     }
   }
   ```
   
  
 

## Meal

```
PUT http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
```

Update an existing meal record.

Admin access required.

### Request

 
 **Body**
 
 ```
 {

     "name": "Example Meal",

     "price": 5

 }
 ```
 

### Examples:

 
 **Example: Update Meal - success**
 
  
  ```
  PUT http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "name": "Example Meal",

       "price": 5

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "Successfully updated meal 6063508ba4ea681a192c19e3"
   }
   ```
   
  
 
 **Example: Update Meal - no name**
 
  
  ```
  PUT http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "price": 7

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 

## Meal

```
DELETE http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
```

Delete an existing meal record.

Admin access required.

### Request

 

### Examples:

 
 **Example: Delete Meal - success**
 
  
  ```
  DELETE http://127.0.0.1:5000/meals/6063508ba4ea681a192c19e3
  ```
  
  **Request**
  
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "Successfully deleted meal 6063508ba4ea681a192c19e3"
   }
   ```
   
  
 

## Users

```
GET http://127.0.0.1:5000/users
```

Get all users records.

Admin access required.

### Examples:

 
 **Example: Get Users - not admin**
 
  
  ```
  GET http://127.0.0.1:5000/users
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Unauthorized action."
     }
   }
   ```
   
  
 
 **Example: Get Users - success**
 
  
  ```
  GET http://127.0.0.1:5000/users
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": [
       {
         "_id": {
           "$oid": "6036635a4b75ab0fbb5fabd5"
         },
         "access": {
           "admin": false,
           "user": true
         },
         "email": "user@user.com",
         "fav_meals": [],
         "name": "User"
       },
       {
         "_id": {
           "$oid": "604bc4e1aff9f63bd6655b07"
         },
         "access": {
           "admin": false,
           "user": true
         },
         "email": "testemail@email.com",
         "fav_meals": []
       },
       {
         "_id": {
           "$oid": "6061d9e29c8043a1058340d0"
         },
         "access": {
           "admin": true,
           "user": true
         },
         "email": "elena@email.com",
         "fav_meals": [
           {
             "$oid": "604658fced8d550213ca4c1a"
           },
           {
             "$oid": "6046589eed8d550213ca4c19"
           }
         ],
         "name": "Elena"
       },
       {
         "_id": {
           "$oid": "60623de94590e06b832e2db7"
         },
         "access": {
           "admin": false,
           "user": true
         },
         "email": "just_user@email.com",
         "fav_meals": [],
         "name": ""
       },
       {
         "_id": {
           "$oid": "6063230eaa160053fd515a19"
         },
         "access": {
           "admin": false,
           "user": true
         },
         "email": "elena7@email.com",
         "fav_meals": [
           {
             "$oid": "604b3bcfc5bc5594786fde3d"
           },
           {
             "$oid": "604658fced8d550213ca4c1a"
           }
         ],
         "name": "Elena7"
       },
       {
         "_id": {
           "$oid": "60634af83ef5cdcf24a6d96d"
         },
         "access": {
           "admin": false,
           "user": true
         },
         "email": "example@email.com",
         "fav_meals": [],
         "name": "Example"
       }
     ]
   }
   ```
   
  
 

## User

```
POST http://127.0.0.1:5000/users
```

Create a new user record.

Admin access required.

### Request

 
 **Body**
 
 ```
 {

     "email": "example2@email.com",

     "password": "example2",

     "name": "Example 2",

     "access": {

         "admin": true

     }

 }
 ```
 

### Examples:

 
 **Example: Post User - success (add fav_meals)**
 
  
  ```
  POST http://127.0.0.1:5000/users
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example3@email.com",

       "password": "example3",

       "name": "Example 3",

       "access": {

           "admin": true

       },

       "fav_meals": [

           {

               "name": "Philadelphia cheesecake"

           },

           {

               "name": "Cherry cheesecake"

           }

       ]

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "new_user_id": "6064853bc838ae729a032832"
     }
   }
   ```
   
  
 
 **Example: Post User - no password**
 
  
  ```
  POST http://127.0.0.1:5000/users
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example3@email.com",

       "name": "Example 3"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 
 **Example: Post User - not admin**
 
  
  ```
  POST http://127.0.0.1:5000/users
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example3@email.com",

       "password": "example3",

       "name": "Example 3"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Unauthorized action."
     }
   }
   ```
   
  
 
 **Example: Post User - success (grant admin access)**
 
  
  ```
  POST http://127.0.0.1:5000/users
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example2@email.com",

       "password": "example2",

       "name": "Example 2",

       "access": {

           "admin": true

       }

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "new_user_id": "60635711ca8613b190fcaf8e"
     }
   }
   ```
   
  
 
 **Example: Post User - wrong format for fav_meals**
 
  
  ```
  POST http://127.0.0.1:5000/users
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example4@email.com",

       "password": "example4",

       "name": "Example 4",

       "fav_meals": "Cherry cheesecake"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 

## User

```
GET http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
```

Get a single user record.

Admin access required.

### Examples:

 
 **Example: Get User - wrong id**
 
  
  ```
  GET http://127.0.0.1:5000/users/1234567890abcdefg
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "No user with id=1234567890abcdefg"
   }
   ```
   
  
 
 **Example: Get User - success**
 
  
  ```
  GET http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "_id": {
         "$oid": "60634af83ef5cdcf24a6d96d"
       },
       "access": {
         "admin": false,
         "user": true
       },
       "email": "example@email.com",
       "fav_meals": [],
       "name": "Example"
     }
   }
   ```
   
  
 

## User

```
PUT http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
```

Update a single user record.

Admin access required.

### Request

 
 **Body**
 
 ```
 {

     "email": "example@email.com",

     "password": "example",

     "fav_meals": [

         {

             "name": "Philadelphia cheesecake"

         },

         {

             "name": "Cherry cheesecake"

         }

     ]

 }
 ```
 

### Examples:

 
 **Example: Update User - not email & password**
 
  
  ```
  PUT http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "name": "Name"

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 
 **Example: Update User - success (add fav_meals)**
 
  
  ```
  PUT http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example@email.com",

       "password": "example",

       "fav_meals": [

           {

               "name": "Philadelphia cheesecake"

           },

           {

               "name": "Cherry cheesecake"

           }

       ]

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "Successfully updated user 60634af83ef5cdcf24a6d96d"
   }
   ```
   
  
 
 **Example: Update User - wrong format for fav_meals**
 
  
  ```
  PUT http://127.0.0.1:5000/users/60634af83ef5cdcf24a6d96d
  ```
  
  **Request**
  
   
   **Body**
   
   ```
   {

       "email": "example@email.com",

       "password": "example",

       "fav_meals": ["Mistery Pie"]

   }
   ```
   
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": {
       "error": "Wrong values passed or missing required values in the request body."
     }
   }
   ```
   
  
 

## User

```
DELETE http://127.0.0.1:5000/users/6064853bc838ae729a032832
```

Delete a single user record.

Admin access required.

### Examples:

 
 **Example: Delete User - success**
 
  
  ```
  DELETE http://127.0.0.1:5000/users/6064853bc838ae729a032832
  ```
  
  **Response**
  
   
   **Body**
   
   ```
   {
     "result": "Successfully deleted user 6064853bc838ae729a032832"
   }
   ```
   
  
 

Generated with [Postdown][PyPI].

[PyPI]:    https://pypi.python.org/pypi/Postdown
