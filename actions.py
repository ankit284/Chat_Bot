from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import zomatopy
import json



class ActionSearchRestaurants(Action):
        country_lookuplist=[]
        def name(self):
                return 'action_restaurant'
        
        def run(self, dispatcher, tracker, domain):
                config={ "user_key":""}
                zomato = zomatopy.initialize_app(config)
                if self.country_lookuplist==[]:
                        with open('./data/lookup/locations.txt','r') as lookup:
                                self.country_lookuplist=lookup.read().splitlines()
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                if loc in self.country_lookuplist:
                        location_detail=zomato.get_location(loc, 1)
                        
                        d1 = json.loads(location_detail)
                        
                        lat=d1["location_suggestions"][0]["latitude"]
                        lon=d1["location_suggestions"][0]["longitude"]
                        
                        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
                        
                        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
                        
                        d = json.loads(results)
                        response=""
                        if d['results_found'] == 0:
                                response= "no results"
                        else:
                                for restaurant in d['restaurants']:
                                        response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"

                        dispatcher.utter_message("-----"+response)
                else:
                        dispatcher.utter_template('utter_noService',tracker)
                return [SlotSet('location',loc)]

class ActionSendEmail(Action):
        def name(self):
                return 'action_send_email'

        def run(self, dispatcher, tracker, domain):
                dispatcher.utter_message("-----")
                return [SlotSet('email','xyz@abc.com')]

class ActionValidateCuisine(Action):
        def name(self):
                return 'action_validate_cuisine'

        def run(self, dispatcher, tracker, domain):
                dispatcher.utter_message("-----")
                return [SlotSet('cuisine','Italian')]

class ActionValidateLocation(Action):
        def name(self):
                return 'action_validate_location'

        def run(self, dispatcher, tracker, domain):
                dispatcher.utter_message("-----")
                return [SlotSet('location','Hyderabad')]

