## Generated Story 5563939221839938948
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_send_email
* send_email{"email": "abcd@123.com"}
    - slot{"email": "abcd@123.com"}
    - utter_goodbye
    - export

## Generated Story 1027659414837775700
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_send_email
* goodbyes{"email": "abcd@xyz.com"}
    - slot{"email": "abcd@xyz.com"}
    - utter_goodbye
    - export

## Generated Story -5866098034741379691
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"budget": "800"}
    - slot{"budget": "800"}
    - action_restaurant
    - slot{"location": "rishikesh"}
    - utter_ask_send_email
* goodbyes
    - utter_goodbye
    - export

## Generated Story -4684592105924043860
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "900"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_send_email
* restaurant_search
    - utter_goodbye
    - export

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

