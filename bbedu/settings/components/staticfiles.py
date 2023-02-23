from bbedu.settings.components.common import DEBUG

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/var/www/html/static/"
STATICFILES_STORAGE = "bbtest.pipeline.storage.ManifestPipelineStorage"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "pipeline.finders.CachedFileFinder",
    "pipeline.finders.PipelineFinder",
]



from bbtest.pipeline_js import (
    BASE0_SOURCE_FILENAMES as BASE0_SOURCE_FILENAMES_JS,
    BASE1_SOURCE_FILENAMES as BASE1_SOURCE_FILENAMES_JS,
    BASE3_SOURCE_FILENAMES as BASE3_SOURCE_FILENAMES_JS,
    BASE0_NKT_SOURCE_FILENAMES as BASE0_NKT_SOURCE_FILENAMES_JS
)
if not DEBUG:
    from bbtest.pipeline_js import BASE2_PRODUCTION_SOURCE_FILENAMES as BASE2_SOURCE_FILENAMES_JS
else:
    from bbtest.pipeline_js import BASE2_DEVELOPMENT_SOURCE_FILENAMES as BASE2_SOURCE_FILENAMES_JS
from bbtest.pipeline_css import (
    BASE0_SOURCE_FILENAMES as BASE0_SOURCE_FILENAMES_CSS,
    BASE1_SOURCE_FILENAMES as BASE1_SOURCE_FILENAMES_CSS,
    BASE0_NKT_SOURCE_FILENAMES as BASE0_NKT_SOURCE_FILENAMES_CSS
)

PIPELINE = {
    "PIPELINE_COLLECTOR_ENABLED": False,
    "DISABLE_WRAPPER": True,
    "SHOW_ERRORS_INLINE": False,
    "JAVASCRIPT": {
        "base0": {
            "source_filenames": BASE0_SOURCE_FILENAMES_JS,
            "output_filename": "js/base0.js",
            "extra_context": {
                "defer": True,
            },
        },
        "base1": {
            "source_filenames": BASE1_SOURCE_FILENAMES_JS,
            "output_filename": "js/base1.js",
            "extra_context": {
                "defer": True,
            },
        },
        "base2": {
            "source_filenames": BASE2_SOURCE_FILENAMES_JS,
            "output_filename": "js/base2.js",
            "extra_context": {
                "defer": True,
            },
        },
        "base3": {
            "source_filenames": BASE3_SOURCE_FILENAMES_JS,
            "output_filename": "js/base3.js",
            "extra_context": {
                "defer": True,
            },
        },
        "base0_nkt": {
            "source_filenames": BASE0_NKT_SOURCE_FILENAMES_JS,
            "output_filename": "js/base0-nkt.js",
            "extra_context": {
                "defer": True,
            },
        },
    },
    "STYLESHEETS": {
        "base0": {
            "source_filenames": BASE0_SOURCE_FILENAMES_CSS,
            "output_filename": "css/base0.css",
        },
        "base1": {
            "source_filenames": BASE1_SOURCE_FILENAMES_CSS,
            "output_filename": "css/base1.css",
        },
        "base0_nkt": {
            "source_filenames": BASE0_NKT_SOURCE_FILENAMES_CSS,
            "output_filename": "css/base0-nkt.css",
        },
    },
}