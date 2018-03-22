# bulid by Bean_Wei/ 2018/3/20 11:23
import six

from filters.schema import base_query_params_schema
from filters.validations import CSVofIntegers,IntegerLike,DatetimeWithTZ

post_query_schema = base_query_params_schema.extend({
    "title": six.text_type,
    "content": six.text_type,
    "slug": six.text_type,
    "timestamp": DatetimeWithTZ(),
    "tags": six.text_type,
    "category": six.text_type,
    "read_num": IntegerLike(),
    "own": CSVofIntegers(),
    "published": CSVofIntegers(),
})

