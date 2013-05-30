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
    'project_name': 'medicare-charges',

    # used for page title and open graph descriptions
    'title': 'Costs of healthcare in California | scpr.org',

    # static-projects directory that will house the project
    'project_category': '',

    # used for page sharing links
    'promoted_url': '',

    # used for page meta and open graph descriptions
    'project_description': '',

    # used for page meta keywords
    'project_keywords': '',

    # used for page kicker
    'project_kicker': 'Health',

    # used for display headline
    'project_headline': 'Costs of care in California: Federal government releases data comparing hospital bills',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/stephanie-oneill">Stephanie O\'Neill</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published May 10, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>The federal government <a href="http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/index.html">released 2011 data Wednesday</a> that it claims make it easier for patients to price shop for hospital services. There are wide variations in cost nationwide, and in southern California. But some experts say the information is irrelevant, as it has little bearing on actual costs.</p><p>Below, choose one of the 100 most common procedures found in the government data to see the average cost for the procedure in California, the lowest average cost and highest average cost. Then choose two hospitals to compare their costs.</p>',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': 'http://www.scpr.org/news/2013/05/08/37187/federal-government-releases-data-comparing-hospita/',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>About This: </strong>Choose one of the 100 most common procedures below to see the average cost for the procedure, the lowest average cost and highest average cost. Then choose two hospitals to compare.',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.treasurer.ca.gov/">Centers for Medicare &amp; Medicaid Services</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': '',
}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'medicare-charges'

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
# blueprint = Blueprint('medicare-charges', __name__)

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