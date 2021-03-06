.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================================
Unique Partner per Event, Combined With Event Sales
===================================================

This module avoids duplicates when you confirm several sale orders for a same
customer and event.

In case you sell different ticket types, the duplicate is however allowed, but
not the combination of event + partner + ticket.

Usage
=====

To use this module, you need to:

#. Go to *Marketing > Events > Create*.
#. Enable *Forbid duplicates*.
#. Try to create 2 registrations for the same partner and ticket in this event.
#. You cannot.
#. Go to *Sales > Sales > Sales Orders*.
#. Create a new sale order for customer "A".
#. Add a new line with:
    - Product: Choose a event ticket product.
    - Event: Choose an event for that product.
    - Ticket: Choose a ticket type if you want.
    - Quantity: 1.
#. Confirm the sale order.
#. Enter the event and check it has 1 registration with 1 seat.
#. Go back to the sale order, duplicate it and confirm it.
#. Go back to the event again, it has 1 registration with 2 seats.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/199/8.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/event/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/OCA/
event/issues/new?body=module:%20
event_sale_registration_partner_unique%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Rafael Blasco <rafabn@antiun.com>
* Jairo Llopis <yajo.sk8@gmail.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
