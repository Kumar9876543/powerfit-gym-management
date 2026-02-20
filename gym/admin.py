from django.contrib import admin

# Register your models here.
from .models import Trainer

admin.site.register(Trainer)

from .models import MembershipPlan

admin.site.register(MembershipPlan)

from .models import Member

admin.site.register(Member)

from .models import Contact

admin.site.register(Contact)