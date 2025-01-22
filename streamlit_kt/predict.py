"""TODO 
    Make predictions with the linear regression trained model (model_penguins.pkl). 
    The model predicts the body_mass_g given the input features: flipper_length_mm, species and sex
    1. Read in the model from the file
    2. Set the value of flipper_length to a number between 160 and 240
    3. Set the value of species to one of the possible options 'Adelie','Chinstrap','Gentoo'
    4. Set the value of sex to 'Female' or 'Male'
    5. Let's create a dictionary having as keys the input features 
    6. create a dataframe from the input_dict_X 
    7. Make predictions
"""

### Import libraries
import pickle
import streamlit as st
import pandas as pd
from utils import load

