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
    '''
    EXAMPLES
    'project_name': 'project-inventory',
    'title': 'News &amp; Data Interactives',
    'project_category': 'test/keller',
    'promoted_url': 'http://projects.scpr.org/',
    'project_description': 'We\'ve collected our interactive maps, databases and charts so you can explore past projects by topic.',
    'project_keywords': 'KPCC, Southern California Public Radio, Crime & Public Safety, Culture, Economy & Money, Education, Environment & Science, General, Health, Politics, Seasonal, Transportation',
    'project_kicker': 'News &amp; Data Interactives',
    'project_headline': 'Explore KPCC\'s databases, maps and more',
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/kitty-felde">Kitty Felde</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',
    'project_pubdate': 'Updated May 13, 2013',
    'project_article_text': '<p>Beard hoodie, magna tumblr chillwave. Letterpress thundercats fixie consectetur accusamus cray gastropub bicycle rights. Adipisicing narwhal magna marfa. Fap photo booth cred, excepteur organic terry richardson vegan aesthetic narwhal. Food truck viral sint vinyl cred. Mustache aute consequat salvia, synth etsy irure +1. High life etsy ullamco, officia voluptate nihil brunch cillum nostrud photo booth duis Austin hella banjo.</p>',
    'project_readmore_link': 'http://www.lapdonline.org/assets/pdf/QDR%203rd%20Qtr.%202012%20FINAL%20MASTER.pdf',
    'project_data_instructions': '<strong>About This Map: </strong>Information on this map should never be used as a substitute for calling 811 two business days before digging. Southern California Gas Company (SoCalGas) is providing this map as a courtesy and for general information purposes only. It does not represent that the information contained herein is accurate for any particular purpose, and therefore disclaims all warranties, expressed or implied, including the warranty of fitness for a particular purpose. Independent verification from experts should be obtained prior to any specific use. Recipient accepts full responsibility for any consequences associated with use of this information.',
    'project_embed': 'False',
    'project_sources': '<a href="http://www.treasurer.ca.gov/">California State Treasurer\'s Office</a>',
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',
    'project_analytics': 'False',
    '''

    # project directory
    'project_name': 'state-of-bridges',

    # used for page title and open graph descriptions
    'title': 'A look at the health of California\'s bridges',

    # static-projects directory that will house the project
    'project_category': 'maps',

    # used for page sharing links
    'promoted_url': '',

    # used for page meta and open graph descriptions
    'project_description': '',

    # used for page meta keywords
    'project_keywords': '',

    # used for page kicker
    'project_kicker': 'Xxxxxxx',

    # used for display headline
    'project_headline': 'Xxxxx xxxxxx xxxxx xxxxx',

    # takes HTML. Will not render if blank
    'project_credits': '',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated May 13, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>Beard hoodie, magna tumblr chillwave. Letterpress thundercats fixie consectetur accusamus cray gastropub bicycle rights. Adipisicing narwhal magna marfa. Fap photo booth cred, excepteur organic terry richardson vegan aesthetic narwhal. Food truck viral sint vinyl cred. Mustache aute consequat salvia, synth etsy irure +1. High life etsy ullamco, officia voluptate nihil brunch cillum nostrud photo booth duis Austin hella banjo.</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>About This Map: </strong>Beard hoodie, magna tumblr chillwave. Letterpress thundercats fixie consectetur accusamus cray gastropub bicycle rights. Adipisicing narwhal magna marfa. Fap photo booth cred, excepteur organic terry richardson vegan aesthetic narwhal. Food truck viral sint vinyl cred. Mustache aute consequat salvia, synth etsy irure +1. High life etsy ullamco, officia voluptate nihil brunch cillum nostrud photo booth duis Austin hella banjo.',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': '',

    # set to True to enable
    'project_comments': '',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'state-of-bridges'

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
# blueprint = Blueprint('state-of-bridges', __name__)

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