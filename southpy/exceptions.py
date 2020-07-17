class APIException(Exception):
  def __init__(
    self,
    status: int,
    error_json: Optional[Mapping[str, Any]] = None,
    ):
  self.status = status
  self.error_json = error_json
  super().__init__(self.status_code)

  def __str__(self) -> str:
    output = f"HTTP {self.status_code}"
    if self.error_json:
      error_str = ", ".join(f"{k}={v}" for k, v in self.error_json.items())
      output += f" - {error_str}"
      return output

  def __repr__(self) -> str:
    return (
      f"APIException(status_code={self.status_code}, "
      f"error_json={self.error_json})"
    )