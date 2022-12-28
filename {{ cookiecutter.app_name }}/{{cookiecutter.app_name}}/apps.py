from ephios.core.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "{{ cookiecutter.app_name }}"

    class EphiosPluginMeta:
        name = "{{ cookiecutter.app_name }}"
        author = "{{ cookiecutter.author }}"
        description = "{{ cookiecutter.description }}"

    def ready(self):
        from . import signals  # NOQA
