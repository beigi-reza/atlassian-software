# Atlassian Software Docker Compose + Activate
This prject run & Activate (crack) Attlasian software as docker container, All programs can be run behind a reverse proxy


## Run Application
### Jira
run [jira-compose.yml](/jira-compose.yml)

```bash
docker-compose -f jira-compose.yml up -d
```
> Use `http://<ip>:8080`

### Confluence

run [confluence-compose.yml](/confluence-compose.yml)

```bash
docker-compose -f confluence-compose.yml up -d
```
> Use `http://<ip>:8090`

### bitbucket

run [bitbucket-compose.yml](/bitbucket-compose.yml)

```bash
docker-compose -f confluence-compose.yml up -d
```
> Use `http://<ip>:8090`

### Bamboo

run [bamboo-compose.yml](/bamboo-compose.yml)

```bash
docker-compose -f bamboo-compose.yml up -d
```
> Use `http://<ip>:8085`

### Fisheye & Crucible

run [fisheys-compose.yml](/fisheys-compose.yml)

```bash
docker-compose -f fisheys-compose.yml up -d
```
> Use `http://<ip>:8088`


### Jira Server Manegment (Service Desk)

run [servicemanagement-compose.yml](/servicemanagement-compose.yml)

```bash
docker-compose -f servicemanagement-compose.yml up -d
```
> Use `http://<ip>:8088`


## Active Software

Moved Here : [activate.md](activate.md)

## Config Reverse Proxy
If Each of Atlassian Software run behind a reverse proxy server (e.g. a load-balancer or nginx server), then you need to specify extra options to make Software aware of the setup. They can be controlled via the below environment variables.
**uncomment this line in compose file** and correction this 

### jira, confluence, Bamboo, Fisheye, Crucible and jira-service Management

```yml
...
environment:      
  ...
  ATL_TOMCAT_SCHEME: 'https'
  ATL_TOMCAT_SECURE: 'true'
  ATL_PROXY_PORT: '443'
  ATL_PROXY_NAME: 'jira.mysite.com'
  ...
volumes:
...
```
### bitbucket
```yml
...
environment:      
  ...
  SERVER_SCHEME: 'https'
  SERVER_SECURE: 'true'
  SERVER_PROXY_PORT: '443'
  SERVER_PROXY_NAME: 'bitbucket.mysite.com'
  ...
volumes:
...
```

# P.S
[Jira Images](https://hub.docker.com/r/atlassian/jira-software)
