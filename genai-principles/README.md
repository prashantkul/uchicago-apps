# Vector Database and Cloud Run Deployment for GenAI Principles
---
## Cloud Run for Application Deployment

### What is Cloud Run?

Cloud Run is a fully managed serverless platform offered by Google Cloud that allows you to deploy and run containerized applications without having to manage the underlying infrastructure.

---

## Instructions

1. **Go to** [console.cloud.google.com](https://console.cloud.google.com)

2. **Open Cloud Shell.**

3. **Create a new Docker repository in Google Cloud Artifact Registry for your group.**  
   Use the naming convention `<group-name>-docker-repo`.

   ```bash
   gcloud artifacts repositories create <docker_repo_name> \
       --repository-format=docker \
       --location=us-central1 \
       --description="Docker repository for Group
       
4. **Authenticate to the repository:**
   ```bash
   gcloud auth configure-docker us-central1-docker.pkg.dev

5. **Build your application as a Docker container:**

   ```bash
   docker build -t us-central1-docker.pkg.dev/adsp-32027-on01/genai-docker-repo/zilliz-app:latest
  
6. **Verify that your image was created successfully by running:**
    ```bash
        docker images #"
        
7. **Push the image to the remote Artifact Registry:**
    ```bash 
        docker push <image_tag>

8. **Deploy the image on Cloud Run**
    ```bash
     gcloud run deploy zilliz-app \
    --image <image_tag> \
    --platform managed \
    --region us-west1 \
    --allow-unauthenticated \
    --set-env-vars ZILLIZ_CLOUD_TOKEN="<token>"
    
    	The ZILLIZ_CLOUD_TOKEN can be copied from the Zilliz cloud console.
    	Replace <image_tag> with your image tag.
