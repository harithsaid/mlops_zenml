import logging
from zenml import step
from typing import Optional
import pandas as pd
from pydantic import BaseModel

class DataCleaningOutput(BaseModel):
    cleaned_df: pd.DataFrame
    
    class Config:
        arbitrary_types_allowed = True  # This allows the DataFrame type

@step
def data_cleaning(df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """
    Args:
        df: Input DataFrame to be cleaned
    Returns:
        Cleaned DataFrame or None if cleaning fails
    """
    pass