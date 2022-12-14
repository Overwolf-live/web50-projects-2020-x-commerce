
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20201014_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(default='Other', on_delete=django.db.models.deletion.CASCADE, related_name='category_for_the_auction', to='auctions.Category'),
        ),
    ]
