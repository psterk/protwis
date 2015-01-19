from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api

from api.resources import GetProteinResource
from api.resources import GetSequenceResource
from api.resources import GetResidueResource

rest_api = Api(api_name='rest')
rest_api.register(GetProteinResource())
rest_api.register(GetSequenceResource())
rest_api.register(GetResidueResource())

# protein class specific resources
if settings.SITE_NAME == 'gpcr':
    from api_gpcr.resources import *
    
    rest_api.register(GetSpeciesResource())
elif settings.SITE_NAME == 'kinase':
    pass

urlpatterns = patterns('',
    url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(rest_api.urls)),
    url(r'^protein/', include('protein.urls')),
)