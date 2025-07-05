from zenml import pipeline
import pandas as pd
import logging

import sys
sys.path.append('C:\\Users\\hsaid\\Downloads\\ZENML_blueprint')

from steps.ingest_data import data_ingestion
from steps.clean_data import data_cleaning
from steps.train_model import train_model
from steps.evaluate_model import evaluate_model


@pipeline
def train_pipeline(data_path: str) -> None:
    """Pipeline to train a model."""
    # Step 1: Ingest data
    df = data_ingestion()
    
    # Step 2: Clean data
    cleaned_data = data_cleaning(df)
    
    # Step 3: Train model
    model = train_model(df)
    
    # Step 4: Evaluate model
    evaluate_model(model)