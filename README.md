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


## Activate (Crack) 

Moved Here : [activateAtlassianSoftware.md](activateAtlassianSoftware.md)

##  Use Reverse Proxy

Moved Here : [Reverse-Proxy-for-Atlassian.md](Reverse-Proxy-for-Atlassian.md)
# P.S
[Jira Images](https://hub.docker.com/r/atlassian/jira-software)
