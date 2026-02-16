# CI/CD Mini Project – Jenkins Freestyle vs Jenkins Pipeline

## Project Overview
This project demonstrates how to implement a simple **CI/CD pipeline** using **Jenkins** with both:
- **Freestyle Job (UI-based)**
- **Pipeline Job (Code-based – Jenkinsfile)**

A **Streamlit Calculator Application** is used as the sample project.  
The same CI/CD workflow is implemented using both job types to understand their differences.

---

## Application Used
**Technology:** Python + Streamlit  
**Application:** Simple Calculator App

### Features
- Addition
- Subtraction
- Multiplication
- Division (with divide-by-zero handling)

---

## CI/CD Workflow
Jenkins performs the following steps:

1. Clone source code from GitHub  
2. Build a Docker image  
3. Push the Docker image to Docker Hub  
4. Send an email notification on successful build  

This workflow is implemented twice:
- Using **Jenkins Freestyle Job**
- Using **Jenkins Pipeline Job**

---

## Project Structure

1. app.py
2. Dockerfile
3. Jenkinsfile
4. CI/CD Mini Project.PDF
5. README.md

# STEP A1: CREATE GITHUB REPOSITORY
1.	Open github.com
2.	Click New Repository
3.	Repository name: Calculator
4.	Select Public
5.	Click Create Repository

<img width="516" height="323" alt="image" src="https://github.com/user-attachments/assets/0a39fb03-f61d-4753-aca0-3c64827358e0" />

---
# STEP A2: CREATE PROJECT FILES (LOCAL SYSTEM)
Open Terminal : Clone the Repository 

### Create app.py & Dockerfile

#### nano app.py
```
import streamlit as st

def calculate(num1, num2, operation):
    if operation == "➕":
        return num1 + num2
    elif operation == "➖":
        return num1 - num2
    elif operation == "✖":
        return num1 * num2
    elif operation == "➗":
        if num2 == 0:
            return None
        return num1 / num2

st.title("📱 Simple Calculator App")
st.subheader("A user-friendly calculator built with Streamlit")

num1 = st.number_input("Enter the first number:", step=1)
num2 = st.number_input("Enter the second number:", step=1)

operation = st.selectbox("Select an operation:", ["➕", "➖", "✖", "➗"])

if operation == "➗" and num2 == 0:
    st.warning("Divided by zero is not allowed!")
else:
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.subheader(f"Result: {result}")
```
#### nano Dockerfile

```
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir streamlit

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```
## Output :
<img width="452" height="281" alt="image" src="https://github.com/user-attachments/assets/2a20d415-8e39-4bcf-ac64-168180008fc4" />
<br>
<br>
<img width="452" height="251" alt="image" src="https://github.com/user-attachments/assets/eb5038ba-df4c-4292-9999-656f5e99ac92" />

---

# STEP A3: PUSH CODE TO GITHUB

```
git add .
git status
git commit -m "jenkins-docker-ci-project"
git remote add origin git@github.com:Abbaskashim/Calculator.git
git push
```
## Output :
<img width="452" height="279" alt="image" src="https://github.com/user-attachments/assets/a801ad50-266f-47be-8c97-74e7981b1904" />
<br>
<br>
<img width="452" height="279" alt="image" src="https://github.com/user-attachments/assets/8246e246-4eaa-46f0-b0b2-5a78625c6351" />

### Output: 

<img width="452" height="282" alt="image" src="https://github.com/user-attachments/assets/ac4c03ef-0944-40cd-917c-0d3030b211ac" />

---

# STEP A4: CREATE FREESTYLE JOB IN JENKINS

1.	Open Jenkins dashboard
2.	Click New Item
3.	Enter name: freestyle-docker-ci
4.	Select Freestyle project
5.	Click OK

## Output :
<img width="475" height="236" alt="image" src="https://github.com/user-attachments/assets/0ef11c5a-8c24-4469-843f-23d1ad841005" />

---

# STEP A5: CONNECT JENKINS TO GITHUB

1.	Click Configure
2.	Scroll to Source Code Management
3.	Select Git
4.	Repository URL: ``` https://github.com/Abbaskashim/Calculator.git ```
5.	Branch: main
6.	Click Save

## Output :
<img width="464" height="220" alt="image" src="https://github.com/user-attachments/assets/065e0f81-9d64-43fb-ac6e-e61622bc6bf3" />

---

STEP A6: BUILD DOCKER IMAGE
1.	Click Configure
2.	Scroll to Build
3.	Click Add Build Step
4.	Select Execute shell
5.	Paste:``` docker build -t abbaskashim/jenkins-demo1:latest . ```

## Output :
<img width="509" height="245" alt="image" src="https://github.com/user-attachments/assets/72e75edf-5a85-4cb1-92ed-e027b9666674" />
<br>
<br>
<img width="524" height="311" alt="image" src="https://github.com/user-attachments/assets/9c2ccbb4-cf3b-420f-8945-0e8f07aab75e" />

---

# STEP A7: PUSH IMAGE TO DOCKER HUB

