{
    'name': 'Odrer Tracking',
    'version': '17.0.1.0.0',
    'description': 'Odrer Tracking of All Products in Website',
    'category': 'Purchase/Order Tracking',
    'summary': 'Order Tracking in Website',
    'installable': True,
    'application': True,
    'depends': [
        'base',
        'stock',
        'website',
        ],
    'data': [
        'data/website_order_menu.xml',
        'views/order_views.xml',
        'views/order_list_views.xml',
        'views/order_details_views.xml',

    ]
}
