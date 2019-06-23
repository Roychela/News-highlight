import urllib.request,json
from .models import NewsSource, NewsArticles

# Getting api key
api_key = None
# Getting the news sources url
base_url = None
#Getting the news articles url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']
def get_news_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)

        news_sources_results = None

        if get_news_sources_response['sources']:
            news_sources_results_list = get_news_sources_response['sources']
            news_sources_results = process_results(news_sources_results_list)
    return news_sources_results

def process_results(news_sources_list):
    '''
    Function that processes the json results
    '''
    news_sources_results = []

    for source in news_sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        if url:
            news_source_object = NewsSource(id,name,description,url,category,country)
            news_sources_results.append(news_source_object)
    
    return news_sources_results