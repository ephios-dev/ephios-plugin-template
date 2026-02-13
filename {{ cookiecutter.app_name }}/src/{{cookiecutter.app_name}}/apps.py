from ephios.core.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "{{ cookiecutter.app_name }}"

    class EphiosPluginMeta:
        name = "{{ cookiecutter.app_name }}"
        author = "{{ cookiecutter.author_name }}"
        description = "{{ cookiecutter.description }}"
        visible = True
        force_enabled = False

    def ready(self):
        from . import signals  # NOQA
