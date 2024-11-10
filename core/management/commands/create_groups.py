from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import User
from inventory.models import InventoryItem, Product, QuantitativeUnit
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Create user groups and set permissions for Administrator, Moderator, and Contributor'

    content_type = ContentType.objects.get_for_model(InventoryItem)
    inventory_item_permission = Permission.objects.filter(content_type=content_type)
    print([perm.codename for perm in inventory_item_permission])
    
    def handle(self, *args, **kwargs):
        groups_permissions = {
            'Administrator': ['add_user', 'change_user', 'delete_user', 'view_user', 'add_inventoryitem', 'change_inventoryitem', 'delete_inventoryitem', 'view_inventoryitem', 'add_product', 'change_product', 'delete_product', 'view_product', 'add_recipe', 'change_recipe', 'delete_recipe', 'view_recipe', 'add_quantitativeunit', 'change_quantitativeunit', 'delete_quantitativeunit', 'view_quantitativeunit'],
            'Moderator': ['view_user', 'add_inventoryitem', 'change_inventoryitem', 'delete_inventoryitem', 'view_inventoryitem', 'add_product', 'change_product', 'delete_product', 'view_product', 'add_recipe', 'change_recipe', 'delete_recipe', 'view_recipe', 'add_quantitativeunit', 'change_quantitativeunit', 'delete_quantitativeunit', 'view_quantitativeunit'],
            'Contributor': ['add_inventoryitem', 'change_inventoryitem', 'delete_inventoryitem', 'view_inventoryitem', 'add_product', 'change_product', 'delete_product', 'view_product', 'add_recipe', 'change_recipe', 'delete_recipe', 'view_recipe', 'add_quantitativeunit', 'change_quantitativeunit', 'delete_quantitativeunit', 'view_quantitativeunit']
        }

        model_content_types = {
            'user': ContentType.objects.get_for_model(User),
            'inventoryitem': ContentType.objects.get_for_model(InventoryItem),
            'product': ContentType.objects.get_for_model(Product),
            'quantitativeunit': ContentType.objects.get_for_model(QuantitativeUnit),
            'recipe': ContentType.objects.get_for_model(Recipe),
        }

        for group_name, permissions_list in groups_permissions.items():
            # Create the group
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Group "{group_name}" created')
            else:
                self.stdout.write(f'Group "{group_name}" already exists')

            # Set permissions
            for perm_codename in permissions_list:
                # Determine model and content type
                model_name = perm_codename.split('_')[1]
                content_type = model_content_types.get(model_name)

                if not content_type:
                    self.stdout.write(f'No content type found for model "{model_name}"')
                    continue

                try:
                    # Fetch the permission based on the codename and content type
                    permission = Permission.objects.get(codename=perm_codename, content_type=content_type)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(f'Permission "{perm_codename}" not found for group "{group_name}"')

            self.stdout.write(f'Permissions set for group "{group_name}"')

        self.stdout.write(self.style.SUCCESS('Groups and permissions setup complete.'))