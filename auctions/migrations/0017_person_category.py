
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20201103_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='auctions.Category'),
        ),
    ]
