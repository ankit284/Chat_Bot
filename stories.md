## Generated Story 5535458598694006300
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "800"}
    - slot{"budget": "800"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* affirm{"location": "testabc@123xyz.com"}
    - slot{"location": "testabc@123xyz.com"}
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chandigarh"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget": "900"}
    - slot{"budget": "900"}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - utter_ask_send_email
* affirm{"location": "abcd@123.com"}
    - slot{"location": "abcd@123.com"}
    - utter_goodbye
    - export

