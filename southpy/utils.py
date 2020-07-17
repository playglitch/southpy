import requests

BASE_URL = "https://southpine.playglitch.xyz/api"

def add_south_metdata(
  res: Union[requests.Response],
  response_dict: Dict[str, Any],
  url: str
  ) -> Dict[str, Any]:
response_dict["south_url"] = url
response_dict["headers"] = dict(res.headers)
return response_dict

def get_profile_url(
  base_url: str,
  username: str
  ) -> str:
url = f"{base_url}/profile?username={username}"
return url

def get_miniprofile_url(
  base_url: str,
  username: str
  ) -> str:
url = f"{base_url}/mini_profile?username={username}"
return url

def get_lobby_url(
  base_url: str,
  lobbyid: int,
  auth_token: Optional[str]
  ) -> str:
url = f"{base_url}/lobby?lobbyid={lobbyid}"
if auth_token is not None:
          url += f"&auth={auth_token}" # Appends the auth token if provided
          return url