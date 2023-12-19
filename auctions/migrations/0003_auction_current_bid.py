from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20220612_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='current_bid',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
