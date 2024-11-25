# Setup Instructions
# Team Onboarding Instructions

| **Step** | **Task**                             | **Command/Details**                                                                                           | **Notes**                                                                                   |
|----------|--------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **1**    | Clone the Repository                | `git clone <repository-url>`                                                                                  | Replace `<repository-url>` with the actual repository URL.                                  |
|          | Navigate to the Project Directory   | `cd CS5200_PWW_DB_Implementation`                                                                             |                                                                                             |
| **2**    | Set Up Python Virtual Environment   | `python3 -m venv venv`                                                                                        | Creates an isolated Python environment in the project folder.                               |
|          | Activate Virtual Environment        | - macOS/Linux: `source venv/bin/activate`<br>- Windows: `venv\Scripts\activate`                               | Look for `(venv)` in your terminal prompt to confirm activation.                            |
| **3**    | Install Dependencies                | `pip install -r requirements.txt`                                                                             | Ensure the virtual environment is activated before running this command.                    |
| **4**    | Set Up Configuration                | Create `.env` file: `touch .env`                                                                              |                                                                                             |
|          | Add Environment Variables           | ```env<br>FLASK_APP=run.py<br>FLASK_ENV=development<br>SECRET_KEY=<your_secret_key>```                         | Replace `<your_secret_key>` with a secure string.                                           |
| **5**    | Run the Application                 | `python run.py`                                                                                               | Starts the Flask development server.                                                        |
| **6**    | Access the Application              | Open a browser and navigate to `http://127.0.0.1:5000/`.                                                      |                                                                                             |
| **7**    | Testing                             | Run tests with `pytest`                                                                                       | Verifies that all implemented features work correctly.                                       |
| **8**    | Contribute to Code                  | Create a new branch: `git checkout -b <feature-branch-name>`                                                  | Replace `<feature-branch-name>` with a descriptive branch name.                             |
|          | Add and Commit Changes              | `git add .`<br>`git commit -m "Describe your changes"`                                                        | Use clear, concise commit messages.                                                         |
|          | Push Changes                        | `git push origin <feature-branch-name>`                                                                       |                                                                                             |
|          | Open a Pull Request (PR)            | Use your version control platform (e.g., GitHub) to create a PR for review.                                   | Ensure the branch passes tests before requesting a review.                                  |
| **9**    | Use Postman for API Testing         | Import Postman collection from `tests/postman/collection.json`.                                               | Configure environment variables in Postman as needed: `BASE_URL=http://127.0.0.1:5000`.    |
| **10**   | Folder Structure Overview           | ```plaintext<br>CS5200_PWW_DB_Implementation/<br>├── app/<br>│   ├── __init__.py<br>│   ├── routes/<br>│   │   ├── public_routes.py<br>│   ├── templates/<br>│   │   ├── home.html<br>├── venv/<br>├── requirements.txt<br>├── run.py<br>``` | Refer to this for understanding project organization.                                       |



This document provides step-by-step instructions to set up the **CS5200 PWW Database Implementation** project, including installing dependencies, configuring the database, running the application locally, and testing.

---
## 1. Project Overview
The **CS5200 PWW Database Implementation** project is designed to manage and interact with a repository of Proofs Without Words (PWW). This project includes:
- Public access to view proofs
- Admin dashboard for managing proofs and users
- Modular Flask-based architecture
- Scalable database design with Flask-SQLAlchemy and migrations

## 2. Technology Stack


| **Component**   | **Language**   | **Version**    | **Libraries**                                | **Notes**                                                                                                                                         |
|------------------|----------------|----------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**      | Python         | 3.x            | Flask, Flask-SQLAlchemy, Flask-Migrate      | - Flask handles routing, server-side logic, and database interaction. <br> - **GPT IDEA:** Use Flask Blueprints to separate functionality by feature (e.g., public vs. admin routes). |
| **Frontend**     | HTML           | N/A            | Jinja2                                      | - Static assets (CSS, JavaScript) are managed in the `app/static/` folder.                                                                        |
| **Database**     | SQL            | MySQL 8.x      | SQLAlchemy, Flask-Migrate                   | - The project uses SQLAlchemy for ORM and Flask-Migrate for database migrations.                                                                  |
| **Testing**      | Python         | 3.x            | Pytest                                      | - Unit and integration tests are implemented in the `tests/` folder to validate models, routes, and application logic.                            |
|                  | N/A            | Postman        | N/A                                         | - Postman is used for manual testing of API endpoints during development. <br> - Postman collections are shared among team members for consistent testing. |


