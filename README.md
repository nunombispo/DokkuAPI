# Dokku API
Dokku API - API to interface with a Dokku installation

This API is built with FastAPI and you can access the docs after installation at [dokku-api-domain]/docs. You can also use the FastAPI docs to test and trial the API methods.


# Introduction
This API allows access with a Dokku installation with an HTTP REST API. This enables more possibilities to remote management of a Dokku server and also for automating application deployment. 

The goal is to provide a standard way of accessing Dokku installations with a remote API, something that Dokku is missing.


# Features
Current supported features:
- Apps (list, create, delete)
- Plugins (list, check if plugin is installed, install, uninstall), currently only supports Postgres, MySQL and LetsEncrypt plugins
- Databases (list, check database exists, create, delete, list linked apps, link, unlink)
- Domains (set, remove, set LetsEncrypt root mail, enable LetsEncrypt for app, enable auto renewal)
- Config (show, set value for key, set keys from file, unset key, apply configurations)

More features are planned to be added soon. The current features allows to deploy an application, set a datastore (database), set domain and enable HTTPS certificates.

# Security
The API is secured with an API KEY that is passed in the header for each request. The API KEY is defined as an ENV variable and must be passed on all requests except the call to the API metadata.


# Pre-requisites
You need access to a Dokku server to install Dokku API as a application. If you don't have a Dokku server, please create a server first. I recommend Digital Ocean since you can get an automatic Dokku installation.

On the Dokku server the following needs to be configured:
```
# Create a Dokku application
$ dokku apps:create dokku-api
```

The Dokku API depends on a couple of ENV variables for specific settings, so the following ENV values must be configured:
```
# Setting dokku-api ENV variables
dokku config:set dokku-api API_NAME="Dokku API" API_VERSION_NUMBER="0.1.1" SSH_HOSTNAME="" SSH_PORT="22"  SSH_KEY_PATH="/dokku-api/id_rsa" SSH_KEY_PASSPHRASE="" API_KEY=""
```
Please set the appropriate values for your setup, SSH_HOSTNAME of your Dokku server (or IP address), SSH_KEY_PASSPHRASE if your private key has a passphrase and API_KEY for the access token between the API and the consuming application.

You can use for instance a UUID generator for the API_KEY, like: https://www.uuidgenerator.net/

The Dokku API also depends on SSH access to the Dokku server to run the commands, which means that SSH keys must be configured and mounted on the Dokku API application.
```
# Create directory for SSH private key
$ sudo mkdir /dokku-api

# Creating private key (copy here the contents of the private key you use to access the Dokky server)
$ sudo nano /dokku-api/id_rsa

# Mounting the directory inside the dokku-api application
$ dokku storage:mount dokku-api /dokku-api/:/dokku-api/
```

# Installation
On your local machine run the following commands:
```
# Clone project
$ git clone https://github.com/nunombispo/DokkuAPI.git

# Change dir
$ cd DokkuAPI

# Add your Dokku server as a remote
$ git remote add dokku dokku@[domain]:dokku-api

# Push repository to Dokku
$ git push dokku
```


You can check additional options on configuring a domain and HTTPS on Dokku Docs: https://dokku.com/docs/deployment/application-deployment/

# Contributing
All contribuitions are welcome
