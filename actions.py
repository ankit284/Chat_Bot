from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.trackers import DialogueStateTracker
from rasa_core.slots import TextSlot

import zomatopy
import json
from flask import Flask
from flask_mail import Message, Mail
import app_email
import ast


class ActionSearchRestaurants(Action):
        
        def name(self):
                return 'action_restaurant'
        
        def run(self, dispatcher, tracker, domain):
                config={ "user_key":""}
                zomato = zomatopy.initialize_app(config)
                city_lookuplist=[]
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                
                if cuisine == None:
                        dispatcher.utter_template('utter_ask_reenter_cuisine', tracker)
                        return 

                if loc == None:
                        dispatcher.utter_template('utter_ask_reenter_location', tracker)
                        return

                # loc="Hyderabad"
                # cuisine="Chinese"
                # getting location id
                location_detail=zomato.get_location(loc, 1)                
                d1 = json.loads(location_detail)
                        
                lat=d1["location_suggestions"][0]["latitude"]
                lon=d1["location_suggestions"][0]["longitude"]
                city_id=d1["location_suggestions"][0]["city_id"]
                tracker.update(SlotSet("lat",lat))
                tracker.update(SlotSet("lon",lon))
                tracker.update(SlotSet("city_id",city_id))
                        
                # cuisine_option=['Chinese', 'Mexican', 'Italian', 'American', 'South Indian','North Indian']
                cuisine_details=zomato.get_cuisines(city_id)
                cuisines_key=""
                try:
                        c_k=list(cuisine_details.keys())
                        c_v=list(cuisine_details.values())
                        c_v=[x.lower() for x in c_v]
                        c_index=c_v.index(cuisine.lower())
                        cuisine_key=str(c_k[c_index])
                        tracker.update(SlotSet('cuisine_key',cuisine_key))
                except ValueError as e:
                        dispatcher.utter_message("Sorry! not able to find cuisine {} restaurant".format(cuisine))
                        # d2 = json.loads(cusine_details)
                        # ={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
                        
                results=zomato.restaurant_search("", lat, lon, cuisine_key, 10)
                        
                d = json.loads(results)
                api_response="{"
                response=""
                if d['results_found'] == 0:
                        response= "no results"
                else:
                        counter=1
                        for restaurant in d['restaurants']:
                                api_response+='"{}":["{}","{}","{}","{}"]'.format(counter,restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],restaurant['restaurant']['user_rating']['aggregate_rating'])
                                if counter<6:
                                        response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+restaurant['restaurant']['user_rating']['aggregate_rating'] +"\n"
                                if counter<10:
                                        api_response+=","
                                        counter+=1

                dispatcher.utter_message("-----\n"+response)
                api_response+="}"
                tracker.update(SlotSet('api_response',api_response))
                
                return [SlotSet('location',loc)]

class ActionSendEmail(Action):
        def name(self):
                return 'action_send_email'

        def run(self, dispatcher, tracker, domain):
                email_id=tracker.get_slot('email')
                render_html=True
                try:
                        api_response=ast.literal_eval(str(tracker.get_slot('api_response')))
                except:
                        render_html=False
                response=app_email.send_mail("Hello","How are you doing",api_response,email_id,render_html)
                
                if response != "Success":
                        dispatcher.utter_template('utter_email_not_sent', tracker)
                else:
                        dispatcher.utter_template('utter_email_sent', tracker)
                return [SlotSet('email',email_id)]

class ActionValidateCuisine(Action):
        def name(self):
                return 'action_validate_cuisine'

        def run(self, dispatcher, tracker, domain):
                cuisine = tracker.get_slot('cuisine')

                if cuisine.lower() not in ['american','mexican','italian','north indian','south indian','chinese']:
                        dispatcher.utter_template('utter_ask_reenter_cuisine', tracker)
                        cuisine = None
                
                return [SlotSet('cuisine',cuisine)]

class ActionValidateLocation(Action):
        def name(self):
                return 'action_validate_location'

        def run(self, dispatcher, tracker, domain):
                loc = tracker.get_slot('location')
                
                with open('./data/lookup/locations.txt','r') as lookup:
                        city_lookuplist=lookup.read().splitlines()
                        city_lookuplist=[x.lower() for x in city_lookuplist]

                if loc not in city_lookuplist:
                        dispatcher.utter_template('utter_ask_reenter_location', tracker)
                        loc = None
                
                return [SlotSet('location',loc)]

# ActionSearchRestaurants().run("","","")