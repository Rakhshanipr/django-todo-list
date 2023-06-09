import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Please turn of yout dns"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
