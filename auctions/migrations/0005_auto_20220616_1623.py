from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_comment_comment_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='auctions',
            new_name='auction',
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
