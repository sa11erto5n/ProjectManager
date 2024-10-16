from django.utils.translation import gettext_lazy as _

menu_items = [
    {
        "title": _("Main Menu"),  # This section has a title with translation
        "items": [
            # Home Page for all users
            {
                "title": _("Home Page"),  # Translatable title
                "icon": "fas fa-home",
                "url": "dash:home",
                "permission": "all",  
            },
            # Participants Menu only for admin
            {
                "title": _("Participants"),  # Translatable title
                "icon": "fas fa-fw fa-users",
                "url": "dash:users",
                "permission": "superuser",  # Only visible to superusers
            },
            # Prodcuts Menu Only For Admin
            {
                "title": _("Products"),  
                "icon": "fas fa-tags",
                "url": "dash:users",
                "permission": "superuser",  
            }
            ]

    },
    {
        # Only for seller
        "title": _("Other"),  # This section has a title with translation
        "items": [
            {
                "title": _("My Account"),
                "icon": "fas fa-fw fa-user",
                "url": "dash:profile",
                "permission": "contributer", 
            },
        ]
    }
]
