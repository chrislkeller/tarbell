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
    'project_name': 'state-of-bridges',

    # used for page title and open graph descriptions
    'title': 'Gauging the health of our Southern California&#39;s bridges',

    # static-projects directory that will house the project
    'project_category': 'applications',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/applications/health-of-our-bridges',

    # used for page meta and open graph descriptions
    'project_description': 'California has more than 24,000 bridges. Many are classified as "Structurally Deficient", "Functionally Obsolete" or "Fracture Critical". Use the filters below to learn more about bridges in Los Angeles, Orange, Riverside, San Bernardino and Ventura counties that carry the above designations, and see how they compare based on Caltrans and FHWA rating systems.',

    # used for page meta keywords
    'project_keywords': 'Los Angeles, Orange, Riverside, San Bernardino and Ventura, Caltrans, bridges, Structurally Deficient, Functionally Obsolete, Fracture Critical, Southern California, Federal Highway Administration',

    # used for page kicker
    'project_kicker': 'Transportation',

    # used for display headline
    'project_headline': 'Gauging the health of Southern California\'s bridges',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/sanden-totten">Sanden Totten</a>, Brian Frank &amp; <a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published June 21, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>California has more than 24,000 bridges. Many are classified as <a title="Click for Glossary of the Terms" href="javascript:void(0)" onclick="glossaryTerms();">"Structurally Deficient"</a>, <a title="Click for Glossary of the Terms" href="javascript:void(0)" onclick="glossaryTerms();">"Functionally Obsolete"</a> or <a title="Click for Glossary of the Terms" href="javascript:void(0)" onclick="glossaryTerms();">"Fracture Critical"</a>. These ominous-sounding terms are part of the <a href="http://www.fhwa.dot.gov/bridge/nbis.cfm" target="_blank">Federal Highway Administration\'s National Bridge Inspection Standards</a> and help to make up a bridge\'s <a title="Click for Glossary of the Terms" href="javascript:void(0)" onclick="glossaryTerms();">Sufficiency Rating</a>. California Department of Transportation officials say these classifications don\'t accurately reflect the overall health of a bridge; to get a more accurate reading of a bridge\'s health, <a href="http://onlinepubs.trb.org/onlinepubs/trnews/trnews215full.pdf" target="_blank">Caltrans</a> developed the <a title="Click for Glossary of the Terms" href="javascript:void(0)" onclick="glossaryTerms();">Bridge Health Index</a>. Use the filters below to learn more about bridges in Los Angeles, Orange, Riverside, San Bernardino and Ventura counties that carry the above designations and see how they compare based on Caltrans and FHWA rating systems.</p>',

    'project_image_url': '',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': 'http://www.scpr.org/news/2013/06/21/37842/how-safe-are-california-s-bridges/',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<strong>About the Data and Map: </strong>This map shows the more than 4,000 bridges in Los Angeles, Orange, Riverside, San Bernardino and Ventura counties that are owned and maintained by local agencies -- including cities and counties -- that have been rated by both the <a href="http://www.dot.ca.gov/hq/LocalPrograms/hbrr99/hbrr99a.htm">California Department of Transportation\'s Local Highway Bridge Program</a> and the <a href="http://www.fhwa.dot.gov/bridge/nbi.cfm">FHWA\'s National Bridge Inventory</a> as of May 2013. The location of bridges is based on Caltrans data and is approximate. To determine FHWA status of a particular bridge we used a structure identification number to find the same bridge in Caltrans data. Data showing state-owned bridges in Southern California could not immediately be provided, but will be added when available.',

    # set to True to enable
    'project_embed': 'False',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.dot.ca.gov/hq/LocalPrograms/hbrr99/hbrr99a.htm">California Department of Transportation\'s Local Highway Bridge Program</a>, <a href="http://www.fhwa.dot.gov/bridge/nbi.cfm">FHWA\'s National Bridge Inventory</a> &amp; <a href="http://www.ire.org/">Investigative Reporters and Editors</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="http://www.google.com/drive/apps.html#fusiontables">Fusion Tables</a>, <a href="http://derekeder.com">Derek Eder\'s</a> <a href="http://derekeder.com/searchable_map_template/">Searchable Map Template</a>, <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',
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