## Reverse Proxy for Atlassian Software

If Each of Atlassian Software run behind a reverse proxy server (e.g. a load-balancer or nginx server), then you need to specify extra options to make Software aware of the setup. They can be controlled via the below environment variables.


1. uncomment this line in compose file
2. Replace the following variables in the `Composefile` file with 
appropriate values.
   -  `<SCHEME>` Protocol **http/https**
   -  `<SECURE>` Set `true` if `<SCHEME>` is `https`
   -  `<PROXY_PORT>` The reverse proxy's port number via which Application is accessed
   - `<PROXY_NAME>` The reverse proxy's fully qualified hostname




### jira, confluence, Bamboo, Fisheye, Crucible and jira-service Management

```yml
...
environment:      
  ...
  ATL_TOMCAT_SCHEME: '<SCHEME>'
  ATL_TOMCAT_SECURE: '<SECURE>'
  ATL_PROXY_PORT: '<PROXY_PORT>'
  ATL_PROXY_NAME: '<PROXY_NAME>'
  ...
volumes:
...
```
### bitbucket
```yml
...
environment:      
  ...
  SERVER_SCHEME: '<SCHEME>'
  SERVER_SECURE: '<SECURE>'
  SERVER_PROXY_PORT: '<PROXY_PORT>'
  SERVER_PROXY_NAME: 'PROXY_NAME'
  ...
volumes:
...
```

## Edit Conf Files 


1 - edit the conf file in `./nginx/conf.d/`

2 - Replace the following variables in the `conf file` file with appropriate values.

- `<server_name>` : fully qualified hostname
-  `<ssl_certificate_path>` path of certificate File
-  `<ssl_certificate_key_path>` path of certificate Key File

# run Nginx

run [nginx-compose.yml](/nginx-compose.yml)


```bash
docker-compose -f nginx-compose.yml up -d
```
