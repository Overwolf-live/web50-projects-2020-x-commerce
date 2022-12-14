
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201014_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='category_for_the_auction', to='auctions.Category'),
        ),
    ]
