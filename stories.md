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

## Generated Story 5563939221839938948
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* send_email{"email": "abcd@123.com"}
    - slot{"email": "abcd@123.com"}
    - utter_goodbye
    - export

