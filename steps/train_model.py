from zenml import step
from typing import Optional
import pandas as pd

@step
def train_model(df: pd.DataFrame) -> Optional[object]:
    """
    Args:
        df (pd.DataFrame): DataFrame to be used in modelling.
    Returns:
        model (object): Trained model.
    """
    # ...existing code...
    # For example, implement your training logic here:
    pass