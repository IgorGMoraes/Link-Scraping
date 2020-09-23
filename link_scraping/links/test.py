from django.test import TestCase
from .models import ParentLink
from .services import format_url, link_to_previous_directory, is_href_valid
from .forms import LinkForm

class Test(TestCase):
    def test_save_parent_link(self):
        parent_link = ParentLink.objects.create(id=None, url='https://www.test.com')
        pl_from_db = ParentLink.objects.get(url='https://www.test.com')
        self.assertEqual(pl_from_db.id, parent_link.id)

    def test_format_url(self):
        url = format_url('test.com')
        self.assertTrue(url.startswith('https://'))

    def test_link_to_previous_directory(self):
        link = link_to_previous_directory('https://test.com/directory/', '../test')
        self.assertEqual(link, 'https://test.com/test')

    def test_is_hrefs_valid(self):
        hrefs = ['#', '']
        self.assertEqual(0, len(list(filter(lambda href: is_href_valid(href), hrefs))))

    def test_form(self):
        form_full = LinkForm(data={'url': 'https://test.com'})
        form_short = LinkForm(data={'url': format_url('test.com')})
        form_invalid = LinkForm(data={'url': 'test'})
        self.assertTrue(form_full.is_valid())
        self.assertTrue(form_short.is_valid())
        self.assertFalse(form_invalid.is_valid())
        