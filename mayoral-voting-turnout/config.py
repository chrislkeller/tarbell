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
    'project_name': 'mayoral-voting-turnout',

    # used for page title and open graph descriptions
    'title': 'Charting voter turnout for mayoral elections',

    # static-projects directory that will house the project
    'project_category': 'interactives/la-mayors-race',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/interactives/la-mayors-race/mayoral-voting-turnout',

    # used for page meta and open graph descriptions
    'project_description': 'This chart shows voter turnout for mayoral elections in LA dating back to 1913, based upon L.A. Times Data Desk data.',

    # used for page meta keywords
    'project_keywords': 'Los Angeles, elections, mayoral election, L.A. mayor\'s race',

    # used for page kicker
    'project_kicker': 'L.A. Mayor\'s Race',

    # used for display headline
    'project_headline': 'Charting voter turnout for mayoral elections',

    # takes HTML. Will not render if blank
    'project_credits': '',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated May 16, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>In advance of Los Angeles\' 2013 mayoral election Tuesday, the L.A. Times <a href="http://www.latimes.com/news/local/la-me-mayor-turnout-20130515-big-dto,0,1068221.htmlstory">analyzed voter turnout</a> dating back to 1913 and found that L.A.\'s Election Day malaise stretches back decades.</p><p>The March 2013 primary contest brought the city its <a href="http://spreadsheets.latimes.com/100-years-l-mayoral-turnout/">second lowest turnout in 100 years</a> -- 20.80 percent -- according to the data. March\'s low turnout was surpassed only by Antonio Villaraigosa\'s primary win in 2009, which brought out just 17.90 percent of the voting public.</p><p>The highest turnout—75.95 percent—came in 1969 when Sam Yorty defeated Tom Bradley.</p><p>The chart below shows voter turnout dating back to 1913 and is based upon data the <a href="http://datadesk.latimes.com/">L.A. Times Data Desk</a> made publicly <a href="http://spreadsheets.latimes.com/api/100-years-l-mayoral-turnout.csv">available for download</a>.</p>',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # set to True to enable
    'project_embed': 'False',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://spreadsheets.latimes.com/100-years-l-mayoral-turnout/" target="_blank">Data made available by the L.A. Times Data Desk</a>',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a>, <a href="http://www.highcharts.com/" target="blank">higcharts.js</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'False',
}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
URL_ROOT = 'mayoral-voting-turnout'

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
# blueprint = Blueprint('mayoral-voting-turnout', __name__)

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