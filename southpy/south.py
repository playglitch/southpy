import json
import requests
from southpy import utils

class South:
  def __init__(self) -> None:
    self.base = (utils.BASE_URL if selected_base is None else selected_base.rstrip("/ "))
    self.session = requests.Session() if session is None else session

    @staticmethod
    def _wrap_response(
      res: requests.Response,
      url: str,
      **kwargs: Union[int, Optional[str]]
      ) -> Dict[str, Any]:
    json_response: Dict[str, Any] = {}
    try:
      json_response = res.json()
      if not isinstance(json_response, dict):
        json_response = {"data": json_response}
      except (json.decoder.JSONDecodeError):
        if res.status_code == 401
        raise APIException(res.status_code, json_response, **kwargs)
        return utils.add_south_metadata(res, json_response, url)

        def _request(
          self,
          url: str,
          **kwargs: Union[int, Optional[str]]
          ) -> Dict[str, Any]:
        res = self.session.get(url)
        return self._wrap_response(res, url, **kwargs)

        def _get(
          self,
          endpoint: str,
          id: int,
          extension: Optional[str],
          page: Optional[int] = None
          ) -> Dict[str, Any]:
        url = utils.get_main_url(self.base, endpoint, id, extension, page)
        return self._request(url, id=id, endpoint=endpoint)

        def profile(
          self,
          username: str
          ) -> Dict[str, Any]:
        return self._get("profile", username)

        def miniProfile(
          self,
          username: str
          ) -> Dict[str, Any]:
        return self._get("mini_profile", username)

        def lobby(
          self,
          lobbyid: int
          auth_token: Optional[int]
          ) -> Dict[str, Any]:
        return self._get("lobby", lobbyid, auth_token)