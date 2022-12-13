# Introduction

For this exam, you'll get the time untill 12h30. When you need an urgent toiletbreak, please ask my colleague Esli or myself.
When you're stuck in the exam, you can ask for help. We'll try to help you as much as possible, but we can't give you the answers.

Estimated time for the exam: 2 hours.

# Steps
1. Docker Flask frontend
2. Docker API fixes
3. GitHub Actions
4. Kubernetes workload
5. Kubectl 

## 1. Docker FASTAPI Frontend
- Total points: 3
- Estimated time: 15 minutes

Create a Dockerfile for the FastAPI frontend webapplication. 
You can find this in the `frontend` directory.
Don't edit the source code.
Add it to the Docker Compose project.
Tag it as `yourname/mlops-exam-1-frontend`
Push it to a registry (Docker Hub or GitHub Container Registry)

## 2. Docker API fixes
- Total points: 3
- Estimated time: 25 minutes

Make sure to fix the Docker API and let it boot up correctly.
There is atleast one error somewhere that you can fix in the source code.
Make sure to get the Docker image tagged as `yourname/mlops-exam-1-backend`.
Check the Docker Compose for that.

## 3. GitHub Actions
- Total points: 3
- Estimated time: 35 minutes

Automate the Docker builds for both the `frontend` and `backend` using GitHub Actions, make sure it can end up on your Docker registry using a `GIT-SHA` tag that is dynamically added.

## 4. Kubernetes workload
- Total points: 6
- Estimated time: 30 minutes

Deploy the frontend and backend into a Kubernetes deployment and use a NodePort service to open them on port `30000` and `30001`.
Create a namespace `exam-nathansegers`

The api requires an environment variable `NAME` and `DATE`, apply these using a ConfigMap.
Test using the `/docker_test` endpoint.
Do this using the Kubernetes Yaml file which you apply using the command line.

In order to make the frontend work in Kubernetes, attach the `API_PORT` environment variable to the frontend deployment. This should contain the value of the port that's exposed on the API.

## 5. Kubectl
- Total points: 5
- Estimated time: 15 minutes

Paste the commands you used in a Word document together with the output. Please note all the details!
- Create an `nginx` deployment with the name `nginx-nathan-segers` in a newly created namespace called `exam-nginx`. Obviously, use your own name! Give it 1 replica and a Kubernetes Tag `exam: version 1`
- Use a seperate command to scale the deployment to 3 replica's
- Now replace the image with `nathansegers/vue-docker:v2.0.0`. Don't change the name here, this is a public image I made for you.
- Create a NodePort service using the commandline
- Delete the deployment and service now.



# Tips
- When you are stuck at a certain part, you can probably pick in from a few milestones so that you can still finish your exam.
- Ask a question when you're really stuck. That way you don't lose precious time and can still score some points.
- Don't be afraid to add an extra screenshot. We rather see one more than one less.
- Work with GitHub so you don't lose your code.

# Hand in
Create a WORD doc with a few screenshots and some extra explanation about the exam.
Write down what went good and what went bad.
Hand in the following on Leho:
- A .ZIP file with all the source code (similar to GitHub)
- a .DOCX Word document with all the screenshots of this assignment.

You can hand it in in one .ZIP

# Questions?
You can ask them in a private message through Teams, or you can raise your hand.
Any technical issues should be addressed with the Helpdesk.