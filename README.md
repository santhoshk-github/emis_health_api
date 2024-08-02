# emis_health_api

below are the list of requirements to build healthcare api

**prerequisites:**
1. python3.8+ version
2. mysql or postgresql db server
3. visual studio code or pycharm editor

**Note:** 
need to update mysql credentials and connection detail for your own. otherwise it won't run.


**Swagger UI:**
http://localhost:8000/docs 

-------------------------------------------
steps for building healthcare app
-------------------------------------------

**Step 1: Setting Up the Environment** 

Create a directory structure for your project:

healthcare_api/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── __init__.py
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

**Step 2: Writing the Code**

main.py - This is the entry point of our FastAPI application
database.py - Set up the database connection
models.py - Define the SQLAlchemy models
schemas.py - Define the Pydantic models (schemas)
crud.py - Define CRUD operations
requirements.txt - Include necessary dependencies


**Step 3: Docker Setup**

Dockerfile - Create a Dockerfile for the FastAPI app

docker-compose.yaml - Set up Docker Compose to manage the FastAPI and MySQL containers:

**Step 4: Running the Application**

Build and run the Docker containers:

docker-compose up --build 

------> **Note:  Mannual Run - uvicorn main:app --reload**


**Step 5: Access the FastAPI documentation:**

Open your browser and go to http://localhost:8000/docs to see the Swagger UI for your API.


**API Endpoints:**
1. `GET /patients/{patient_id}`: Retrieve a patient's care record by ID
2. `POST /patients`: Create a new patient care record
3. `PUT /patients/{patient_id}`: Update a patient's care record
4. `DELETE /patients/{patient_id}`: Delete a patient's care record

**API Request/Response Formats**

- Requests: JSON
- Responses: JSON


**Patient Care Record Model**

- `id` (int, unique identifier)
- `name` (string)
- `age` (int)
- `date_of_birth` (string)
- `medical_history` (string)
- `lab_results` (string)

**Example API Responses:**


- `GET /patients/{patient_id}`:
```
[
  {
    "patient_id": "12345",
    "name": "John Doe",
    "age": "34",
    "date_of_birth": "1990-01-01",
    "medical_history": "diabetes, hypertension - metformin - 500mg twice daily ",
    "lab_results": "blood glucose, 120 mg/dL, 2022-01-01"
  }
  {
    "patient_id": "23456",
    "name": "Yannick Wade",
    "age": "55",
    "date_of_birth": "1969-01-01",
    "medical_history": "diabetes, hypertension - metformin - 500mg twice daily ",
    "lab_results": "blood glucose, 120 mg/dL, 2024-01-01"
  }
]
```

#### **************** Important update ************** ####

-This setup provides a simple healthcare API that can be used to manage patient records with basic CRUD operations. 
-We can extend it further to include more features as needed. 
-Also to secure the application we can add user Admin authention in login process.

#################
