
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_person_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
