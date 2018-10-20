## Generated Story 4467620711531577782
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* send_email{"email": "jpr.saurabh@gmail.com"}
    - slot{"email": "jpr.saurabh@gmail.com"}
* goodbye
    - utter_goodbye
    - export

