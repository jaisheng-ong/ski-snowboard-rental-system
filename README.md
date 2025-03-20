# Ski and Snowboard Rental System

A comprehensive solution for winter sports equipment rental management

## Project Overview

The Ski and Snowboard Rental System is a Python-based application designed to manage rental operations
for a winter sports equipment shop. The system handles customer information, inventory tracking, 
rental calculations, and financial reporting in an efficient and user-friendly manner.

## Key Features

- **Customer Management**: Track customer details including contact information and rental history
- **Inventory Control**: Monitor available skis and snowboards with real-time updates
- **Flexible Rental Options**: Support for hourly, daily, and weekly rental periods
- **Discount Management**: Apply coupon codes and family discounts automatically

## System Architecture

The system is built using object-oriented programming principles in Python, featuring two main classes:

### cCustomer Class

Manages all customer-related information and operations:
- Personal information (name, phone)
- Rental details (quantities, rate category, duration)
- Discount information (coupon codes)
- Date tracking (rental date, expected return)

### cShop Class

Handles shop operations and business logic:
- Inventory management
- Pricing calculations
- Discount application
- Rental cost computation
- Financial reporting

## User Interface

The system provides a simple console-based interface with four main operations:

1. **New Customer Rental** - Process new equipment rentals
2. **Rental Return** - Handle equipment returns and final billing
3. **Show Inventory** - Display current stock levels
4. **End of Day** - Generate daily financial reports

## Key Functionalities

### Rental Pricing

The system automatically calculates the most cost-effective rate for customers based on rental duration:
- Hourly rates for short-term rentals
- Daily rates for medium-term rentals
- Weekly rates for extended rentals

### Discount System

Two types of discounts are available:
- **Coupon Discounts** - 10% off with valid coupon codes that has 6 character long and ends with 'BBP'
- **Family Discounts** - 25% off for rentals of 3-5 items, with special handling for 6+ items

### Inventory Management

The system maintains real-time inventory tracking:
- Automatic updates when equipment is rented or returned
- Prevents renting unavailable equipment
- Provides visibility into current inventory levels

## Technical Implementation

The system implements several technical features:
- Data validation for all user inputs
- Exception handling to prevent system crashes
- Encapsulation through getters/setters
- List-based data structures for customer management
- Date and time handling for rental duration calculations

## Future Enhancements

Potential improvements for future versions:
- Database integration for persistent data storage
- Graphical user interface for improved user experience
- Customer loyalty program implementation
- Equipment maintenance tracking
- Online reservation system

---
