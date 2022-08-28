
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_auction_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
