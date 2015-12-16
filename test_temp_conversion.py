from temp_conversion import fahr_to_kelvin

def test_random():
	assert fahr_to_kelvin(20.0)==266.4833333333333

def test_zero():
	assert round(fahr_to_kelvin(-459.67),2)==0.00

def test_positive():
	assert fahr_to_kelvin(50)>=273
