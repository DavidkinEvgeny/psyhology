# Generated by Django 4.0.5 on 2022-06-22 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityInSocialNetworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_activity_in_social_networks', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityOnJnlineTradingPlatforms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_activity_on_online_trading_platforms', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_age', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AnonymityOnTheInternet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_anonymity_on_the_internet', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LevelOfAwareness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_level_of_awareness', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MessageBoardActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message_board_activity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UseOfReactionEnhancers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_use_of_reaction_enhancers', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_work', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MyQuesyion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('result', models.TextField(verbose_name='Результат')),
                ('activity_in_social_networks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.activityinsocialnetworks', verbose_name='Активность в соц. сетях')),
                ('activity_on_online_trading_platforms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.activityonjnlinetradingplatforms', verbose_name='Активность на торговых интернет-платформах')),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.age', verbose_name='Возраст')),
                ('anonymity_on_the_internet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.anonymityontheinternet', verbose_name='Анонимности в Интернете')),
                ('level_of_awareness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.levelofawareness', verbose_name='Уровень осведомленности')),
                ('message_board_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.messageboardactivity', verbose_name='Активность доски объявлений')),
                ('use_of_reaction_enhancers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.useofreactionenhancers', verbose_name='Применение усилителей реакции')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.work', verbose_name='Социальный статус(работа)')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
