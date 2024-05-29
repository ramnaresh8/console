# Generated by Django 4.2.7 on 2024-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_alter_providercredentials_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentsync',
            name='service',
            field=models.CharField(choices=[('cloudflare_pages', 'Cloudflare Pages'), ('aws_secrets_manager', 'AWS Secrets Manager'), ('github_actions', 'GitHub Actions'), ('hashicorp_vault', 'Hashicorp Vault'), ('hashicorp_nomad', 'Hashicorp Nomad')], max_length=50),
        ),
    ]