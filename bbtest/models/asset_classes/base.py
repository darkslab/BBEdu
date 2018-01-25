class Asset:
    def __init__(self, asset, storage_bucket, **kwargs):
        self._asset = asset
        self._storage_bucket = storage_bucket

    def asset(self):
        return self._asset

    def storage_bucket(self):
        return self._storage_bucket
