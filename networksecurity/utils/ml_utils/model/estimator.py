from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys

class NetworkModel:
    def __init__(self, preprocessor, model):

        try:
            self.model = model
            self.preprocessor = preprocessor
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def predict(self, x):
        x_transform  = self.preprocessor.transform(x)
        y_hat = self.model.predict(x_transform)
        return y_hat