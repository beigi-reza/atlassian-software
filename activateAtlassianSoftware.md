# Activate Atlassiasn Software


Open Application on browser

Enter the requested information, When asked for license

run `atlassian-agent.jar` in Application container

docker exec **`<container_name>`** java -jar atlassian-agent.jar -m **`<email>`** -o **`<organisation>`** -p **`<product>`** -s **`<ServerID>`**

>NOTE : Server ID is shown at License request step on **Application Setup wizard** 
Copy Produced license to License request field & Click OK


## -m,--mail
License email

## -o,--organisation
License organisation


## -p,--product
License product

List of Product Support

- `jc` : **JIRA Core**
- `jsd` : **JIRA Service Desk**
- `jira`: **JIRA Software**
- `jsm`: **JIRA Service Management**
- `crucible` : **Crucible**
- `conf` : **Confluence**
- `bitbucket` : **Bitbucket**
- `bamboo` : **Bamboo**
- `fisheye` : **FishEye**
- `questions`: **Questions plugin for Confluence**
- `crowd` : **Crowd**
- `capture`: **Capture plugin for JIRA**
- `training`: **Training plugin for JIRA**
- `tc`: **Team Calendars plugin for Confluence**
- `portfolio` : **Portfolio plugin for JIRA**
- `*` : **Third party plugin key**

## example

```bash
docker exec jira java -jar /atlassian-agent.jar -m my@email.com -o mycompany -p jc -s BFDY-ET5R-24G4-5B84
```


## Refrence & Links

https://zhile.io/

https://github.com/hgqapp/atlassian-agent

https://gitee.com/gfly/atlassian-agent

