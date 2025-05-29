# model_repo
Deploy model using K8

Setting up the env:
> pip install fastapi uvicorn python-multipart pillow torch torchvision
- Dockerfile in ModelInfService
- go to ModelInfService
> uvicorn app:app --reload



Dependecies Used
- fastAPi
- torch
- torch vision

Containisation:
- Build Image > docker build -t modelinfservice:1.0 . 
- Run the image > docker run -p 8000:8000  modelinfservice:1.0  

    Create minikube cluster
    > minikube start
    - load image (for local testing)
    >  minikube image load modelinfservice:1.0

    Create deployment
    > kubectl create deployment modelinf-service --image=modelinfservice:1.0
    alternatively from yml
    > kubectl apply -f deployment.yml
    to delete deployment
    > kubectl delete -f deployment.yml
    Check pods
    > kubectl get pods
    Check logs
    > kubectl logs <pod_name>

    Create Service
    > kubectl expose deployment modelinf-service --type=NodePort --port=8000
    Expose minikubes service
    >  minikube service modelinf-service

    We will get the exposed ip and port, and we can access our API to our Model


Monitoring
minikube dashboad - http://127.0.0.1:53020/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/#/workloads?namespace=default