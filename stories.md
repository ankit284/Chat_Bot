## Generated Story -3334542526149540885
* greet
    - utter_greet
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"price": "400"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* send_email{"email": "xyz@abc.com"}
    - slot{"email": "xyz@abc.com"}
    - action_send_email
    - slot{"email": "xyz@abc.com"}
    - utter_goodbye
    - export

