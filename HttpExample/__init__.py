import logging

import azure.functions as func
import pandas as pd
import requests
from azure.search.documents import SearchClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    def test_pandas():
        df = pd.DataFrame(
            {
                "Name": [
                    "Braund, Mr. Owen Harris",
                    "Allen, Mr. William Henry",
                    "Bonnell, Miss. Elizabeth",
                ],
                "Age": [22, 35, 58],
                "Sex": ["male", "male", "female"],
            }
        )
        logging.info(df.describe())

    def test_azure_search():
        print(SearchClient.__dir__)


    def test_requests():
        r = requests.post("http://httpbin.org/post")
        print("Testing POST...")
        print("POST: Success!") if r.status_code == 200 else print("POST: Failure")
        
        r = requests.get("http://httpbin.org/get")
        print("Testing GET...")
        print("GET: Success!") if r.status_code == 200 else print("GET: Failure")
    
    test_pandas()
    test_azure_search()
    test_requests()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
