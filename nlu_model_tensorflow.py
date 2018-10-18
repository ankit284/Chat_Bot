from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
import json

builder = ComponentBuilder(use_cache=True)

with open('./config_tensorflow.json') as conf_file:
	config_data = json.load(conf_file)

def train_nlu(config_data):
        training_data = load_data(config_data["data"])
        trainer = Trainer(config.load('./config_tensorflow.json'), builder)
        trainer.train(training_data)
        model_directory = trainer.persist(config_data["path"], fixed_model_name = 'restaurantnlu')


def run_nlu(config_data):
        interpreter = Interpreter.load(config_data["path"]+'/default/restaurantnlu', builder)
        print(interpreter.parse("can you please suggest food"))

if __name__ == '__main__':
	train_nlu(config_data)
	run_nlu(config_data)


