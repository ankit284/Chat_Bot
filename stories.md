## Generated Story -3199611331310421518
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "hyderabad", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "american"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 8058684356069390102
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ajdgjasd@gas.com"}
    - slot{"email": "ajdgjasd@gas.com"}
    - action_send_email
    - slot{"email": "ajdgjasd@gas.com"}
    - utter_goodbye
    - export

