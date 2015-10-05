from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.conf import settings

from wpadmin.utils import get_admin_site_name
from wpadmin.menu import items
from wpadmin.menu.menus import Menu

class TopMenu(Menu):

    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)

        self.children += [
            items.MenuItem(
                title='nomi',
                icon='fa-connectdevelop',
                css_styles='font-size: 1.5em;',
            ),
        ]


class LeftMenu(Menu):
    def init_with_context(self, context):

        admin_site_name = get_admin_site_name(context)
        user = context.get('request').user

        self.children += [
            items.ModelList(
                    title=_('Utilizadores e grupos'),
                    icon='fa-user',
                    models=('django.contrib.auth.*', 'myusers.*'),
            ),
            items.MenuItem(
                    title=_('Profiles'),
                    url=reverse('admin:core_profile_changelist'),
                    enabled=user.has_perm('core.change_profile'),
                    icon='fa-users'
            ),

            items.MenuItem(
                    title=_('Attributes'),
                    url=reverse('admin:core_attribute_changelist'),
                    enabled=user.has_perm('core.change_attribute'),
                    icon='fa-paperclip'
            ),

        ]