import os
import tempfile
from pathlib import Path

import boto3

from main import create_slide_from_scratch

BUCKET_NAME = os.environ["BUCKET_NAME"]
s3 = boto3.client("s3")


def scratch(event, context):

    with tempfile.TemporaryDirectory() as d:
        print(d)
        pptx_path = create_slide_from_scratch(Path(d))
        print(pptx_path)

        s3.upload_file(str(pptx_path), BUCKET_NAME, pptx_path.name)
        return s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": BUCKET_NAME, "Key": pptx_path.name},
            ExpiresIn=3600,
            HttpMethod="GET",
        )


if __name__ == "__main__":
    scratch({}, None)
