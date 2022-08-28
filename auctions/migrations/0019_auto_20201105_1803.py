
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_auction_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='status',
            new_name='closed',
        ),
    ]
