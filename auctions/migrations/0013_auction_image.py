
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201019_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
