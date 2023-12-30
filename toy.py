from secedgar import filings, FilingType

# 10Q filings for Apple (ticker "aapl")
my_filings = filings(cik_lookup="aapl",
                     filing_type=FilingType.FILING_10Q,
                     user_agent="David Yoon (junhoyoon00@gmail.com)")
my_filings.save('./')