---

## 3. Project Structure

The project is organized as follows:
```plaintext
CS5200_PWW_DB_Implementation/
├── app/
│   ├── __init__.py            # Application factory and app initialization
│   ├── models.py              # Database models for tables
│   ├── routes/
│   │   ├── __init__.py        # Blueprint setup
│   │   ├── public_routes.py   # Routes for public users
│   │   ├── admin_routes.py    # Routes for admin features
│   │   ├── user_routes.py     # Routes for user-specific functionality
│   ├── templates/             # HTML templates for rendering pages
│   │   ├── public/
│   │   │   ├── home.html
│   │   │   ├── proof_detail.html
│   │   ├── admin/
│   ├── static/                # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── scripts.js
├── migrations/                # Flask-Migrate database migrations
├── tests/                     # Unit and integration tests
│   ├── test_models.py         # Tests for database models
│   ├── test_routes.py         # Tests for routes and APIs
├── venv/                      # Virtual environment folder
├── config.py                  # Configuration file
├── requirements.txt           # Python dependencies
├── run.py                     # App entry point
├── README.md                  # Project documentation
├── SETUP.md                   # Setup instructions
```

## 4. Access Control: Role-Based Permissions Table

| **Role**             | **Permissions**                                                                                     | **Use Cases**                                                                                                   | **Access Scope**                                    | **Time Limitations**            |
|-----------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------|
| **Editors**           | - Full CRUD on all proofs (public and private).                                                    | - Approve new entries submitted by public users.                                                              | All proofs and content (public and private).       | Unlimited access.               |
|                       | - Authorize new users for specific roles (e.g., referee, data entry staff).                        | - Update existing proofs and their metadata.                                                                  |                                                    |                                  |
|                       | - Manage public access settings for content (e.g., limited public access to images).               | - Assign limited-time access to referees.                                                                     |                                                    |                                  |
| **Data Entry Staff**  | - Create, Read, and Update proofs and metadata they are assigned to.                                | - Add new entries to the database.                                                                            | Proof metadata and images they are assigned.       | Unlimited access (while active).|
|                       | - Cannot delete or manage user permissions.                                                        | - Update metadata (e.g., tags, topics, MSC Codes).                                                            |                                                    |                                  |
|                       |                                                                                                     | - Upload associated images or files for proofs.                                                               |                                                    |                                  |
| **Referees**          | - Read-only access to all proofs (public and private).                                              | - Review content for quality or accuracy.                                                                     | All proofs (public and private).                   | Limited access dates.           |
|                       | - Cannot create, update, or delete content.                                                        | - Provide feedback during their limited access window.                                                        |                                                    |                                  |
| **Public Users**      | - Read-only access to published public proofs.                                                     | - Explore publicly published proofs for educational or research purposes.                                      | Publicly available proofs only.                    | Unlimited access (public).      |


---

## Access Control Logic

### 1. Role Assignment
- Assign roles (Editor, Data Entry Staff, Referee, Public) during user creation.
- Use a relational database table like `roles` to manage role permissions.

### 2. Access Filters
- Apply role-based filters on API endpoints:
  - **Editors:** No restrictions.
  - **Data Entry Staff:** CRU all proofs, except remove ability to change proof access level
  - **Referees:** Read-only filter for all proofs.
  - **Public:** Read-only filter for public proofs.

### 3. Time-Limited Access
- Use a `start_date` and `end_date` field for roles like Referee.
- Deny access automatically after the `end_date`.

---

