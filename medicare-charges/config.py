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
    'title': 'Costs of health care in California | scpr.org',

    # static-projects directory that will house the project
    'project_category': 'applications',

    # used for page sharing links
    'promoted_url': 'http://projects.scpr.org/static/applications/compare-medicare-charges',

    # used for page meta and open graph descriptions
    'project_description': 'KPCC has created this searchable database that will allow you to compare the costs of the 100 most frequently billed procedures paid under Medicare in 2011.',

    # used for page meta keywords
    'project_keywords': 'Centers for Medicare and Medicaid Services, health care, medicare, medicaid, hospital charges, common procedures',

    # used for page kicker
    'project_kicker': 'Health Care',

    # used for display headline
    'project_headline': 'How much does medical care cost? A searchable database of procedures in California billed to Medicare in 2011',

    # takes HTML. Will not render if blank
    'project_credits': '<a href="http://www.scpr.org/about/people/staff/chris-keller">Chris Keller</a>',

    # takes HTML. Will not render if blank
    'project_pubdate': 'Published May 30, 2013',

    # takes HTML. Will not render if blank
    'project_article_text': '<p>How much does a hospital charge Medicare when you undergo a given procedure? Depends on where you go. Say you want a new pacemaker: At <a href="http://articles.latimes.com/2013/may/17/business/la-fi-cedars-hospital-prices-20130517" target="_blank">Cedars-Sinai Medical Center</a>, the average bill in 2011 was about $140,496. But the U.C. San Diego Medical Center charged Medicare an average of $41,023 for the same procedure.</p><p>So how do you find out who is cheapest?</p><p>KPCC has created this searchable database that will allow you to compare the average charge for the 100 most frequently billed procedures paid under Medicare in 2011, which you can view by hospital or as a statewide average. It\'s based on <a href="http://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/index.html" target="_blank">data released in May</a> by the <a href="http://www.cms.gov/" target="_blank">Centers for Medicare and Medicaid Services</a> as a way to make it easier for patients to comparison shop for hospital services by price.</p><p>A caveat: The data shows a wide variation in average bills, but experts note that the <a href="http://www.washingtonpost.com/blogs/wonkblog/wp/2013/05/08/one-hospital-charges-8000-another-38000/" target="_blank">amounts billed have little bearing on what you actually pay</a>. You will see that difference in the amount shown as the "average reimbursement" for a procedure, which is the average amount actually paid to the hospital.</p><!--<p>The Medicare data contained the 100 most frequently billed discharges paid under Medicare -- some 7 million -- and were categorized under a system known as the Medicare Severity Diagnosis Related Group (MS-DRG). The MS-DRG is a series of more than 700 classifications meant to organize an illness or condition and accurately reflect the severity of an illness.</p><p>To help sort these discharges further, we\'ve grouped them by their "Major Diagnostic Category," <a href="http://health.utah.gov/opha/IBIShelp/codes/MDC.htm">which correspond to a single organ system or etiology and in general are associated with a particular medical specialty</a>.</p>--><p>Questions? <a href="mailto:scprweb@scpr.org?Subject=RE:%20How%20much%20does%20medical%20care%20cost%3F%20A%20searchable%20database%20of%20procedures%20by%20hospital%20in%20California">Write us</a> or leave a comment below.</p>',

    'project_image_url': 'http://a.scpr.org/i/0f6f30f30b5b5eca175ea4278eab88ba/40977-small.jpg',

    # hyperlink to the CMS story. Will not render if blank
    'project_readmore_link': '',

    # takes HTML. Will not render if blank
    'project_data_instructions': '<p><strong>To use this database</strong>: Let\'s say you wanted to compare the average statewide bill for treatment of kidney disease. To search the database, select "Kidney &amp; Urinary Tract" from the "Getting Started" menu, then choose from one of the diagnoses that match. Once you choose a category and a diagnosis, the data will show you charges and reimbursements in the state based on 1) overall average, 2) lowest and highest average charges and 3) difference. You can also compare the procedure between two hospitals to see how they compare on average charges and average reimbursement.</p>',

    # set to True to enable
    'project_embed': '',

    # HTML anchor tag(s) to the data source of the story. Will not render if blank
    'project_sources': '<a href="http://www.cms.gov/">Centers for Medicare &amp; Medicaid Services</a>.',

    # HTML anchor tag(s) to the tools used to build the project. Will not render if blank
    'project_open_source': 'Built using <a href="https://github.com/newsapps/tarbell-template" target="blank">Tarbell</a>, <a href="http://underscorejs.org/" target="blank">underscore.js</a> &amp; <a href="http://twitter.github.com/bootstrap/">Bootstrap</a>.',

    # set to True to enable
    'project_analytics': 'True',

    # set to True to enable
    'project_comments': 'True',
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