# MonkeyPoxAPI

MonkeyPoxAPI a simple package that allows users to develop applications using data scraped from CDC's official MonkeyPox tracker

## Installation

```bash
pip install monkeypoxapi
```

## Usage
```python
from monkeypoxapi import uscases

# returns the number of Monkey Pox cases in California
uscases.numcases("California")

# returns the total number of cases in the US
uscases.total()

# returns the date this data was recorded
uscases.date()

```




## Saving csv as a fileobject to an S3 bucket

```python
import boto3
from monkeypoxapi import uscases

s3 = boto3.resource('s3')
key = 'KEY'
bucket = 'BUCKET'

fileobj = uscases.csv()

s3.upload_fileobj(fileobj, bucket, key)


```

## License
[MIT](https://choosealicense.com/licenses/mit/)


## How this works

Data is being webscraped from CDC's official website on monkeypox data.

-HTTP GET requests to endpoints

-Requests are parsed into respective objects to allow for indexing

-JSON and CSV files are returned as io objects
