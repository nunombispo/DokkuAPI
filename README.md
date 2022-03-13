# Dokku API
Dokku API - API to interface with a Dokku installation

This API is built with FastAPI and you can access the docs after installation at [dokku-api-domain]/docs. You can also use the FastAPI docs to test and trial the api methods.


# Introduction
This api allows access with a Dokku installation with an HTTP REST API. This enables more possibilities to remote management of a Dokku server and also for automating application deployment. 

The goal is to provide a standard way of accessing Dokku installations with a remote API, something that Dokku is missing.


# Features
Current supported features:
- Apps (list, create, delete)
- Plugins (list, check if plugin is installed, install, uninstall), currently only supports Postgres, MySQL and LetsEncrypt plugins
- Databases (list, check database exists, create, delete, list linked apps, link, unlink)
- Domains (set, remove, set LetsEncrypt root mail, enable LetsEncrypt for app, enable auto renewal)

More features are planned to be added soon. The current features allows to deploy an application, set a datastore (database), set domain and enable HTTPS certificates.

# Security
No security is currently implemented in the API. After deployment it is available on the deployment URL or IP:PORT address without any security. Be aware of this if you expose it externally.
An API token feature is planned to be added soon.


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
dokku config:set dokku-api API_NAME="Dokku API" API_VERSION_NUMBER="0.1" SSH_HOSTNAME="" SSH_PORT="22"  SSH_KEY_PATH="/dokku-api/id_rsa" SSH_KEY_PASSPHRASE=""
```
(Please set the appropriate values for your setup, SSH_HOSTNAME and SSH_KEY_PASSPHRASE if your private key has a passphrase)

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

# Add your Dokku server as a remote
$ git remote add dokku dokku@[domain]:dokku-api

# Push repository to Dokku
$ git push dokku
```


You can check additional options on configuring a domain and HTTPS on Dokku Docs: https://dokku.com/docs/deployment/application-deployment/

# Contributing
All contribuitions are welcome
