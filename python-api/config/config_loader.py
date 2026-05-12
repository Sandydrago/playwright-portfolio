import os
from .dev_config import DevConfig
from .staging_config import StagingConfig
from .prod_config import ProdConfig

def get_config():
    env = os.getenv("TEST_ENV", "dev").lower()

    if env == "staging":
        return StagingConfig()
    elif env == "prod":
        return ProdConfig()
    return DevConfig()
