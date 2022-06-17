from django.contrib import admin
from assets.models import AssetCategory, SubAssetCategory

# Register your models here.

@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'created', 'modified')

@admin.register(SubAssetCategory)
class SubAssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('asset_category', 'name', 'alias', 'created', 'modified')

