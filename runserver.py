'''
Created on Oct 29, 2016

@author: salami
'''

# Configurations
from chloroform import app
app.config.from_object('cfg.default_settings')
#Set this variable and make it point to a configuration file if you want to override default settings
# > export CHLOROFORM_SETTINGS=/path/to/settings.py
#app.config.from_envvar('CHLOROFORM_SETTINGS')
app.run()