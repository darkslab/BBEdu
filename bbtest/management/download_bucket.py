from django.conf import settings
from google.cloud.storage import Client
from google.oauth2.service_account import Credentials

from bbtest.models import TestParagraph


def storage_bucket():
    return Client(
        project=settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"].get("project_id"),
        credentials=Credentials.from_service_account_info(settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"]),
    ).bucket(settings.SECRETS["GOOGLE_STORAGE_BUCKET"])

bucket = storage_bucket()

obj_list = TestParagraph.objects.filter(
    paragraph_class = "ImageParagraph"
    # paragraph_class = "SplitText"
)

export = ""

for i, obj in enumerate(obj_list):
    # meta = json.loads(obj.meta_data)
    meta = obj.meta_data
    export += "{},{},{}\n".format(obj.pk, meta["asset_uuid"], meta["asset_object_name"])
    line = "{}/{}: {},{},{}".format(i + 1, len(obj_list), obj.pk, meta["asset_uuid"], meta["asset_object_name"])
    print(line, " "*50, end="\r")
    blob = bucket.blob(meta["asset_object_name"])
    local_path = "assets/{}.jpg".format(meta["asset_uuid"])
    blob.download_to_filename(local_path)
    

with open("export.assets.iac.csv", "w") as f:
    f.write(export)