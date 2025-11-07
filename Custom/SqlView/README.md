# TFCS Customisation Module

This module extends the Odoo `sale.order` model with additional custom fields to meet TFCS business requirements.

## Features

The module adds the following custom fields to Sales Orders:

### Customer Information
- **Customer PO Number**: Store customer's purchase order number for reference
- **Customer Tier**: Customer tier (Bronze, Silver, Gold, Platinum, Diamond) affecting pricing/discounts

### Order Processing
- **Priority Level**: Priority indicator (Low, Medium, High, Urgent) for order processing
- **Approval Status**: Status field for managerial approval (Pending, Approved, Rejected, Not Required)
- **Order Source**: Source of the order (Online, Retail Store, Phone, Email, Walk-in, Referral, Other)
- **Referral Source**: How customer found the business (Social Media, Referral, Advertisement, etc.)

### Payment & Promotions
- **Custom Payment Terms**: Custom terms specific to the sale order
- **Promotional Code**: Applied discount or promotional code
- **Special Tax Exemption Code**: Tax exemption details specific to the order

### Delivery & Packaging
- **Delivery Instructions**: Detailed instructions for order delivery
- **Preferred Delivery Time**: Customer's preferred delivery window
- **Shipping Account Number**: Customer's account number for specific courier services
- **Custom Packaging Requirements**: Notes or codes for specific packaging needs

### Sales & Gift Features
- **Sales Representative Contact**: Contact details of assigned sales representative
- **Gift Message**: Message to include if order is marked as a gift
- **Is Gift Order**: Automatically computed field based on gift message presence

## Installation

1. Place this module in your Odoo addons directory
2. Update the addons list in Odoo
3. Install the "TFCS Customisation" module

## Usage

After installation, the new fields will appear in the Sales Order form view:

- **TFCS Custom Fields** section: Customer PO, Tier, Priority, Approval Status, Order Source, etc.
- **Delivery & Packaging** section: Delivery instructions, preferred time, packaging requirements
- **Sales Representative** section: Sales rep contact details
- **Payment Terms** field: Custom payment terms

The fields are also available in:
- Sales Order list view (key fields shown as optional columns)
- Sales Order search view (with additional filters for High Priority, Pending Approval, Gift Orders)

## Technical Details

- **Model**: Extends `sale.order`
- **Dependencies**: `sale`, `sales_team`, `account`
- **Views**: Form, Tree, and Search view extensions
- **Security**: Inherits existing sale.order permissions

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| customer_po_number | Char | Customer's purchase order number |
| custom_payment_terms | Text | Custom payment terms for this order |
| delivery_instructions | Text | Detailed delivery instructions |
| preferred_delivery_time | Selection | Preferred delivery time window |
| sales_rep_contact | Text | Sales representative contact details |
| promotional_code | Char | Applied promotional code |
| customer_tier | Selection | Customer tier (Bronze to Diamond) |
| priority_level | Selection | Order priority (Low to Urgent) |
| approval_status | Selection | Managerial approval status |
| order_source | Selection | Source of the order |
| custom_packaging_requirements | Text | Special packaging requirements |
| shipping_account_number | Char | Courier account number |
| referral_source | Selection | How customer found business |
| special_tax_exemption_code | Char | Tax exemption code |
| gift_message | Text | Gift message for the order |
| is_gift | Boolean | Computed field for gift orders | 