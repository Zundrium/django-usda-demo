from django.conf.urls import patterns, include, url
from rest_framework import routers
from django_usda.modelviewsets import FoodViewSet, FoodGroupViewSet, FoodLanguaLFactorViewSet, LanguaLFactorViewSet, NutrientDataViewSet, NutrientViewSet, SourceViewSet, DerivationViewSet, WeightViewSet, FootnoteViewSet, DataLinkViewSet, DataSourceViewSet, FoodInfoViewSet
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()

router.register(r'foods', 				FoodViewSet)
router.register(r'foodgroups', 			FoodGroupViewSet)
router.register(r'foodlangualfactors', 	FoodLanguaLFactorViewSet)
router.register(r'langualfactors', 		LanguaLFactorViewSet)
router.register(r'nutrientdatas', 		NutrientDataViewSet)
router.register(r'nutrients', 			NutrientViewSet)
router.register(r'sources', 			SourceViewSet)
router.register(r'derivations', 		DerivationViewSet)
router.register(r'weights', 			WeightViewSet)
router.register(r'footnotes', 			FootnoteViewSet)
router.register(r'datalinks', 			DataLinkViewSet)
router.register(r'datasources', 		DataSourceViewSet)
router.register(r'foodinfo', 			FoodInfoViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^demo/', 'demo.views.index'),
)