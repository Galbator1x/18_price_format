import pytest

from format_price import format_price


def idfn(val):
    return "params: {}".format(str(val))


@pytest.fixture(scope='function', params=[
    (1.1, '1.10'),
    (',0', '0'),
    ('5.', '5'),
    ('0495', '495'),
    ('5 . 0 3 ', '5.03'),
    (3245.000000, '3 245'),
    (5.03, '5.03'),
    (4686953.13456, '4 686 953.13'),
    (96543294, '96 543 294')],
    ids=idfn
)
def correct_param(request):
    return request.param


class TestPrice:
    def test_empty_string(self):
        with pytest.raises(ValueError):
            format_price('')

    @pytest.mark.parametrize('price', ['qweasd', '   ', '\t', '\n', '.',
                                       'dfg!.,$/-f=sfs', 'dg.fgh'])
    def test_letters_and_punctuations(self, price):
        with pytest.raises(ValueError):
            format_price(price)

    @pytest.mark.parametrize('price', ['..', '.5.', '5..2', '453.78.9',
                                       'fdg35.hgf.5 '])
    def test_more_than_one_dot(self, price):
        with pytest.raises(ValueError):
            format_price(price)

    @pytest.mark.parametrize('price', ['ro632.5g', '0,s', 'h96 .h 524'])
    def test_incorrect_price(self, price):
        with pytest.raises(ValueError):
            format_price(price)

    def test_correct_price(self, correct_param):
        input_param, expected_output = correct_param
        result = format_price(input_param)
        assert result == expected_output
