# rest-api-tests

This project provides a basic framework for a REST API testing with pytest.

The APIs that are used for testing, points to a ecommerce store that is build on Woocommerce(open-source e-commerce plugin for WordPress).
https://woocommerce.com/?utm_source=google&utm_medium=cpc&utm_campaign=acquisition_search_brand_row&utm_content=woocommerce&gclid=Cj0KCQiA8t2eBhDeARIsAAVEga0uck9tkh0l4qZ9LZTz9VjW0MjfkpG1JL7i0gl0MUyrSx7OLjrvcwsaAuhHEALw_wcB

API documentation is available in the link below
https://woocommerce.github.io/woocommerce-rest-api-docs/?shell#introduction

The project is intended to show some working examples for commonly used pytest freatures like marks, fixtures, paramatrize, etc

The API response is validated with the data in the DB.

Steps:
Modules to install:
  pip install pytest
Then from the main directory, run
  python setup.py develop
  
 The tests are written in the tests folder.
 
 To run tests
 Run the tests
   pytest -m <the currosponding marker name>
   eg: pytest -m tcid10       
   eg: pytest -m orders       #This runs all the tests with orders marker.
   
