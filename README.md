# IS218 Final

## About
During the summer, I run an online art-exchange event where participants draw gifts for each other. These gifts are called **'attacks'**. Each attack is scored to earn points for your team. The event runs for one month, and at the end of the month, the points are tallied and the winning team is announced.

Typically, we use a form service and Google Sheets to collect data and perform calculations.

For this final project, I decided to recreate the form we use. The information entered in the form is scored and sent to a PostgreSQL database.

## Installation

### 1. Clone the repository:
```bash
git clone <repository_url>
```

### 2. Create the `.env` file
Create a `.env` file in the project root and add the following variables:
```env
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fastapi_db
# Change the below to 'True' only when running pytest
TEST_MODE=False
```

### 3. Build and run the Docker containers:
```bash
docker-compose up --build
```

### 4. Access the Website and API Documentation
- Visit the website at: [http://localhost:8000/](http://localhost:8000/)
- Access the API Docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

### 5. Open pgAdmin
- Navigate to [http://localhost:5050/](http://localhost:5050/)
- **Login Credentials**:
  - Email: `admin@example.com`
  - Password: `admin`

### 6. Configure pgAdmin
- Click **'Add New Server'** and configure the following settings:
  - **General Tab**:
    - Name: `FastAPI PostgreSQL`
  - **Connection Tab**:
    - Host: `db` (as defined in `docker-compose.yml`)
    - Port: `5432`
    - Maintenance Database: `fastapi_db`
    - Username: `postgres`
    - Password: `postgres`
  - Click **"Save"** to establish the connection.

### 7. Shut down the containers
To stop the containers, run:
```bash
docker-compose down
```

