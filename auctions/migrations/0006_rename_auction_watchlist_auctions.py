from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20220616_1623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='auction',
            new_name='auctions',
        ),
    ]
