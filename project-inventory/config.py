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
    'project_name': 'project-inventory',

    # used for page title and open graph descriptions
    'title': 'News &amp; Data Interactives',

    # static-projects directory that will house the project
    'project_category': 'http://projects.scpr.org/',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/',

    # used for page meta and open graph descriptions
    'project_description': 'We\'ve collected our interactive maps, databases and charts so you can explore past projects by topic.',

    # used for page meta keywords
    'project_keywords': 'KPCC, Southern California Public Radio, Crime & Public Safety, Culture, Economy & Money, Education, Environment & Science, General, Health, Politics, Seasonal, Transportation',

    # used for page kicker
    'project_kicker': 'News &amp; Data Interactives',

    # used for display headline
    'project_headline': 'Explore KPCC\'s databases, maps and more',

    # takes HTML. Will not render if blank
    'project_credits': '',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated November 27, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>We\'ve collected our interactive maps, databases and charts so you can explore past projects by topic.</p>',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # Default is False. Set to True to enable
    'project_embed': 'False',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # Default is False. Set to True to enable
    'project_analytics': 'True',
}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
URL_ROOT = 'project-inventory'

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
# blueprint = Blueprint('project-inventory', __name__)

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