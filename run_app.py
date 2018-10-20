from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import warnings
import ruamel
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-459797226497-460231095108-460235671796-fd65a340d219a7374eff03341c465569', #app verification token
							'xoxb-459797226497-460406157730-jxpRz011X6DHVBXdnLR9gjvN', # bot verification token
							'9RePOdqTeK09UJuzj5aRjDgE', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5014, '/', input_channel))