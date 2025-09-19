#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "galaxyuz_project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django import qilinmadi. Django o‘rnatilganini tekshiring."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
