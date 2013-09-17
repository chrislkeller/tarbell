# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0Aq8qwSArzKP9dElWSnU1bjd3Rkpna0EwYVQ1dnprcEE',
}

"""
Set default context. These variables will be globally available to the template.
"""
DEFAULT_CONTEXT = {
    # project directory
    'project_name': 'statehouse-vetoes',

    # used for page title and open graph descriptions
    'title': 'California governors and use of veto since 1967',

    # static-projects directory that will house the project
    'project_category': 'politics',

    # used for page sharing links
    'promoted_url': '',

    # used for page meta and open graph descriptions
    'project_description': '',

    # used for page meta keywords
    'project_keywords': '',

    # used for page kicker
    'project_kicker': 'Politics',

    # used for display headline
    'project_headline': 'California governors and their use of the veto since 1967',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published Sept. 9, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p><a href="http://gov.ca.gov/home.php">Gov. Jerry Brown</a> vetoed about 12 percent of the bills passed by the state legislature in 2012, the second lowest veto percentage since 1996 when then-Governor Pete Wilson vetoed just under 9 percent of the bills that came across his desk, according to <a href="http://projects.scpr.org/static/documents/?doc=784913-governors-vetoes-2012" target="blank">research</a> by the <a href="http://sgf.senate.ca.gov/" target="blank">Senate Committee on Governance &amp; Finance</a>.<p>On the whole over his 10-plus years in office -- from 1975 to 1982 and from 2011 to 2012 -- Brown has signed 12,744 bills, which is the most since 1967. He also has the fewest number of vetoes over that time period: 773.</p><p>Brown\'s use of the veto is much lower than that of his predecessor Gov. Arnold Schwarzenegger, who on average vetoed about 26 percent of the bills presented to him by state legislators between 2004 and 2010. It\'s also higher than Brown\'s previous stint as governor, when he vetoed about 4.6 percent of the bills passed by the legislature.</p><p>Here are some additional tidbits based on the committee\'s <a href="http://projects.scpr.org/static/documents/?doc=784913-governors-vetoes-2012" target="blank">research</a>:</p><ul><li>Brown\'s 2012 percentage is less than the average percentage since 1967 (13 percent).</li><li>In 1982, Brown vetoed just 30 bills of the 1,674 he considered, setting the record for the lowest number of vetoes.</li><li>The five years with the fewest chaptered bills have all been since 2007.</li><li>Schwarzenegger vetoed over three times as many bills in his seven years (1,970) as Brown did in his first eight years (528), and twice as many as Reagan did in eight years (843).</li></ul>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>About This Chart</strong>: The chart below shows the percentage of bills vetoed by California\'s governors dating back to 1967 and is based on <a href="http://projects.scpr.org/static/documents/?doc=784913-governors-vetoes-2012" target="blank">research</a> from the <a href="http://sgf.senate.ca.gov/">Senate Committee on Governance &amp; Finance</a>. The percentages were calculated based on bills passed by the legislature in regular session and includes bills that a governor allowed to become law without a signature. The 2010 figure includes four bills signed by Lt. Gov. Abel Maldonado while serving as Acting Governor. The number of bills are based on published statutes for each year and information from the Office of the Governor. The numbers of vetoes are based on records kept by the governor\'s office.',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://projects.scpr.org/static/documents/?doc=784913-governors-vetoes-2012">Senate Committee on Governance &amp; Finance</a>',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a>, <a href="http://twitter.github.com/bootstrap/">Bootstrap</a> &amp; <a href="http://www.highcharts.com/" target="blank">Highcharts</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'statehouse-vetoes'

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
# blueprint = Blueprint('statehouse-vetoes', __name__)

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