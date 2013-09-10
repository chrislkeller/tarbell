# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0An8W63YKWOsxdC1DbjM0MVFUelFXcUFCY2xZWGtSZGc',
}


"""
Set default context. These variables will be globally available to the template.
"""
DEFAULT_CONTEXT = {
    # project directory
    'project_name': 'farm-to-you',

    # used for page title and open graph descriptions
    'title': 'How Wal-Mart distributes strawberries to 200 stores',

    # static-projects directory that will house the project
    'project_category': 'interactive',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/interactives/from-farm-to-you/',

    # used for page meta and open graph descriptions
    'project_description': 'Wal-Mart Stores Inc. tells KPCC how it transports strawberries grown at a small Santa Maria farm to 200 stores in California and Nevada.',

    # used for page meta keywords
    'project_keywords': 'Wal-Mart Stores Inc, California, Better Produce, strawberries',

    # used for page kicker
    'project_kicker': 'Business &amp; Agriculture',

    # used for display headline
    'project_headline': 'How Wal-Mart distributes strawberries to 200 stores',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/wendy-lee">Wendy Lee</a>, <a href="http://www.scpr.org/about/people/staff/grant-slater">Grant Slater</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published June 11, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>Wal-Mart Stores Inc. plans to grow the sales of locally-grown produce nationwide and is buying crops directly from farmers. The retailer tells KPCC how it transports strawberries grown at a small Santa Maria farm to 200 stores in California and Nevada.</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'farm-to-you'

"""
Don't render to static HTML.
"""
# DONT_PUBLISH = False

"""
Don't create JSON for project (default: true)
"""
CREATE_JSON = False

"""
Uncomment the following lines to provide this configuration file as a Flask
blueprint.
"""
# from flask import Blueprint
# blueprint = Blueprint('farm-to-you', __name__)

"""
Example use of flask blueprint to add a template filter.
"""
# @blueprint.app_template_filter('example_filter')
# def example_filter(text):
#    return text + ' ...suffix.'

"""
Load secrets. Don't change this unless you know what you're doing.
"""
import imp
import os
def get_secrets():
    """ Return a secrets module """
    root = os.path.dirname(os.path.abspath(__file__))
    return imp.find_module('secrets', [root])

secrets = imp.load_module('secrets', *get_secrets())

if hasattr(secrets, 'GOOGLE_AUTH'):
    GOOGLE_DOC.update(secrets.GOOGLE_AUTH)