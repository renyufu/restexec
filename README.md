# restexec
RESTful command executor with static file serve.

# install
```pip install git+https://github.com/renyufu/restexec.git```

# run 
```
export TOKEN=yourtoken
export CMDS="ls,ls -l,date"

restexec
```

# request
```
curl -s -k -H 'Content-Type: application/json' -H 'X-Auth-Token: yourtoken' -d '{"command": "ls"}' https://localhost/execute
```

# get static file
```
curl -s -k -H -H 'X-Auth-Token: yourtoken' https://localhost:8080/build/ota.bin -o build/ota.bin
```
