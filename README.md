# rest-api-tests

This project provides a basic framework for a REST API testing with pytest.

Resources used
For the APIs to be tested, an ecommerce online store is created on Woocommerce (open-source e-commerce plugin for WordPress).
https://woocommerce.com/?utm_source=google&utm_medium=cpc&utm_campaign=acquisition_search_brand_row&utm_content=woocommerce&gclid=Cj0KCQiA8t2eBhDeARIsAAVEga0uck9tkh0l4qZ9LZTz9VjW0MjfkpG1JL7i0gl0MUyrSx7OLjrvcwsaAuhHEALw_wcB

API documentation is available in the link below
https://woocommerce.github.io/woocommerce-rest-api-docs/?shell#introduction

The project is intended to show some working examples for commonly used pytest freatures like marks, fixtures, paramatrize, etc

All tests call the API and verify the response with DB. The database is set up locally.
