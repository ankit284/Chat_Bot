from rasa_core.agent import Agent 
from rasa_core.policies.keras_policy import KerasPolicy 
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer) 
from rasa_core.policies.fallback import FallbackPolicy

import logging

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    training_data_file = './data/ankit_stories.md'
    model_path = './models/dialogue'
    # fallback = FallbackPolicy(fallback_action_name="action_default_fallback", core_threshold=0.001,nlu_threshold=0.001)
    
    featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=100)

    agent = Agent('./restaurant_domain.yml',policies=[KerasPolicy(featurizer),MemoizationPolicy(max_history=100)])

    agent.train(training_data_file,
    augmentation_factor = 50,
    epoch=500,
    batch_size=10,
    validation_split=0.2)

    agent.persist(model_path)
