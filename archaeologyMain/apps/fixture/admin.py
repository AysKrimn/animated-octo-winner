from django.contrib import admin
from .models import *


admin.site.register(Fixture)
admin.site.register(FixtureGainType)
admin.site.register(CustomTaxRate)

