from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "auth_users"
    def ready(self):
        # подключаем сигналы
        import auth_users.app.signals