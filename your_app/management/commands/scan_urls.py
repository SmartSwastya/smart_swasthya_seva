import os
import django
from django.core.management.base import BaseCommand
from django.urls import get_resolver
from django.conf import settings
from django.template import TemplateDoesNotExist


class Command(BaseCommand):
    help = 'Scan all URLs and validate views and templates'

    def handle(self, *args, **kwargs):
        django.setup()
        resolver = get_resolver()
        url_patterns = resolver.url_patterns

        missing_templates = []
        missing_views = []

        # Iterate through all url patterns
        for pattern in url_patterns:
            if hasattr(pattern, 'url_patterns'):  # Check if it's an 'include' (nested urls)
                for subpattern in pattern.url_patterns:
                    self._check_url_and_template(subpattern, missing_templates, missing_views)
            else:
                self._check_url_and_template(pattern, missing_templates, missing_views)

        # Print summary of missing templates and views
        self._print_report(missing_templates, missing_views)

    def _check_url_and_template(self, pattern, missing_templates, missing_views):
        try:
            # Check if view exists
            view = pattern.callback
            view_name = view.__name__
            # Check if view function exists in views.py (Simple method, improves detection)
            if not self._view_exists(view_name):
                missing_views.append(view_name)

            # Check if corresponding template exists
            template_name = f'{view_name}.html'  # Assumes the template name matches the view
            if not self._template_exists(template_name):
                missing_templates.append(template_name)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error processing URL: {str(e)}"))

    def _view_exists(self, view_name):
        try:
            # Try importing the view and check if it exists
            view_module = __import__('your_app.views', fromlist=[view_name])
            return hasattr(view_module, view_name)
        except ImportError:
            return False

    def _template_exists(self, template_name):
        try:
            # Try loading the template
            template_path = os.path.join(settings.TEMPLATES[0]['DIRS'][0], template_name)
            return os.path.exists(template_path)
        except TemplateDoesNotExist:
            return False

    def _print_report(self, missing_templates, missing_views):
        if missing_views:
            self.stdout.write(self.style.ERROR(f"Missing Views: {', '.join(missing_views)}"))
        else:
            self.stdout.write(self.style.SUCCESS("All views are accounted for!"))

        if missing_templates:
            self.stdout.write(self.style.ERROR(f"Missing Templates: {', '.join(missing_templates)}"))
        else:
            self.stdout.write(self.style.SUCCESS("All templates are accounted for!"))
