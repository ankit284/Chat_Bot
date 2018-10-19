from rasa_core.agent import Agent 
from rasa_core.policies.keras_policy import KerasPolicy 
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer) 

import logging

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    training_data_file = './data/core_stories.md'
    model_path = './models/dialogue'

    featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)

    agent = Agent('./restaurant_domain.yml',policies=[KerasPolicy(featurizer),MemoizationPolicy(max_history=5)])

    agent.train(training_data_file,
    augmentation_factor = 50,
    epoch=500,
    batch_size=10,
    validation_split=0.2)

    agent.persist(model_path)