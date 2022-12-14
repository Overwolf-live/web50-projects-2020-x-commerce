
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201019_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='last_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_bid_for_the_auction', to='auctions.Bid'),
        ),
    ]
