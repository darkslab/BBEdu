from bbtest.jobs.upload import image_paragraph_processor


def upload_processor(upload, asset):
    return {
        "asset_adopter": "image_paragraph_asset_adopter",
        "job": image_paragraph_processor,
    }
