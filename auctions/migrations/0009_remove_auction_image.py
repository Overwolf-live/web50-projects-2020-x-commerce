
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201019_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='image',
        ),
    ]
