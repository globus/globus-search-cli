import httpretty
from tests.framework.responses import register_api_route_from_fixtures


def test_collection_show(run_line):
    path = "/v1/index/1a57bbe5-5272-477f-9d31-343b8258b7a5"
    register_api_route_from_fixtures("search", path, "GET", 200)

    output = run_line("globus-search show-index 1a57bbe5-5272-477f-9d31-343b8258b7a5")

    assert (
        output
        == """\
{
  "@datatype": "GSearchIndex",
  "@version": "2017-09-01",
  "creation_date": "2018-03-26 18:29:26",
  "description": "",
  "display_name": "mdf",
  "id": "1a57bbe5-5272-477f-9d31-343b8258b7a5",
  "max_size_in_mb": 5000,
  "num_entries": 970736,
  "num_subjects": 970737,
  "size_in_mb": 1770
}
"""
    )
    last_req = httpretty.last_request()
    assert last_req.method == "GET"
    assert last_req.path == path
