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
    'project_name': 'monthly-jobs-added',

    # used for page title and open graph descriptions
    'title': 'Explaining the Monthly Jobs Report',

    # static-projects directory that will house the project
    'project_category': 'Business',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/interactives/monthly-jobs-added/',

    # used for page meta and open graph descriptions
    'project_description': 'On the first Friday of each month, the U.S. Bureau of Labor Statistics releases the Employment Situation Summary, commonly known as the monthly jobs report. The BLS also revises nonfarm payroll employment from the two prior months. The result is an "Initial" figure, a "Revised" figure and a "Final" figure. This chart and table attempt to illustrate the differences between the "Initial" figure and the "Final" figure.',

    # used for page meta keywords
    'project_keywords': 'Employment Situation Summary, U.S. Bureau of Labor Statistics',

    # used for page kicker
    'project_kicker': 'Business',

    # used for display headline
    'project_headline': 'Explaining the Monthly Jobs Report',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/wendy-lee" target="_blank">Wendy Lee</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller" target="_blank">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated Sept. 4, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>On the first Friday of each month, the <a href="http://www.bls.gov/">U.S. Bureau of Labor Statistics</a> releases the <a href="http://www.bls.gov/news.release/empsit.nr0.htm">Employment Situation Summary</a>, commonly known as the monthly jobs report.</p><p>The Employment Situation Summary details the level of "nonfarm payroll employment" over the previous month and the current unemployment rate. The BLS also details employment in various sectors and industries, such as professional and business services, health care and retail trade.</p><p>Each month the BLS also revises nonfarm payroll employment from the two prior months. The result is an "Initial" figure, a "Revised" figure and a "Final" figure. The chart and table below attempt to illustrate the differences between the "Initial" figure and the "Final" figure.</p><p>For example: In April the <a href="http://www.bls.gov/news.release/archives/empsit_05042012.htm">BLS intially reported</a> that the economy added 115,000 new jobs that month. The bureau decreased the figure to 77,000 new jobs in its <a href="http://www.bls.gov/news.release/archives/empsit_06012012.htm">June 2012 release</a> and finalized the figure at 68,000 new jobs in its <a href="http://www.bls.gov/news.release/archives/empsit_07062012.htm">July 2012 release</a>. The difference between the "Initial" estimate and the "Final" estimate was -47,000 jobs added.</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>Using the interactive:</strong> Hover over any part of the chart to see the number of jobs added for that month. Click on the points above the chart for information about contextual moments. Use the slider below the chart to zoom in on a specific section.</span>',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.bls.gov/">U.S. Bureau of Labor Statistics</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/jsoma/tabletop">tabletop.js</a>, <a href="http://www.highcharts.com/">highcharts.js</a>, <a href="http://handlebarsjs.com/">handlebars.js</a> &amp; <a href="http://twitter.github.com/bootstrap/">bootstrap</a>.',

    # set to True to enable
    'project_analytics': '',

    # set to True to enable
    'project_comments': '',

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