1.	Click Add Build Step → Execute shell
2.	Paste: ``` docker build -t abbaskashim/jenkins-demo1:latest .```

## Output :
<img width="524" height="324" alt="image" src="https://github.com/user-attachments/assets/bff37682-7a5d-4f83-9bcf-a5c75f3927c4" />

#### Docker Push Output: 

<img width="524" height="296" alt="image" src="https://github.com/user-attachments/assets/2269f1de-55cf-485a-8867-eaac79bdff26" />

---

# STEP A8: EMAIL NOTIFICATION

1.	Scroll to Post-build Actions
2.	Select Email Notification
3.	Enable Send on success
4.	Add your email

## Output :
<img width="523" height="306" alt="image" src="https://github.com/user-attachments/assets/bbc8ad55-e042-40bf-9b55-e683bb425b8a" />

---

# STEP A9: RUN FREESTYLE JOB
1.	Click Build Now
2.	Open Console Output

## Output :
<img width="524" height="310" alt="image" src="https://github.com/user-attachments/assets/4076af55-bd7c-4a5b-808d-ebd52c882243" />

#### Email Notification:

## Output :
<img width="523" height="294" alt="image" src="https://github.com/user-attachments/assets/17b92688-0c47-4eaa-b828-1ef33e6cca2b" />

----
----
# Part B – Jenkins Pipeline CI/CD Project

## Project Overview
This project demonstrates the creation and execution of a Jenkins **Pipeline Job** using a `Jenkinsfile` stored in GitHub.  
The pipeline automates the CI process and sends an email notification after successful execution.  
A comparison between **Freestyle Job** and **Pipeline Job** is also included.

---

## Jenkins Pipeline Job

### Step B1: Create Pipeline Job
1. Open Jenkins Dashboard
2. Click **New Item**
3. Enter Job Name: pipeline-docker-ci
4. Select **Pipeline**
5. Click **OK**

## Output :
<img width="524" height="154" alt="image" src="https://github.com/user-attachments/assets/c8049772-08bb-4a13-a7cf-9e779e4f982e" />

---

### Step B2: Create & Push Jenkinsfile to GitHub

Navigate to your project directory and create the Jenkinsfile:

```bash
nano Jenkinsfile
```
### Push Jenkinsfile TO Github

```
git add .
git commit -m "Jenkin file"
git push
```
## Output :
<img width="524" height="305" alt="image" src="https://github.com/user-attachments/assets/69694542-ff3e-4ce1-805e-7edd496cd9b5" />

----

# STEP B4: CONFIGURE PIPELINE JOB
1.	Job → Configure
2.	Definition: ``` Pipeline script from SCM ```
3.	SCM: Git
4.	Repo URL
5.	Branch: main
6.	Script Path: ``` Jenkinsfile ```
7.	Save

## Output :
<img width="524" height="280" alt="image" src="https://github.com/user-attachments/assets/496814ac-f360-4011-b8d6-21900fa3b1ef" />
<br>
<br>
<img width="524" height="277" alt="image" src="https://github.com/user-attachments/assets/1708c3ae-f614-44a3-856e-0e72ff650a5f" />

# STEP B5: RUN PIPELINE

1.	Click Build Now
2.	Watch stages turn green

## Output :
<img width="524" height="269" alt="image" src="https://github.com/user-attachments/assets/5be3a9c3-a5c5-4c02-b73f-3e35fba352fe" />
<br>
<br>
<img width="524" height="343" alt="image" src="https://github.com/user-attachments/assets/acc40f0a-6117-4abf-93c4-34a752c3c89b" />

# Step B6: Email Notification from Pipeline

1.	Email sent after successful pipeline execution
2.	Must include job and build detail

## Output :
<img width="524" height="255" alt="image" src="https://github.com/user-attachments/assets/9a9bf510-9a81-499f-a66b-2dbeb9a7af7f" />

---
# Part C: Comparison & Analysis

### Step 11: Freestyle vs Pipeline Comparison

#### Criteria	Freestyle Job	Pipeline Job

| Criteria | Freestyle Job | Pipeline Job |
|--------|---------------|--------------|
| Configuration Method | Configured using Jenkins Web UI (manual setup) | Configured using code written in a Jenkinsfile |
| Version Control | ❌ Not version controlled (stored in Jenkins UI) | ✅ Version controlled along with source code |
| Reusability | Low – difficult to reuse across jobs | High – pipeline code can be reused and shared |
| Complexity Handling | Suitable for simple, linear tasks | Designed for complex CI/CD workflows |
| Maintainability | Harder to maintain due to manual changes | Easy to maintain due to code-based configuration |
| Scalability | Limited scalability | Highly scalable for large projects |
| Error Handling | Basic error handling | Advanced error handling using stages and conditions |
| Collaboration | Limited team collaboration | Better collaboration through shared Jenkinsfile |
| Automation Level | Partial automation | Full CI/CD automation |
| Best Use Case | Small projects or beginner tasks | Enterprise-level CI/CD pipelines |






