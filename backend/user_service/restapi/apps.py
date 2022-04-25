from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "restapi"
    def ready(self):
        # подключаем сигналы
        import restapi.app.signals