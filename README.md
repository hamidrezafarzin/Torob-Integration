<h1 align="center">Python Torob Integration </h1>

# Overview

- [Introduction](#introduction)
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Introduction
A Python module facilitating effortless interaction with the Torob API for seamless access to product suggestions, search results, detailed product information, special offers, and price chart data.
This module utilizes the Torob API available at [https://torob.com/](https://torob.com/). It is important to note that the usage of this module does not alter any data on the Torob website.


# Installation
A Python module facilitating effortless interaction with the Torob API for seamless access to product data. in order to use this module you have to install it by pip command or through setup.

```bash
pip install torob-integration
```
Import package into your project by:

```bash
from torob_integration.api import Torob
```
in order to use the module please consider looking at examples and documentations.

# Usage

import module and create object
```python
from torob_integration.api import Torob
torob_instance = Torob()
```

Fetch product suggestions based on a query
```python
from torob_integration.api import Torob
torob_instance = Torob()
suggestion_result = torob_instance.suggestion("laptop")
```

Perform a search for products based on a query and page number
```python
from torob_integration.api import Torob
torob_instance = Torob()
search_result = torob_instance.search("phone", page=0)
```

Get detailed information about a specific product. Note: Before running the `details` function, execute the `search` function to obtain the actual values for 'prk' and 'search_id'.
```python
from torob_integration.api import Torob
torob_instance = Torob()
details_result = torob_instance.details(prk='sample_prk', search_id='sample_search_id')
```

Fetch special offers for products with optional pagination based on page number
```python
from torob_integration.api import Torob
torob_instance = Torob()
special_offers_result = torob_instance.special_offers(page=0)
```

Get the price chart data for a specific product, Note: Before running the `price_chart` function, execute the `search` function to obtain the actual values for 'prk' and 'search_id'.
```python
from torob_integration.api import Torob
torob_instance = Torob()
price_chart_result = torob_instance.price_chart(prk='sample_prk', search_id='sample_search_id')
```


## license
MIT license
