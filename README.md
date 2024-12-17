# IS218 Final

## Video Link
I do not usually talk this slow, but my brain is struggling to put together words while being sick.

[https://youtu.be/7PnVFw_Z4gc?si=5gvvCaWs4X1IoMEM
](https://youtu.be/7PnVFw_Z4gc?si=5gvvCaWs4X1IoMEM)
## About
During the summer, I run an online art-exchange event where participants draw gifts for each other. These gifts are called **'attacks'**. Each person scores their attack to earn points for their team. The event runs for one month, and at the end of the month, the points are tallied and the winning team is announced.

For this final project, I decided to recreate the form that we use for scoring. Once you hit submit, your score is calculated and returned to the form, and all of your form information is stored in a PostgreSQL database.

The cat image came from [here](https://store.line.me/stickershop/product/16919130/en) and the dog image came from [here](https://store.line.me/stickershop/product/15939506/en).

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

