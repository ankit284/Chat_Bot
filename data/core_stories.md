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
* send_email{"email": "test@testmail.com"}
    - slot{"email": "test@testmail.com"}
* goodbye
    - utter_goodbye
    - export
## Generated Story 1523839646586044917
* restaurant_search{"cuisine": "north indian", "location": "raebarelie"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "raebarelie"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "raebarelie"}
    - utter_goodbye
    - export

## Generated Story -4317997935640952185
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - export

## Generated Story 600278197254133861
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "raebareli"}
    - slot{"location": "raebareli"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - action_restaurant
    - slot{"location": "raebareli"}
    - action_restaurant
    - slot{"location": "raebareli"}
    - export

## Generated Story -6714059600070157139
* restaurant_search{"cuisine": "north indian", "location": "hyderabad"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@testmail.com"}
    - slot{"email": "test@testmail.com"}
    - action_send_email
    - slot{"email": "test@testmail.com"}
    - utter_goodbye
    - export

## Generated Story -4407532458322318847
* restaurant_search{"cuisine": "north indian", "location": "hyderabad"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "hyderabad"}
    - utter_ask_budget
* restaurant_search{"budget": "300"}
    - slot{"budget": "300"}
    - slot{"lat": 17.366}
    - slot{"lon": 78.476}
    - slot{"city_id": 6}
    - slot{"cuisine_key": "50"}
    - slot{"api_response": "{\"1\":[\"AB's - Absolute Barbecues\",\"Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad\",\"1500\",\"4.9\"],\"2\":[\"AB's - Absolute Barbecues\",\"Plot 483, 4th Floor, Pemmasani Complex, Bajaj Electronics Building, Near Madhapur Police Station, Road 36, Jubilee Hills, Hyderabad\",\"1500\",\"4.9\"],\"3\":[\"Chili's American Grill & Bar\",\"Flat 48, Ground Floor, Opposite Vengal Rao Park, Road 1, Banjara Hills, Hyderabad\",\"1400\",\"4.9\"],\"4\":[\"Chili's American Grill & Bar\",\"F 48, 1st Floor, Inorbit Mall, Hitech City, Hyderabad\",\"1400\",\"4.9\"],\"5\":[\"AB's - Absolute Barbecues\",\"8-2-618/10-11, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad\",\"1500\",\"4.9\"],\"6\":[\"The Roastery Coffee House\",\"8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad\",\"800\",\"4.8\"],\"7\":[\"Nimrah Cafe And Bakery\",\"Beside Mecca Masjid, Charminar Road, Charminar, Hyderabad\",\"100\",\"4.8\"],\"8\":[\"Exotica\",\"Opposite Audi Showroom, 5th Floor, 12th Square Building, Road 12, Banjara Hills, Hyderabad\",\"1500\",\"4.7\"],\"9\":[\"Farzi Cafe\",\"1200, Road 59, Jubilee Hills, Hyderabad\",\"1800\",\"4.7\"],\"10\":[\"Sahib\u2019s Barbeque by Ohri\u2019s\",\"Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur\",\"1400\",\"4.7\"]}"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_get_email_confirmation
* affirm
    - utter_ask_send_email
* send_email{"email": "test@testmail.com"}
    - slot{"email": "test@testmail.com"}
    - action_send_email
    - slot{"email": "test@testmail.com"}
    - utter_goodbye
    - export