## Implementation Plan
1. Set up the **roles** and **permissions schema** in the database.
2. Implement **role-based access control (RBAC)** in the backend.
3. Add **time-limit logic** for roles like referees.
4. Define access-level filtering for key API endpoints.

---

## 5. Front End Views & API Calls

### A. Home Page
**Purpose:** Landing page for database, show all public proofs


| **Objective**   | **API Call**           | **Method** | **Endpoint**           | **Request Body**                 | **Response Fields**                          | **Edge Cases**                               | **Access Level**       | **Data Returned**                                    | **Authentication**  | **Authorization**              |
|------------------|------------------------|------------|------------------------|-----------------------------------|----------------------------------------------|-----------------------------------------------|------------------------|-----------------------------------------------------|---------------------|-------------------------------|
| 1                | Get Proofs            | GET        | `/proofs`              | None                              | `[{id, title, summary}]`                     | 404 if no proofs are found.                   | Public, User, Admin    | Public proofs for public users, user-owned proofs for logged-in users, all proofs for admins | Optional (for public) | Role-based filtering applies   |
| 2                | Search Proofs         | GET        | `/proofs/search`       | None (use query params: `?query`, `tags`, `type`) | `[{id, title, description}]`                 | 204 if no results match the query.            | Public, User, Admin    | Public proofs for public users, user-owned proofs for logged-in users, all proofs for admins | Optional            | Role-based filtering applies   |




---
---
---
everything below is just starting point ideas, need to go through and pair down


## 1. Login Page
**Purpose:** Allow authorized users to sign in 

### API Calls:
| API Call      | Method | Endpoint     | Request Body                         | Response Fields             | Edge Cases                              |
|---------------|--------|--------------|--------------------------------------|-----------------------------|-----------------------------------------|
| User Login    | POST   | `/login`     | `{username_or_email, password}`      | `{access_token, user_role}` | 401 if credentials are invalid.         |
| User Logout   | POST   | `/logout`    | None                                 | `{message}`                 | 401 if user is not authenticated.       |

**Details:**

- **`POST /login`:**
  - **Purpose:** Authenticates the user and provides an access token for authorized actions.
  - **Request Body:**
    - `username_or_email` (required): The user's username or email.
    - `password` (required): The user's password.
  - **Response Fields:**
    - `access_token`: A token used for authenticated requests.
    - `user_role`: The role of the user (`public`, `editor`, `data_entry`, `referee`, `admin`).
  - **Edge Case Handling:**
    - 401 Unauthorized if the credentials are invalid or missing.
    - 400 Bad Request if required fields are missing.

- **`POST /logout`:**
  - **Purpose:** Logs the user out by invalidating the access token.
  - **Request Body:** None.
  - **Response Fields:**
    - `message`: Confirmation message upon successful logout.
  - **Edge Case Handling:**
    - 401 Unauthorized if the user is not authenticated or the token is invalid.

---



## 2. Proof Detail Page
**Purpose:** Displays detailed metadata and content for a specific proof.

### API Calls:
| API Call          | Method | Endpoint           | Request Body | Response Fields                          | Edge Cases                  |
|-------------------|--------|--------------------|--------------|------------------------------------------|-----------------------------|
| Get Proof Details | GET    | `/proofs/:id`      | None         | `{id, title, description, author, tags}` | 404 if the proof is not found. |

---

## 3. Public Proof Submission Page
**Purpose:** Enables public users to submit a proof for review.

### API Calls:
| API Call          | Method | Endpoint          | Request Body                           | Response Fields         | Edge Cases                  |
|-------------------|--------|-------------------|----------------------------------------|-------------------------|-----------------------------|
| Submit Proof      | POST   | `/proofs/submit`  | `{title, description, image, author}`  | `{id, status}`          | 400 if required fields are missing. |

---

## 4. Editor Dashboard
**Purpose:** Central hub for editors to manage database entries and permissions.

