from django.utils.translation import get_language


RESULT_MAIN_DESCRIPTION_TEXTS = {}

def result_main_description_text(section_id):
    if section_id not in RESULT_MAIN_DESCRIPTION_TEXTS:
        return [ "" ]
    return RESULT_MAIN_DESCRIPTION_TEXTS[section_id][get_language()]


RESULT_TOPIC_DESCRIPTION_TEXTS = {}

def result_topic_description_text(topic_id):
    if topic_id not in RESULT_TOPIC_DESCRIPTION_TEXTS:
        return [ "" ]
    return RESULT_TOPIC_DESCRIPTION_TEXTS[topic_id][get_language()]
