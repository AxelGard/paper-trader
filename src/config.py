
"""Base config dict """
config_dict = {
    "DEBUG" : False
}


def ProductionConfig():
    """ for production config."""
    global config_dict
    config_dict["DEBUG"] = False


def DevelopmentConfig():
    """ Config for development """
    global config_dict
    config_dict["DEBUG"] = True
    
