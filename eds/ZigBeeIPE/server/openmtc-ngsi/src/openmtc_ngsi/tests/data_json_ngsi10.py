
updateContextRequestJSON = """{
  "updateContextRequest": {
    "contextElementList": {
      "contextElement": [
        {
          "entityId": {
            "id": "urn:username:sergio",
            "type": "urn:username"
          },
          "contextAttributeList": {
            "contextAttribute": [
              {
                "name": "cell",
                "metadata": {
                  "contextMetadata": [
                    {
                      "name": "Timestamp",
                      "value": "2012-06-13T15:04:52+01:00"
                    },
                    {
                      "name": "Expires",
                      "value": "2012-06-13T17:05:52+01:00"
                    },
                    {
                      "name": "Source",
                      "value": "TeamLife_1.13"
                    }
                  ]
                },
                "contextValue": {
                  "cgi": "222-1-61101-7066"
                }
              }
            ]
          }
        }
      ]
    },
    "updateAction": "UPDATE"
  }
 }
"""

queryContextRequestJSON = """{
  "queryContextRequest": {
    "entityIdList": {
      "entityId": [
        {
          "type": "urn:username",
          "id": "urn:username:sergio"
        }
      ]
    },
    "attributeList": {
      "attribute": [
        "cell",
        "cell1"
      ]
    },
    "restriction": {
      "attributeExpression": "//contextValue[starts-with(cgi,'222')]"
    }
  }
 }
"""

