from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auction_current_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='message',
        ),
    ]
