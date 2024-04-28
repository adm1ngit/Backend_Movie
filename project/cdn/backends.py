from storages.backends.s3boto3 import S3Boto3Storage

class StaticRootS3Boto3Storages(S3Boto3Storage):
    location = 'static'

class MediaRootS3Boto3Storages(S3Boto3Storage):
    location = 'media'