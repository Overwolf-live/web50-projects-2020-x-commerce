
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_delete_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='img_url',
        ),
    ]
