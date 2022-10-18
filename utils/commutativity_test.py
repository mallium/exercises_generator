from commutativity import get_summands, get_factors, commutativity

def test_get_summands():
  assert get_summands("x+y") == ["x", "y"]
  assert get_summands("x-y") == ["x", "-y"]
  assert get_summands("-x-y") == ["-x", "-y"]
  assert get_summands("-12x+3y-4z") == ["-12x", "3y", "-4z"]
  assert get_summands("x+3y") == ["x", "3y"]
  assert get_summands("3x+4y") == ["3x", "4y"]
  assert get_summands("3xy+5z+nm9") == ["3xy", "5z", "nm9"]
  
def test_get_factors():
  assert get_factors("xy") == ["x", "y"]
  assert get_factors("xy^2") == ["x", "y^2"]
  assert get_factors("x^2y") == ["x^2", "y"]
  assert get_factors("x^3y^5") == ["x^3", "y^5"]
  assert get_factors("x^3y^67z^2") == ["x^3", "y^6", "7", "z^2"]
  assert get_factors("5x^2y^34tz^8") == ["5", "x^2", "y^3", "4", "t", "z^8"]
  
def test_commutativity():
  assert commutativity("3x+2") == ["3x+2", "2+3x", "x3+2", "2+x3"]
  assert commutativity("3x-2") == ["3x-2", "-2+3x", "x3-2", "-2+x3"]
  assert commutativity("-3x-5y") == ['-3x-5y', '-5y-3x', '-3x-y5', '-y5-3x', '-x3-5y', '-5y-x3', '-x3-y5', '-y5-x3']


  