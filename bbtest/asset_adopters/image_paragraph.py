from bbtest.models.upload import expiring_url


def asset_adopter(asset, **kwargs):
    object_name = asset.asset_object().object_name()
    return {
        "asset_uuid": asset.uuid,
        "asset_object_name": object_name,
        "asset_url": expiring_url(object_name),
    }
