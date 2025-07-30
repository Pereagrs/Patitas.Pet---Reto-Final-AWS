{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PermitirSubidaDesdeLambda",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::020961627277:role/LabRole"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::patitas-imagenes/*"
        }
    ]
}