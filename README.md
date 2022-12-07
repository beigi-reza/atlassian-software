# Atlassian Software Docker Compose with crack

This prject run & crack Attlasian software as docker container, all Application run behind a reverse proxy server


## Jira
If Jira is run behind a reverse proxy server (e.g. a load-balancer or nginx server) as described here, then you need to specify extra options to make Jira aware of the setup. They can be controlled via the below environment variables.
uncomment this line in `jira-compose.yml` and edit this 

```yml
...
hostname: jira
environment:      
  ...
  #ATL_TOMCAT_SCHEME: 'https'
  #ATL_TOMCAT_SECURE: 'true'
  #ATL_PROXY_PORT: '443'
  #ATL_PROXY_NAME: 'jira.my-site.com'
  ...
volumes:
...
```

run a [jira-compose.yml](/jira-compose.yml)

```bash
docker-compose -f jira-compose.yml up -d
```
> Use `http://<ip>:8080`

### Crack Jira

1. open `http://<ip>:8080` on browser
2. Edit Name & Address & click Next
3. When asked for license
4. Run `atlassian-agent.jar` in jira container

    ```bash
    docker exec jira java -jar atlassian-agent.jar -m r.beigy@gmail.com -o jira -p jira -s <ServerI D>
    ```
   - NOTE : **Server ID** is shown at License request step on JIRA Setup wizard

4. Copy Produced license to Jira License request field & Click Next

## Confluence

run a [confluence-compose.yml](/confluence-compose.yml)

```bash
docker-compose -f confluence-compose.yml up -d
```
> Use `http://<ip>:8090`
### Crack Confluence

1. open `http://<ip>:8090` on browser
3. When asked for license
4. Run `atlassian-agent.jar` in jira container

    ```bash
    docker exec confluence java -jar atlassian-agent.jar -m r.beigy@gmail.com -o confluence -p confluence -s B0F2-VAOH-QRK0-E331
    ```
   - NOTE : **Server ID** is shown at License request step on JIRA Setup wizard

4. Copy Produced license to Jira License request field & Click Next

