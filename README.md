### 📄 `Hi` 

```markdown
# 🚀 CRUD with FastAPI, Docker, and SQLAlchemy

Hi, my name is **Deilhers**, I'm a junior developer and this is a CRUD project built using modern technologies like **FastAPI**, **Docker**, and **SQLAlchemy** to create an efficient and modular environment.

---

## 🛠 Technologies Used

- **FastAPI** – Modern and fast web framework for APIs with Python
- **Docker** – Containers to isolate and replicate environments
- **SQLAlchemy** – ORM for efficient database management
- **PostgreSQL** – Relational database system
- **Pydantic <2.0** – Data validation

---

## ⚙️ Installation Steps

1. **Install Python**
2. Install dependencies (make sure you have `pip`):
   ```bash
   pip install -r requirements.txt

⚠️ Note: The requirements.txt file is incomplete. You also need to install:

pip install SQLAlchemy psycopg2-binary "pydantic<2.0"

    Install Docker

    Run the container from the project directory:

docker compose up --build

Enter the database container and clone the SQL script repository:

git clone https://github.com/Dei-web/Script_SQL.git

Execute the SQL script inside the container to create the database and required tables.

Enter the FastAPI container and run:

uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

Open your browser and go to:

http://localhost:8000

You can also access the interactive API documentation at:

http://localhost:8000/docs