### API Calls:
| API Call              | Method | Endpoint           | Request Body | Response Fields                  | Edge Cases                  |
|-----------------------|--------|--------------------|--------------|----------------------------------|-----------------------------|
| Get Pending Proofs    | GET    | `/editor/proofs`   | None         | `[{id, title, status}]`          | 403 if unauthorized.        |

---

## 5. PWW Entry Management Page
**Purpose:** Detailed view to manage or edit a single proof.

### API Calls:
| API Call           | Method | Endpoint             | Request Body                     | Response Fields                  | Edge Cases                  |
|--------------------|--------|----------------------|----------------------------------|----------------------------------|-----------------------------|
| Update Proof       | PUT    | `/editor/proofs/:id` | `{title, description, tags}`     | `{id, title, description}`       | 404 if proof is not found.  |
| Delete Proof       | DELETE | `/editor/proofs/:id` | None                             | `{message}`                      | 404 if proof is not found.  |

---

## 6. User Access Management Page
**Purpose:** Allows editors to manage access for other users.

### API Calls:
| API Call           | Method | Endpoint               | Request Body                     | Response Fields                 | Edge Cases                   |
|--------------------|--------|------------------------|----------------------------------|---------------------------------|------------------------------|
| Manage User Access | POST   | `/admin/users/access`  | `{user_id, role, expiration}`    | `{message}`                     | 403 if unauthorized.         |

---

## 7. Data Entry Dashboard
**Purpose:** Allows data entry staff to add new entries or update existing ones.

### API Calls:
| API Call         | Method | Endpoint             | Request Body               | Response Fields                  | Edge Cases                  |
|------------------|--------|----------------------|----------------------------|----------------------------------|-----------------------------|
| Add New Entry    | POST   | `/data/entries`      | `{title, description}`     | `{id, title}`                    | 400 if required fields are missing. |
| Update Entry     | PUT    | `/data/entries/:id`  | `{title, description}`     | `{id, title, description}`       | 404 if entry is not found.  |

---

## 8. Referee Dashboard
**Purpose:** Enables referees to review database content for limited periods.

### API Calls:
| API Call         | Method | Endpoint               | Request Body | Response Fields                  | Edge Cases                  |
|------------------|--------|------------------------|--------------|----------------------------------|-----------------------------|
| Get All Entries  | GET    | `/referee/entries`     | None         | `[{id, title, description}]`     | 403 if unauthorized.        |

---

## 9. Advanced Search Page
**Purpose:** Allows detailed searches based on various filters.

### API Calls:
| API Call         | Method | Endpoint               | Request Body                       | Response Fields                  | Edge Cases                  |
|------------------|--------|------------------------|------------------------------------|----------------------------------|-----------------------------|
| Search Proofs    | GET    | `/proofs/search`       | `?query=keywords&tags=tag1,tag2`  | `[{id, title, description}]`     | 204 if no results found.    |

---

## 10. Export Data Page
**Purpose:** Enables users to export citation information in various formats.

### API Calls:
| API Call        | Method | Endpoint               | Request Body | Response Fields                  | Edge Cases                  |
|-----------------|--------|------------------------|--------------|----------------------------------|-----------------------------|
| Export Data     | GET    | `/proofs/export`       | `?format=bibtex` | `file`                          | 400 if format is invalid.   |

---

## 11. System Health Dashboard
**Purpose:** Provides admins with insights into system health and usage.

### API Calls:
| API Call           | Method | Endpoint              | Request Body | Response Fields                  | Edge Cases                  |
|--------------------|--------|-----------------------|--------------|----------------------------------|-----------------------------|
| Get System Status  | GET    | `/admin/health`       | None         | `{status, uptime, usage_metrics}`| 503 if server is down.      |

---

## 12. Settings Page
**Purpose:** Allows administrators to configure system settings.

### API Calls:
| API Call          | Method | Endpoint               | Request Body                     | Response Fields                 | Edge Cases                  |
|-------------------|--------|------------------------|----------------------------------|---------------------------------|-----------------------------|
| Update Settings   | PUT    | `/admin/settings`      | `{setting_name, setting_value}`  | `{message}`                     | 403 if unauthorized.        |

---







