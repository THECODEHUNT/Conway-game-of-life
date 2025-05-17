from utils import next_gen

def test_blinker():
    blinker1 = {(1,0), (1,1), (1,2)}
    blinker2 = {(0,1), (1,1), (2,1)}
    assert next_gen(blinker1) == blinker2
    assert next_gen(blinker2) == blinker1
