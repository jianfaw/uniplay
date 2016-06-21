# uniplay
Universal Player XBlock v 1.0

## Pre-requirements:
  1. EdX platform installed;
  2. Skilful in operating system of Linux.

## Installations:
#### 1. Make sure you have the following items in your config file - cms.env.json
  
  > "ALLOW_ALL_ADVANCED_COMPONENTS": True
  
  If it does not exist, insert it into the "FEATURES".
  
#### 2. Execute the commands
  * Switch to user "edxapp"
  
  >sudo -H -u edxapp bash
  * Change directory to "edxapp" home
  
  >cd ~
  * Loading the virtual environment of edxapp
  
  >source edxapp_env
  * Clone the XBlock to certain directory
  
  >git clone https://github.com/longmen21/uniplay/
  * Install
  
  >pip install -e ./uniplay
  * Bach to the user "edustack"
  
  >exit
    
#### 3. Restart the CMS platform
  
  >source /edx/bin/supervisorctl restart edxapp:

#### 4. courses settings
  
  >Go to Settings -> Advanced Settings and set advanced_modules to ["uniplay"].

## Suggestions:
  Keep the user "edxapp" clear of the privilege "sudo", you ought to switch user to "edustack" if you need the superior 
  authority.


