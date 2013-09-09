# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0AqQRnXPMXTfhdE45czJScGpOQ2MwSXlBTkYzQ0ZNSUE',
}


"""
Set default context. These variables will be globally available to the template.
"""

DEFAULT_CONTEXT = {
    # project directory
    'project_name': 'finding-peace-and-quiet',

    # used for page title and open graph descriptions
    'title': 'Where do you find peace and quiet in LA?',

    # static-projects directory that will house the project
    'project_category': 'map',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/maps/finding-peace-and-quiet',

    # used for page meta and open graph descriptions
    'project_description': 'Nearly 10 million people call Los Angeles County home. More than 40 million pay LA a visit each year. With so many people and only so much space, it can be tough to find peace and quiet. This map shows places our listeners go to relax and get away from it all.',

    # used for page meta keywords
    'project_keywords': 'los angeles, public insight network, relaxation, peace and quiet',

    # used for page kicker
    'project_kicker': 'Life &amp; Culture',

    # used for display headline
    'project_headline': 'Where do you find peace and quiet in LA?',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/jose-martinez">Jos&#233; Martinez</a>, <a href="http://www.scpr.org/about/people/staff/ashley-alvarado">Ashley Alvarado</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated May 27, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>It can be hard to find tranquility in South Los Angeles, home to many of L.A. County\'s most densely populated neighborhoods. It can be loud and finding a quiet space to think can be tough. This lack of tranquility can affect a person\'s quality of life. Sometimes, even their health. This problem is not unique to South L.A. as millions call Southern California home. That\'s why KPCC wants to know: Where do you go to get away from it all?</p><p>Is there a favorite park or hiking trail? Maybe you prefer an empty museum or quiet garden. Tell KPCC and help us map the best places to escape.</p><div class="content-partners"><p class="pij">This was informed by KPCC listeners. <a href="http://www.scpr.org/network/">Become a source.</a></p></div>',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': 'http://www.scpr.org/blogs/southla/2013/05/27/13711/where-do-you-go-to-find-peace-and-quiet-in-south-l/',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a>, <a href="https://github.com/mahnunchik/markerclustererplus">MarkerClustererPlus</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',
}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'finding-peace-and-quiet'

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
# blueprint = Blueprint('finding-peace-and-quiet', __name__)

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