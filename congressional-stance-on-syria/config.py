# coding: utf-8

"""
Google doc configuration. If not provided, no Google doc will be used.
"""

GOOGLE_DOC = {
    'key': '0Aq8qwSArzKP9dHN0WDllWENuV0pMcWZwRHhmal9zOXc',
}


"""
Set default context. These variables will be globally available to the template.
"""
DEFAULT_CONTEXT = {

    # project directory
    'project_name': 'congressional-stance-on-syria',

    # used for page title and open graph descriptions
    'title': 'Syria: Where do your members of Congress stand?',

    # static-projects directory that will house the project
    'project_category': 'Politics',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/charts/congressional-stance-on-syria/',

    # used for page meta and open graph descriptions
    'project_description': 'Here\'s where California\'s members of Congress stand on Syria & whether the United States should take military action.',

    # used for page meta keywords
    'project_keywords': 'California congressional delegation, immigration reform, Karen Bass, Xavier Becerra, Ami Bera, Barbara Boxer, Julia Brownley, Ken Calvert, John Campbell, Lois Capps, Tony Cardenas, Judy Chu, Paul Cook, Jim Costa, Susan Davis, Jeff Denham, Anna Eshoo, Sam Farr, Dianne Feinstein, John Garamendi, Janice Hahn, Mike Honda, Jared Huffman, Duncan Hunter, Darrell Issa, Doug LaMalfa, Barbara Lee, Zoe Lofgren, Alan Lowenthal, Doris Matsui, Kevin McCarthy, Tom McClintock, Buck McKeon, Jerry McNerney, Gary Miller, George Miller, Grace Napolitano, Gloria Negrete McLeod, Devin Nunes, Nancy Pelosi, Scott Peters, Dana Rohrabacher, Lucille Roybal-Allard, Ed Royce, Raul Ruiz, Linda Sanchez, Loretta Sanchez, Adam Schiff, Brad Sherman, Jackie Speier, Eric Swalwell, Mark Takano, Mike Thompson, David Valadao, Juan Vargas, Maxine Waters, Henry Waxman',

    # used for page kicker
    'project_kicker': 'Politics',

    # used for display headline
    'project_headline': 'Syria: Where do your members of Congress stand?',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/kitty-felde">Kitty Felde</a>, Nuran Alteir, Monica Luhar, <a href="http://www.scpr.org/about/people/staff/brian-frank">Brian Frank</a> &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Updated Sept. 9, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': 'Members of Congress return Sept. 9 for closed door security briefings on Syria. Many lawmakers - including several members of the California delegation - have weighed in on whether the U.S. should take military action against Syria following allegations of a chemical weapons attack by the Assad regime against civilians. The debate has been anything but partisan. Democrats and Republicans are equally divided over how the U.S. should respond. Their stances have also become more nuanced, with legislators divided over multiple options: stay out of Syria\'s business, increase diplomatic pressure, or carry out a limited strike. We reached out to the California delegation on Capitol Hill to find out how they\'re leaning on the question that lies at the heart of this debate: <strong>Are you for or against some form of military action in Syria?</strong>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '',

    # set to True to enable
    'project_embed': 'False',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': 'Interviews with the California Congressional Delegation, public statements, and other news outlets.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',

}

"""
Root URL project will appear at (e.g. http://mydomain.tld/)
"""
# URL_ROOT = 'congressional-stance-on-syria'

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
# blueprint = Blueprint('congressional-stance-on-syria', __name__)

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