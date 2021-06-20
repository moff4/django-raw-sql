#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def run_wsgi():
    # use wsgi from STD lib
    from wsgiref.simple_server import make_server
    from proj1.wsgi import application

    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")

        # Serve until process is killed
        httpd.serve_forever()


if __name__ == '__main__':
    # main()
    run_wsgi()
