
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20201106_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='person',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_to_use', to='auctions.Person'),
        ),
    ]
