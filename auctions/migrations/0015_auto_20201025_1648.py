
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201025_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
