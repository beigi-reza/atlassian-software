# Atlassian Software Docker Compose with crack

This prject run & crack Attlasian software as docker container, All programs can be run behind a reverse proxy


## reverse proxy
If Each of Atlassian Software run behind a reverse proxy server (e.g. a load-balancer or nginx server), then you need to specify extra options to make Software aware of the setup. They can be controlled via the below environment variables.
**uncomment this line in compose file** and correction this 

### jira, confluence
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


## Run Jira
run [jira-compose.yml](/jira-compose.yml)

```bash
docker-compose -f jira-compose.yml up -d
```
> Use `http://<ip>:8080`

## Run Confluence

run [confluence-compose.yml](/confluence-compose.yml)

```bash
docker-compose -f confluence-compose.yml up -d
```
> Use `http://<ip>:8090`

## Run bitbucket

run [bitbucket-compose.yml](/bitbucket-compose.yml)

```bash
docker-compose -f confluence-compose.yml up -d
```
> Use `http://<ip>:8090`

## Run Bamboo

run [bamboo-compose.yml](/bamboo-compose.yml)

```bash
docker-compose -f bamboo-compose.yml up -d
```
> Use `http://<ip>:8085`

# P.S
[Jira Images](https://hub.docker.com/r/atlassian/jira-software)

## Run Fisheye & Crucible

run [fisheys-compose.yml](/fisheys-compose.yml)

```bash
docker-compose -f fisheys-compose.yml up -d
```
> Use `http://<ip>:8088`

# P.S
[Jira Images](https://hub.docker.com/r/atlassian/jira-software)
