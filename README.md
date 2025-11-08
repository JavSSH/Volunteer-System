# Volunteer Management System

A web-based platform connecting Corporate Social Responsibility (CSR) representatives with Persons-in-Need (PIN) for volunteer opportunities and community service matching.

## Overview

This system facilitates connections between individuals seeking assistance and corporate volunteers looking to give back to their communities. The platform supports multiple user roles and streamlines the volunteer matching process.

## Features

### User Roles
- **User Admin:** Manage user accounts and profiles
- **Platform Manager:** Oversee categories, generate reports, and manage system operations
- **CSR Representative:** Browse opportunities, create shortlists, and track volunteer history
- **Person-in-Need (PIN):** Create assistance requests and track matches

### Core Functionality
- User account management with role-based access control
- Category-based volunteer opportunity organization (100+ categories)
- Request creation and tracking system
- Shortlist management for CSR representatives
- Volunteer service history tracking
- Daily, weekly, and monthly reporting
- Real-time opportunity view and shortlist counters

## Technology Stack

- **Backend:** Python, Flask
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JavaScript, Jinja2 templates
- **Architecture:** BCE (Boundary-Entity-Controller)

## Test Data

The system includes pre-populated dummy data for testing and demonstration purposes.

### Sample Data Included

**Categories (100 volunteer opportunity types)**
- Located in: `database/mock-data/category.sql`
- Contains 100 diverse volunteer categories including Elderly Care, Food Distribution, Youth Programs, etc.
- All categories include names, descriptions, and active/inactive status flags

**User Accounts (100 distinct user accounts)**
- Located in: `database/mock-data/user.sql`
- Pre-configured test accounts for all user roles (see Default User Credentials section)
- Includes sample data for names, emails, addresses, phone numbers, and account statuses

**User Profiles (4 distinct user profiles/types)**
- Located in: `database/mock-data/userprofile.sql`
- Links users to their respective roles (User Admin, Platform Manager, CSR Rep, PIN)
- Includes profile descriptions and role assignments

