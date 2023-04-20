
from django.apps import AppConfig
from django.urls import reverse
from cms.api import add_plugin, create_page
from cms.models import Placeholder
from djangocms_text_ckeditor.cms_plugins import TextPlugin

class TalkgptConfig(AppConfig):
    name = 'talkgpt'

    def ready(self):
        landing_page = create_page(
            'Landing Page',
            'talkgpt/landing.html',
            'en',
            parent=None,
            published=True,
            apphook='TextOnlyApp',
            apphook_namespace='talkgpt',
            in_navigation=True,
        )
        landing_placeholder = Placeholder.objects.create(
            slot='content',
            page=landing_page,
        )
        text_plugin = add_plugin(
            placeholder=landing_placeholder,
            plugin_type=TextPlugin,
            language='en',
            body='Welcome to our landing page!',
        )
        landing_page_url = reverse('pages-details-by-slug', args=['landing'])
        print(f'Landing page URL: {landing_page_url}')

        examples_page = create_page(
            'Examples Page',
            'talkgpt/examples.html',
            'en',
            parent=None,
            published=True,
            apphook='TextOnlyApp',
            apphook_namespace='talkgpt',
            in_navigation=True,
        )
        examples_placeholder = Placeholder.objects.create(
            slot='content',
            page=examples_page,
        )
        text_plugin = add_plugin(
            placeholder=examples_placeholder,
            plugin_type=TextPlugin,
            language='en',
            body='Here are some examples:',
        )
        examples_page_url = reverse('pages-details-by-slug', args=['examples'])
        print(f'Examples page URL: {examples_page_url}')

        talkgpt_page = create_page(
            'Talk GPT Page',
            'talkgpt/talkgpt.html',
            'en',
            parent=None,
            published=True,
            apphook='TextOnlyApp',
            apphook_namespace='talkgpt',
            in_navigation=True,
        )
        talkgpt_placeholder = Placeholder.objects.create(
            slot='content',
            page=talkgpt_page,
        )
        text_plugin = add_plugin(
            placeholder=talkgpt_placeholder,
            plugin_type=TextPlugin,
            language='en',
            body='Start talking to our GPT!',
        )
        talkgpt_page_url = reverse('pages-details-by-slug', args=['talkgpt'])
        print(f'Talk GPT page URL: {talkgpt_page_url}')


