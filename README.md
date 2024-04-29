# Testes práticos

**Build**

```
docker build -t pyshowinfopod .
docker tag pyshowinfopod:latest joejeff/pyshowinfopod:latest
docker login
docker push joejeff/pyshowinfopod:latest
```


**Deploy**

```
k apply -f pyshowpodinfo.yaml

k get pod

k expose deployment pyshowinfopod-deploy --port 5000 --type NodePort

k get svc

while sleep 1; do curl -s http://192.168.56.111:32718/; done

k scale deployment pyshowinfopod-deploy --replicas=10
k scale deployment pyshowinfopod-deploy --replicas=0
k scale deployment pyshowinfopod-deploy --replicas=2

k delete -f pyshowpodinfo.yaml 
```


#https://docs.docker.com/samples/flask/
