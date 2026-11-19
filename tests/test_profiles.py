import pytest
from launcher.profiles import offline_uuid,validate_nickname
def test_valid(): assert validate_nickname("Lazy_123")=="Lazy_123"
@pytest.mark.parametrize("s",["ab","this_name_is_too_long","имя","bad-name",""])
def test_invalid(s):
    with pytest.raises(ValueError): validate_nickname(s)
def test_uuid():
    x=offline_uuid("LazyPlayer"); assert x==offline_uuid("LazyPlayer") and len(x)==36
