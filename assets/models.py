from django.db import models

# Create your models here.
class AssetCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubAssetCategory(models.Model):
    asset_category = models.ForeignKey(AssetCategory, related_name="sub_categories", on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return f"{self.name} - ({self.asset_category.name})"

