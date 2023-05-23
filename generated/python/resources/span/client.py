# This file was auto-generated by Fern from our API Definition.

import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import FintoLangfuseEnvironment
from .types.create_llm_span_request import CreateLLMSpanRequest
from .types.create_span_request import CreateSpanRequest
from .types.span import Span
from .types.update_span_request import UpdateSpanRequest


class SpanClient:
    def __init__(self, *, environment: FintoLangfuseEnvironment):
        self._environment = environment

    def create_llm_call(self, *, request: CreateLLMSpanRequest) -> Span:
        _response = httpx.request(
            "POST", urllib.parse.urljoin(f"{self._environment}/", "api/llm-span"), json=jsonable_encoder(request)
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Span, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: CreateSpanRequest) -> Span:
        _response = httpx.request(
            "POST", urllib.parse.urljoin(f"{self._environment}/", "api/spans"), json=jsonable_encoder(request)
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Span, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, *, request: UpdateSpanRequest) -> Span:
        _response = httpx.request(
            "PATCH", urllib.parse.urljoin(f"{self._environment}/", "api/spans"), json=jsonable_encoder(request)
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Span, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
