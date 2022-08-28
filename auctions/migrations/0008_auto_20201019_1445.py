
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
