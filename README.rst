Credit Limit Control Module
===========================

Description
-----------

The Credit Limit Control module enhances the purchase order workflow in Odoo by introducing credit limit controls for vendors. It allows setting a global credit limit in the settings and individual credit limits for partners/contacts. Additionally, it adds two new stages to the purchase order workflow: First Approval and Second Approval. The module ensures that purchase orders are routed through these stages based on the comparison between the vendor's credit limit and the global credit limit set in the settings.

Installation
------------

1. Download the module from the repository.
2. Add the module to your Odoo addons directory.
3. Install the module from the Odoo Apps menu.
4. Restart the Odoo server if necessary.

Configuration
-------------

1. Navigate to Settings > Purchase > Configuration.
2. Find the "Credit Limit Control" section.
3. Set the desired global credit limit in the "Credit Limit" field.

Usage
-----

1. Navigate to the Contacts module and open a partner/contact record.
2. Set the individual credit limit for the partner in the "Partner Credit Limit" field.
3. Navigate to the Purchase module and create a new purchase order.
4. Select a vendor from the partner dropdown.
5. Upon confirming the purchase order, the module checks if the selected vendor's credit limit exceeds the global credit limit set in the settings.
6. If the vendor's credit limit exceeds the global limit, the purchase order moves to the "First Approval" stage.
7. Upon approval at the "First Approval" stage, the purchase order proceeds to the "Second Approval" stage.
8. Once approved at the "Second Approval" stage, the purchase order is confirmed and processed further.

Notes
-----

- If the vendor's credit limit is below or equal to the global credit limit, the purchase order proceeds directly to confirmation without requiring approval stages.
- Administrators can configure additional settings and permissions related to credit limit control as needed.
- Ensure that users are appropriately trained on the new workflow to effectively utilize the credit limit control features.

Contributing
------------

Contributions to this module are welcome. Please submit any bug reports, feature requests, or pull requests to the repository.

License
-------

This module is licensed under the GPL-3 license. See the LICENSE file for more details.
