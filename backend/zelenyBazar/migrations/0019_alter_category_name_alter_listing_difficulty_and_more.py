# Generated by Django 4.1.3 on 2022-12-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zelenyBazar', '0018_alter_category_name_alter_listing_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Kaktusy', 'Cacti'), ('Palmy', 'Palms'), ('Ovocné stromy', 'Fruit Trees'), ('Okrasné stromy', 'Decorative Trees'), ('Okrasné rostliny', 'Decorative Plants'), ('Ostatní', 'Others'), ('Bylinky', 'Herbs'), ('Exotické rostliny', 'Exotic Plants'), ('Skalničky', 'Rocky Plants'), ('Užitkové rostliny', 'Utility Plants'), ('Okrasné keře', 'Decorative Bushes')], max_length=30),
        ),
        migrations.AlterField(
            model_name='listing',
            name='difficulty',
            field=models.CharField(choices=[('Lehká', 'Easy'), ('Střední', 'Medium'), ('Težká', 'Hard'), ('Nezadáno', 'Unknown')], default='Nezadáno', max_length=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='plantType',
            field=models.CharField(choices=[('Řízek', 'Cut'), ('Semínka', 'Seeds'), ('Živá rostlina', 'Alive Plant'), ('Ostatní', 'Other'), ('Nezadáno', 'Unknown')], default='Nezadáno', max_length=20),
        ),
    ]