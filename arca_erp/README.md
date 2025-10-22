# ARCA ERP

ARCA ERP is a modular, API-first Enterprise Resource Planning system built with Python, Django, and Django REST Framework. It follows a clean, domain-driven architecture with a service-layer pattern.

## Overview

The system is composed of over 35 modules categorized into logical layers, such as Core Business, HR, Finance, Retail, and SCM. Each module is an independent Django app, exposing its own set of RESTful APIs.

### Tech Stack

- **Backend:** Django 5+, Django REST Framework
- **Database:** PostgreSQL 15
- **Cache/Queue:** Redis (for Celery)
- **Authentication:** JWT (via SimpleJWT)
- **API Documentation:** Swagger (via drf-yasg)
- **Development Environment:** Docker Compose

## Modules

### Core Business Layer
- `finance_core`: General ledger, journal entries, trial balance, chart of accounts
- `cost_mgmt`: Budgeting, cost centers, profitability
- `material_core`: Procurement, vendor master, goods receipt
- `order_mgmt`: Sales orders, delivery, invoicing
- `warehouse_x`: Warehouse management, bins, stock movement
- `asset_care`: Asset tracking, depreciation, maintenance
- `prod_core`: Production planning, routing, work orders
- `quality_core`: Quality checks, audits, compliance certificates

### Human & Organizational
- `people_ops`: Employee master, payroll, attendance
- `talent_hub`: Recruitment, onboarding, performance
- `org_core`: Departments, roles, hierarchy, org chart

### Customer & Retail
- `customer_360`: CRM hub for customer master and contact history
- `lead_ops`: Leads, opportunities, pipeline
- `service_desk`: Support tickets and SLAs
- `loyalty_plus`: Points, rewards, and redemption logic
- `promo_core`: Campaigns, offers, promo management
- `retail_pos`: POS backend for transactions
- `checkout`: POS front-end integration
- `sync_hub`: POS sync and replication
- `retail_hub`: Real-time retail data sync between stores
- `price_core`: Pricing engine and discount management

### Supply Chain & Procurement
- `supply_core`: Supply chain planning, logistics, fulfillment
- `fleet_ops`: Fleet, route, and transport management
- `purchase_hub`: RFQs, tenders, purchase contracts

### Finance Extensions
- `pay_link`: Payment gateway integration (UPI, card, wallet)
- `tax_core`: GST/VAT computation, filing, compliance

### Integration & Infrastructure
- `event_core`: Internal event bus, async pub/sub messaging
- `service_bridge`: API gateway proxy, microservice routing
- `data_hub`: Central data warehouse and ETL service
- `admin_core`: System configuration, access control, roles

### Analytics & Governance
- `data_insights`: Analytics dashboards, metrics aggregation
- `compliance_core`: Policy management, audit logs, user actions
- `trace_core`: Transactional traceability, changelog system
- `forecast_x`: Predictive analytics, machine learning integration

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd arca-erp
   ```

2. **Build and run the containers:**
   ```bash
   docker-compose up --build
   ```

   The application will be available at `http://localhost:8000`.

### API Documentation

The Swagger API documentation is available at `http://localhost:8000/swagger/`.

### Health Check

A health check endpoint is available at `http://localhost:8000/health/`.

### Authentication

To authenticate, send a POST request to `/api/token/` with your username and password to obtain a JWT token. Include this token in the `Authorization` header of subsequent requests as a bearer token.

**Example:**
```
Authorization: Bearer <your-access-token>
```
