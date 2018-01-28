from bbtest.models.upload import expiring_url


def asset_adopter(asset, **kwargs):
    return {
        "asset_uuid": asset.uuid,
        "asset_url": expiring_url(asset.asset_object().object_name()),
    }
