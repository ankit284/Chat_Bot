## Generated Story 3435432227545728728
* greet
    - utter_greet
* restaurant_search{"budget": "500", "cuisine": "italian", "location": "bangalore"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "hmmm@hmmm.com"}
    - slot{"email": "hmmm@hmmm.com"}
    - action_send_email
    - slot{"email": "hmmm@hmmm.com"}
    - utter_goodbye
    - export

