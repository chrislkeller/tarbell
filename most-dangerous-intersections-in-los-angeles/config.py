# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0AuXre6OvBEihdHQ1QlQwU1lVNHRRZGVQa25SQ3IxRmc',
}


"""
Set default context. These variables will be globally available to the template.
"""
DEFAULT_CONTEXT = {
    # project directory
    'project_name': 'most-dangerous-intersections-in-los-angeles',

    # used for page title and open graph descriptions
    'title': 'Dangerous intersections in Los Angeles',

    # static-projects directory that will house the project
    'project_category': 'Public Safety',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/maps/pedestrian-safety/',

    # used for page meta and open graph descriptions
    'project_description': 'The city of Los Angeles is taking steps to make 53 dangerous intersections safer for pedestrians. As a first step, the city will install "continental crosswalks" that provide increased visibility for pedestrians. This map shows which intersections that the city considers dangerous and those that you the reader consider dangerous.',

    # used for page meta keywords
    'project_keywords': 'Los Angeles, pedestrians, bicyclists, intersections, accidents, dangerous',

    # used for page kicker
    'project_kicker': 'Public Safety',

    # used for display headline
    'project_headline': 'Tell Us: Where are the most dangerous intersections in Los Angeles',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/chris-keller" target="_blank">Chris Keller</a> &amp; <a href="http://www.scpr.org/about/people/staff/kim-bui" target="_blank">Kim Bui</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated Sept. 17, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>The city of Los Angeles is taking steps to make <a href="http://blogdowntown.com/2012/12/7093-new-zebra-crossings-aim-to-make-53-la-intersection" target="blank">53 dangerous intersections</a> safer for pedestrians and cyclists. As a first step, the city will install "continental crosswalks" - aka "zebra crossings" - that provide increased visibility for pedestrians.</p><p>This map shows which intersections (marked in green) that the city considers dangerous. But are they the same as the intersections (marked in red) that <a href="http://www.scpr.org/news/2012/10/02/34497/help-us-map-los-angeles-most-dangerous-areas-bicyc/" target="_blank">YOU have designated as hazardous&#63;</a></p><p>See how they match up - or don\'t - in our interactive map.</p><p>Are there others&#63; Let us know what intersections and other locations you believe are the most dangerous for pedestrians and cyclists. Simply click the button below and tell us your experience.</p>',

    'project_image_url': 'http://a.scpr.org/i/a731eaaab6e7b5c316b30b3c5bc3466b/19204-full.jpg',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': 'Reader submissions &amp; <a href="http://www.treasurer.ca.gov/">Los Angeles Mayor\'s Office</a>',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="http://www.google.com/drive/apps.html#fusiontables">Fusion Tables</a>, <a href="http://derekeder.com">Derek Eder\'s</a> <a href="http://derekeder.com/searchable_map_template/">Searchable Map Template</a>, <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'False',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'metropolitan-water-district-rental-properties'

"""
Don't render to static HTML.
"""
# DONT_PUBLISH = False

"""
Don't create JSON for project (default: true)
"""
# CREATE_JSON = False

"""
Uncomment the following lines to provide this configuration file as a Flask
blueprint.
"""
# from flask import Blueprint
# blueprint = Blueprint('metropolitan-water-district-rental-properties', __name__)

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