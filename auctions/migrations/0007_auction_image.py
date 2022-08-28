
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
