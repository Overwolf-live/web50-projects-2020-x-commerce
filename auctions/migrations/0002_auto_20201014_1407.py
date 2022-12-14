
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalwatchlist',
            name='auctions',
            field=models.ManyToManyField(blank=True, related_name='auctions_in_the_watchlist', to='auctions.Auction'),
        ),
    ]
