## Installation:
To run this project you need python (version>=3.8) installed a long with scrapy framework.
Download and install python using https://www.python.org/downloads.

Install prerequisite libraries from requirements.txt file,
  Navigate to project directory and run:
```bash
pip install -r requirements.txt
```

## Developer tips:

Update user to login at line: 15, 16 in the spider:

```bash
username='xxxxxxxx'

password='xxxxxx'
```

Website will meet hcaptcha: Spider have to use google pass captcha api, replace it at link 17 in the spider:

```bash
api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

## How to run:

### Get the list code of NAICS and SIC

```bash
scrapy crawl siccode
```

Dataset siccode.csv export to ./Data/siccode.csv (*)

### Run to get dataset

Dataset make rom 10 pages / dataset

Dataset structure: Type_Code_No.csv

Ex: NAICS_54_1.csv:

Type: NAICS

Code: 54

No: 1 (Page from 1-10)

```bash
scrapy crawl kcls -a type=x -a code=y
```

x: NAICS (All NAICS), SIC (ALL SIC), PNAICS (Primary NAICS only), PSIC (Primary SIC only)

y: is code number of NAICS or SIC


Ex:

```bash
scrapy crawl kcls -a type=NAICS -a code=54
```

Dataset store in ./Data/xxx.csv

# NOTE

Website source maybe not response data while running. Just need re-run to get data continues

