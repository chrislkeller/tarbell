# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0An8W63YKWOsxdFZ4VTJIWngtY0VJWHJKM0dRUEpndVE',
}


"""
Set default context. These variables will be globally available to the template.
"""
DEFAULT_CONTEXT = {
    # project directory
    'project_name': 'la-county-jobs-by-sector',

    # used for page title and open graph descriptions
    'title': 'L.A. County health care jobs growing, construction & retail rebounding',

    # static-projects directory that will house the project
    'project_category': 'Business & Economy',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/interactives/monthly-jobs-added/',

    # used for page meta and open graph descriptions
    'project_description': 'On the first Friday of each month, the U.S. Bureau of Labor Statistics releases the Employment Situation Summary, commonly known as the monthly jobs report. The BLS also revises nonfarm payroll employment from the two prior months. The result is an "Initial" figure, a "Revised" figure and a "Final" figure. This chart and table attempt to illustrate the differences between the "Initial" figure and the "Final" figure.',

    # used for page meta keywords
    'project_keywords': 'Employment Situation Summary, U.S. Bureau of Labor Statistics',

    # used for page kicker
    'project_kicker': 'Business',

    # used for display headline
    'project_headline': 'Employment by sector: L.A. County health care jobs growing, construction & retail rebounding',

    # takes HTML. Will not render if blank
    'project_credits': 'Nuran Alteir, <a href="http://www.scpr.org/about/people/staff/wendy-lee" target="_blank">Wendy Lee</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller" target="_blank">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published Sept. 13, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>Five years after Lehman Brothers filed for bankruptcy protection, California\'s civilian unemployment rate is at 8.7 percent -- up from 7.9 percent in September 2008. According to Robert Kleinhenz, chief economist with the Los Angeles County Economic Development Corporation, it could take years before local job growth reaches the peak levels seen before what has now become known as the Great Recession.</p><p>But as a whole, the state is adding jobs at a faster pace than most of the nation -- second only to Utah -- according the UCLA Anderson Forecast.</p><p>The graph below shows the last 10 years of employment data from the <a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html">Califoria Employment Development Department</a>, arranged by sector. At a glance, it reveals which sectors provided the largest portion of jobs in the state\'s economy. When you click on each sector one-by-one, you can clearly see which industries were hardest hit by the recession (manufacturing, construction and retail), which have rebounded (arts and entertainment and food service), and which seem to have emerged unscathed (health care and social assistance).</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': 'http://www.scpr.org/blogs/economy',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>Using the interactive:</strong> The graph below shows the last 10 years of employment data by sector from the <a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html" target="_blank">California Employment Development Department</a>. At a glance it shows which sector accounts for the largest portion of jobs in the states economy over the last 10 years. Use the legend on the right to filter through the employment sectors one-by-one, to see how each was affected by the Great Recession. Use the slider across the bottom to zoom in and explore the data further.</span>',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html">Califoria Employment Development Department</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="http://code.shutterstock.com/rickshaw/">Rickshaw</a>, <a href="https://github.com/newsapps/tarbell-template">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">bootstrap</a>.',

    # set to True to enable
    'project_analytics': '',

    # set to True to enable
    'project_comments': 'False',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'monthly-jobs-added'

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
# blueprint = Blueprint('monthly-jobs-added', __name__)

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