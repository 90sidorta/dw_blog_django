#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dw_blog_django.settings.base import ENVIRONMENT


def main():
    """Run administrative tasks."""
    if ENVIRONMENT == "DEVELOPMENT":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "dw_blog_django.settings.development"
        )
    elif ENVIRONMENT == "PRODUCTION":
        os.environ.setdefault(
            "DJANGO_SETTINGS_MODULE", "dw_blog_django.settings.production"
        )
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dw_blog_django.settings.base")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
