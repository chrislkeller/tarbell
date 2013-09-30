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
    'title': 'L.A. County health care jobs growing, construction and retail rebounding',

    # static-projects directory that will house the project
    'project_category': 'Business & Economy',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/charts/la-county-jobs-by-sector',

    # used for page meta and open graph descriptions
    'project_description': 'The graph below shows the last 10 years of Los Angeles County employment data from the California Employment Development Department arranged by economic sector, revealing which were hardest hit by the recession.',

    # used for page meta keywords
    'project_keywords': 'Los Angeles County, Los Angeles County employment data, California Employment Development Department',

    # used for page kicker
    'project_kicker': 'Business & Economy',

    # used for display headline
    'project_headline': 'Employment by sector: L.A. County health care jobs growing, construction and retail rebounding',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="https://twitter.com/whatnuransaid" target="_blank">Nuran Alteir</a>, <a href="http://www.scpr.org/about/people/staff/wendy-lee" target="_blank">Wendy Lee</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller" target="_blank">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published Sept. 13, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>Five years after Lehman Brothers filed for bankruptcy protection, <a href="http://www.scpr.org/blogs/economy/2013/08/16/14528/la-county-unemployment-rate-nearly-10-percent-in-j/" target="_blank">Los Angeles County\'s unemployment rate</a> remains at 9.9 percent, 2.5 percentage points higher than the national rate. According to Robert Kleinhenz, chief economist with the <a href="http://laedc.org/" target="_blank">Los Angeles County Economic Development Corporation</a>, it could take years before local job growth reaches the peak levels seen before what has now become known as the Great Recession.</p><p>In 2007, before the recession, Los Angeles County had 4.12 million non-farm jobs, according to the state\'s Employment Development Department. Last year, the number of non-farm jobs in the county was 3.86 million.</p><p>"The pace of job growth has been really slow," Kleinhenz said. "Recovery has been slow in part because the financial crisis has hampered activity all the way around."</p><p>The graph below shows the last 10 years of Los Angeles County employment data from the <a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html">California Employment Development Department</a>, arranged by sector. At a glance, it reveals which sectors provided the largest portion of jobs. When each sector is viewed one-by-one, you can clearly see which industries were hardest hit by the recession (manufacturing, construction and retail), which have rebounded (arts and entertainment and food service), and which seem to have emerged unscathed (health care and social assistance).</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': 'http://www.scpr.org/blogs/economy/2013/09/13/14716/l-a-s-economy-still-recouping-losses-five-years-af/',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>Using the interactive:</strong> The graph below shows the last 10 years of Los Angeles County employment data by sector from the <a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html" target="_blank">California Employment Development Department</a>. At a glance, it reveals which sectors provided the largest portion of jobs. Use the legend menu to see how each was affected by the Great Recession.',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.labormarketinfo.edd.ca.gov/LMID/Employment_by_Industry_Data.html">Califoria Employment Development Department</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="http://code.shutterstock.com/rickshaw/">Rickshaw</a>, <a href="https://github.com/newsapps/tarbell-template">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',

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