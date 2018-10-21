## Generated Story 5531831153953553777
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 1995729700704826868
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - action_validate_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - action_restaurant
    - utter_ask_send_email
* deny
    - utter_goodbye
    - export

## Generated Story -604375998088902518
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "hyderabad", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story -8244669627926220586
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -1367035906579954553
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "cuisine": "mexican", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export


## Generated Story 3242629234640858394
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "cuisine": "mexican", "budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -1367035906579954553
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "cuisine": "mexican", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - action_send_email
    - slot{"email": null}
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 3242629234640858394
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "cuisine": "mexican", "budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 1982201520010505095
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "budget": "500", "cuisine": "north indian"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 2550947626072210786
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "budget": "700", "cuisine": "mexican"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -1367035906579954553
* greet
    - utter_greet
* restaurant_search{"location": "bangalore", "cuisine": "mexican", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - action_send_email
    - slot{"email": null}
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 3242629234640858394
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "cuisine": "mexican", "budget": "300"}
    - slot{"budget": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 1982201520010505095
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "budget": "500", "cuisine": "north indian"}
    - slot{"budget": "500"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 2550947626072210786
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "budget": "700", "cuisine": "mexican"}
    - slot{"budget": "700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -8190622316988994815
* greet
    - utter_greet
* restaurant_search{"budget": "500", "location": "hyderabad", "cuisine": "south indian"}
    - slot{"budget": "500"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "ankit284@gmail.com"}
    - slot{"email": "ankit284@gmail.com"}
    - action_send_email
    - slot{"email": "ankit284@gmail.com"}
    - utter_goodbye
    - export

## Generated Story -1327320664524996494
* greet
    - utter_greet
* restaurant_search{"budget": "700", "location": "chennai", "cuisine": "american"}
    - slot{"budget": "700"}
    - slot{"cuisine": "american"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -824154151604329730
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "budget": "500", "location": "delhi"}
    - slot{"budget": "500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@xyz.com"}
    - slot{"email": "test123@xyz.com"}
    - action_send_email
    - slot{"email": "test123@xyz.com"}
    - utter_goodbye
    - export

## Generated Story -8871874266623399363
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "700", "location": "kolkata"}
    - slot{"budget": "700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -6091099200797353842
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_ask_send_email
* deny
    - utter_goodbye
    - export

## Generated Story -6343159596268679850
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@abc.com"}
    - slot{"email": "test123@abc.com"}
    - action_send_email
    - slot{"email": "test123@abc.com"}
    - utter_goodbye
    - export

## Generated Story -6091099200797353842
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_ask_send_email
* deny
    - utter_goodbye
    - export

## Generated Story -6343159596268679850
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@abc.com"}
    - slot{"email": "test123@abc.com"}
    - action_send_email
    - slot{"email": "test123@abc.com"}
    - utter_goodbye
    - export

## Generated Story 2785395967149872169
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@abc.com"}
    - slot{"email": "test123@abc.com"}
    - action_send_email
    - slot{"email": "test123@abc.com"}
    - utter_goodbye
    - export

## Generated Story 2785395007149872169
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "budget": "500"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - utter_ask_send_email
* deny
    - utter_goodbye
    - export

## Generated Story 1827989850553430735
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad", "budget": "600"}
    - slot{"budget": "600"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@abc.com"}
    - slot{"email": "test123@abc.com"}
    - action_send_email
    - slot{"email": "test123@abc.com"}
    - utter_goodbye
    - export

## Generated Story -6346642154572712871
* goodbye
    - utter_greet
* restaurant_search{"location": "bangalore", "budget": "700"}
    - slot{"budget": "700"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 5961944727647916089
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "kolkata"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -707327600777061580
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "chennai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - utter_ask_send_email
* affirm
    - utter_ask_send_email
* send_email{"email": "test123@abc.com"}
    - slot{"email": "test123@abc.com"}
    - action_send_email
    - slot{"email": "test123@abc.com"}
    - utter_goodbye
    - export

## Generated Story -6360928381470845351
* greet
    - utter_greet
* restaurant_search{"budget": "500", "cuisine": "mexican"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_validate_location
    - slot{"location": "bhopal"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* affirm{"email": "test@test.com"}
    - slot{"email": "test@test.com"}
    - action_send_email
    - slot{"email": "test@test.com"}
    - utter_goodbye
    - export

## Generated Story 4203211954486848325
* greet
    - utter_greet
* restaurant_search{"budget": "700", "cuisine": "american"}
    - slot{"budget": "700"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 5714104571767162434
* greet
    - utter_greet
* restaurant_search{"budget": "700", "location": "raipur"}
    - slot{"budget": "700"}
    - slot{"location": "raipur"}
    - action_validate_location
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story -3549826802723777575
* greet
    - utter_greet
* restaurant_search{"budget": "500", "location": "shimla"}
    - slot{"budget": "500"}
    - slot{"location": "shimla"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* affirm{"location": "test@123.com"}
    - slot{"location": "test@123.com"}
    - action_send_email
    - slot{"email": null}
    - utter_goodbye
    - export

## Generated Story 5004737910825328135
* greet
    - utter_greet
* restaurant_search{"budget": "500"}
    - slot{"budget": "500"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_validate_location
    - slot{"location": "patna"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* affirm{"location": "test@678.com"}
    - slot{"location": "test@678.com"}
    - action_send_email
    - slot{"email": null}
    - utter_goodbye
    - export

## Generated Story 3648262468921994499
* greet
    - utter_greet
* restaurant_search{"budget": "600"}
    - slot{"budget": "600"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_validate_location
    - slot{"location": "jaipur"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 4535999750252127528
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 4134209299475854784
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_validate_location
    - slot{"location": "ahmedabad"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* affirm{"email": "test@abcd.com"}
    - slot{"email": "test@abcd.com"}
    - action_send_email
    - slot{"email": "test@abcd.com"}
    - utter_goodbye
    - export

## Generated Story 4209562526913605607
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* deny
    - utter_goodbye
    - export

## Generated Story 1635464585156389991
* greet
    - utter_greet
* restaurant_search{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"budget": "700"}
    - slot{"budget": "700"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* affirm{"email": "ert@ert.com"}
    - slot{"email": "ert@ert.com"}
    - action_send_email
    - slot{"email": "ert@ert.com"}
    - utter_goodbye
    - export

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

## Generated Story 3435432227545728727
* greet
    - utter_greet
* restaurant_search{"budget": "500", "cuisine": "mexican", "location": "hyderabad"}
    - slot{"budget": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - action_restaurant
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* deny
    - utter_goodbye
    - export

