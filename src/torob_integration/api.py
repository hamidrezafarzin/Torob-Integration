import requests

class Torob:
    """
    # Class Torob: Interacts with the Torob API to fetch product data.

    ## Keyword arguments in functions :
    - `q`: Query string for product-related actions.
    - `page`: Page number for paginated results (default is 0).
    - `prk`: Product key identifier.
    - `search_id`: Search identifier for detailed product information.

    ## functions return:
    - For the `suggestion` method: Product suggestions based on the provided query.
    - For the `search` method: Paginated search results for products.
    - For the `details` method: Detailed information about a specific product.
    - For the `special_offers` method: Special offers for products with optional pagination.
    - For the `price_chart` method: Price chart data for a specific product.
    """

    def __init__(self):
        self._suggestion_url = "https://api.torob.com/suggestion2/"
        self._search_url = "https://api.torob.com/v4/base-product/search/"
        self._details_url = "https://api.torob.com/v4/base-product/details/"
        self._special_offers_url = "https://api.torob.com/v4/special-offers/"
        self._price_chart_url = "https://api.torob.com/v4/base-product/price-chart/"

    def suggestion(self, q: str) -> dict:
        params = {"q": q}
        result = self._send_get(url=self._suggestion_url, params=params)
        return result

    def search(self, q: str, page: int = 0) -> dict:
        params = {"q": q, "page": page}
        _result = self._send_get(url=self._search_url, params=params)
        result = self.__get_search_data_from_url(data=_result)
        return result

    def details(self, prk, search_id) -> dict:
        params = {"prk": prk, "search_id": search_id}
        result = self._send_get(url=self._details_url, params=params)
        return result

    def special_offers(self, page: int = 0) -> dict:
        params = {"page": page}
        result = self._send_get(url=self._special_offers_url, params=params)
        return result

    def price_chart(self, prk, search_id) -> dict:
        params = {"prk": prk, "search_id": search_id}
        result = self._send_get(url=self._price_chart_url, params=params)
        return result

    def _send_get(self, url: str, params: dict = None, timeout=5) -> dict:
        try:
            response = requests.get(url, params, timeout=timeout)
            response.raise_for_status()
            result_json = response.json()
        except requests.ConnectionError as e:
            raise ConnectionError
        else:
            return result_json

    def __get_search_data_from_url(self, data: dict) -> dict:
        for item in data["results"]:
            # Extract 'prk' and 'search_id' from 'more_info_url'
            prk_start = item["more_info_url"].find("prk=") + 4
            prk_end = item["more_info_url"].find("&", prk_start)
            prk = item["more_info_url"][prk_start:prk_end]

            search_id_start = item["more_info_url"].find("search_id=") + 10
            search_id_end = item["more_info_url"].find("&", search_id_start)
            search_id = item["more_info_url"][search_id_start:search_id_end]

            # Add 'prk' and 'search_id' to the current object
            item["prk"] = prk
            item["search_id"] = search_id
        return data
