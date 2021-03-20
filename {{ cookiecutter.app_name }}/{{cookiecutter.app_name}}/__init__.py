from ephios.core.plugins import PluginConfig


class AppConfig(PluginConfig):
    name = "{{ cookiecutter.app_name }}"

    class EphiosPluginMeta:
        name = "{{ cookiecutter.app_name }}"
        author = "{{ cookiecutter.author }}"
        description = "{{ cookiecutter.description }}"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "{{ cookiecutter.app_name }}.{{ cookiecutter.app_name }}App"