# Install and Crack Atlassian Software As Docker Comtainer

This prject run & crack attlasian software as docker container, all ppplication run behind a reverse proxy server


## JIRA

run a composefile

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
    docker exec jira java -jar atlassian-agent.jar -m r.beigy@gmail.com -o jira -p jira -s B0F2-VAOH-QRK0-E331
    ```
- NOTE : **Server ID** is shown at License request step on JIRA Setup wizard

