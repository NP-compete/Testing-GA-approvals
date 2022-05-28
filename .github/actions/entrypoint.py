#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

import os
import sys
import json
import boto3
import requests
from botocore.exceptions import ClientError

# For Testing
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

# Inputs
OPERATION = sys.argv[1]
ENVIRONMENT = sys.argv[0]

# Store in secrets
AUTH_TOKEN = os.environ.get("GITHUB_TOKEN")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
CODEPIPELINE_NAME = os.environ.get("CODEPIPELINE_NAME")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_PROFILE = os.environ.get("AWS_PROFILE")


session = requests.Session()
headers = {
    "Authorization": "token %s" % AUTH_TOKEN,
    "Accept": "application/vnd.github.v3+json",
}

# Create an issue
def create_issue(title, body=None):
    issue_url = "https://api.github.com/repos/%s/issues" % (REPOSITORY)
    issue = {"title": title, "body": body, "labels": ["deployment-requested"]}
    r = session.post(issue_url, data=json.dumps(issue), headers=headers)
    if r.status_code == 201:
        print(
            "Successfully Created Issue #{0}: {1}".format(
                r.json().get("number"), r.json().get("title")
            )
        )
    else:
        print("Could not create Issue")
        print("Response:", r.content)


# Comment on issue
def create_comment(ISSUE_NUMBER, COMMENT):
    comment_url = "https://api.github.com/repos/%s/issues/%s/comments" % (
        REPOSITORY,
        ISSUE_NUMBER,
    )
    comment = {"body": COMMENT}
    r = session.post(comment_url, data=json.dumps(comment), headers=headers)
    if r.status_code == 201:
        print("Successfully Commented on Issue #{0}".format(ISSUE_NUMBER))
    else:
        print("Could not comment on Issue")
        print("Response:", r.content)


# Trigger CodePipeline
def trigger_codepipeline(CODEPIPELINE_NAME, AWS_REGION, AWS_PROFILE="default"):
    session = boto3.session.Session(profile_name=AWS_PROFILE)
    client = session.client(
        service_name="codepipeline",
        region_name=AWS_REGION,
    )
    try:
        client.start_pipeline_execution(name=CODEPIPELINE_NAME)
        print("Successfully triggered CodePipeline")
    except ClientError as e:
        print(e.response["Error"]["Message"])
        print("Could not trigger CodePipeline")


# Close Issue
def close_issue(ISSUE_NUMBER):
    close_issue_url = "https://api.github.com/repos/%s/issues/%s" % (
        REPOSITORY,
        ISSUE_NUMBER,
    )
    request_body = {"state": "closed"}
    r = session.patch(close_issue_url, data=json.dumps(request_body), headers=headers)
    if r.status_code == 200:
        print("Successfully Closed Issue #{0}".format(ISSUE_NUMBER))
    else:
        print("Could not close Issue")
        print("Response:", r.content)



def main():
    match OPERATION:
        case "create_comment":
            create_comment(issue_number, comment)
        case "create_issue":
            create_issue(
                "Deployment Approval Required for %s" % ENVIRONMENT,
                "Comment 'Approved' to approve this deployment",
            )
        case "trigger_codepipeline":
            trigger_codepipeline(CODEPIPELINE_NAME, AWS_REGION, AWS_PROFILE)
        case "close_issue":
            close_issue(issue_number)
        case _:
            print("Code not found")


if __name__ == "__main__":
    main()