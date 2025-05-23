# House Billing Management System

## Project Structure

```
house-billing-system/
├── frontend/                      # Vue.js frontend application
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── assets/               # Static assets (images, fonts, etc.)
│   │   ├── components/           # Reusable Vue components
│   │   │   ├── auth/
│   │   │   │   ├── Login.vue
│   │   │   │   └── Register.vue
│   │   │   ├── bills/
│   │   │   │   ├── BillForm.vue
│   │   │   │   ├── BillList.vue
│   │   │   │   └── BillCard.vue
│   │   │   └── common/
│   │   │       ├── Navbar.vue
│   │   │       └── Footer.vue
│   │   ├── views/                # Page components
│   │   │   ├── Home.vue
│   │   │   ├── Dashboard.vue
│   │   │   ├── Bills.vue
│   │   │   └── Profile.vue
│   │   ├── router/               # Vue Router configuration
│   │   │   └── index.js
│   │   ├── store/                # Vuex store
│   │   │   ├── index.js
│   │   │   ├── modules/
│   │   │   │   ├── auth.js
│   │   │   │   └── bills.js
│   │   │   ├── services/             # API services
│   │   │   │   ├── api.js
│   │   │   │   ├── auth.service.js
│   │   │   │   └── bills.service.js
│   │   │   ├── utils/                # Utility functions
│   │   │   │   └── helpers.js
│   │   │   ├── App.vue
│   │   │   └── main.js
│   │   ├── package.json
│   │   └── vite.config.js
│   ├── backend/                       # FastAPI backend application
│   │   ├── app/
│   │   │   ├── api/                  # API routes
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   └── bills.py
│   │   │   ├── core/                 # Core functionality
│   │   │   │   ├── __init__.py
│   │   │   │   ├── config.py
│   │   │   │   ├── security.py
│   │   │   │   └── database.py
│   │   │   ├── models/               # Database models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   └── bill.py
│   │   │   ├── schemas/              # Request/Response schemas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── user.py
│   │   │   │   └── bill.py
│   │   │   ├── services/             # Business logic
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   └── bills.py
│   │   │   └── utils/                # Utility functions
│   │   │       ├── __init__.py
│   │   │       └── helpers.py
│   │   ├── tests/                    # Test files
│   │   │   ├── __init__.py
│   │   │   ├── test_auth.py
│   │   │   └── test_bills.py
│   │   ├── requirements.txt
│   │   └── main.py
│   ├── .gitignore
│   ├── README.md
│   └── docker-compose.yml
```

## Key Components

### Frontend (Vue.js)
- **Components**: Reusable UI components for authentication, bills management, and common elements
- **Views**: Main page components for different routes
- **Store**: Vuex store for state management
- **Services**: API integration services
- **Router**: Route configuration for navigation

### Backend (FastAPI)
- **API Routes**: Endpoints for authentication and bills management
- **Models**: Database models for users and bills
- **Schemas**: Request/Response data structures
- **Services**: Business logic implementation
- **Core**: Configuration, security, and database setup

### Database (Neon Postgres)
- User table for authentication
- Bills table for expense tracking
- Relationships between users and bills

## Features
1. User Authentication
   - Registration
   - Login
   - Password reset

2. Bills Management
   - Add new bills (Internet, Rent, Water, Electricity, EMIs)
   - View bill history
   - Edit/Delete bills
   - Filter and search bills
   - Bill categorization
   - Due date tracking

3. Dashboard
   - Overview of all bills
   - Monthly expense summary
   - Payment status
   - Due bills alerts

4. User Profile
   - Personal information
   - Preferences
   - Notification settings

## Technology Stack
- Frontend: Vue.js 3 with Composition API
- Backend: FastAPI
- Database: Neon Postgres
- Authentication: JWT
- Styling: Tailwind CSS
- State Management: Vuex
- API Communication: Axios 