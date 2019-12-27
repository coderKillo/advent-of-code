import unittest
import sys
import run as app

class Pointer_Tests(unittest.TestCase):

    def test_init(self):
        p = app.Point()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
    
    def test_init_value(self):
        p = app.Point(1,2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
    
    def test_neg(self):
        p = app.Point(1,2)
        p = -p
        self.assertEqual(p.x, -1)
        self.assertEqual(p.y, -2)
    
    def test_add(self):
        p1 = app.Point(1,2)
        p2 = app.Point(3,4)
        p3 = p1 + p2
        self.assertEqual(p3.x, 4)
        self.assertEqual(p3.y, 6)

    def test_sub(self):
        p1 = app.Point(1,2)
        p2 = app.Point(3,5)
        p3 = p2 - p1
        self.assertEqual(p3.x, 2)
        self.assertEqual(p3.y, 3)
    
    def test_manhatten(self):
        p1 = app.Point()
        p2 = app.Point(6,6)
        self.assertEqual(p1.manhatten(p2), 12)

        p2 = app.Point(-6,6)
        self.assertEqual(p1.manhatten(p2), 12)

        p1 = app.Point(2,14)
        p2 = app.Point(2,6)
        self.assertEqual(p1.manhatten(p2), 8)

class WirePlan_Tests(unittest.TestCase):

    def setUp(self):
        self.wires = [['R20', 'U20', 'L40', 'D10'], ['D10', 'R5', 'U15', 'L10']]
        self.wireplan = app.WirePlan(self.wires)
    
    def test_create_plan(self):
        plan = app.WirePlan.create_plan(w=3,h=5)
        self.assertEqual(len(plan), 6,"row should be equal to height + 1 (0..h)") 
        self.assertEqual(len(plan[0]), 4,"one row should have elements equal to width + 1 (0..w)") 

    def test_calculatePlanSize(self):
        w, h = self.wireplan.calculatePlanSize(self.wires[0:1])
        self.assertEqual(w, 40)
        self.assertEqual(h, 20)

        w, h = self.wireplan.calculatePlanSize(self.wires[1:2])
        self.assertEqual(w, 10)
        self.assertEqual(h, 15)

        w, h = self.wireplan.calculatePlanSize(self.wires)
        self.assertEqual(w, 40)
        self.assertEqual(h, 30)
    
    def test_central_port(self):
        self.assertEqual(self.wireplan.c_port.x, 20)
        self.assertEqual(self.wireplan.c_port.y, 10)
    
    def test_setter_getter(self):
        self.wireplan.set_field(app.Point(10,5), 4, 10)

        id = self.wireplan.get_field_id(app.Point(10,5))
        self.assertEqual(id, 4)

        count = self.wireplan.get_field_count(app.Point(10,5))
        self.assertEqual(count, 10)

        self.wireplan.set_field(app.Point(10,5), 4, 20)
        count = self.wireplan.get_field_count(app.Point(10,5))
        self.assertEqual(count, 30)

    
    def test_checkIntersection(self):
        point = app.Point(10,5) 
        self.wireplan.ptr = point
        self.wireplan.wire_idx = 1
        self.assertFalse(self.wireplan.checkIntersection())

        self.wireplan.set_field(point, 1, 0)
        self.assertFalse(self.wireplan.checkIntersection())

        self.wireplan.set_field(point, 2, 0)
        self.assertTrue(self.wireplan.checkIntersection())

    def test_move(self):
        self.wireplan.ptr = app.Point()

        self.wireplan.move(app.Point(10,0))
        self.assertEqual(self.wireplan.ptr.x, 10)
        self.assertEqual(self.wireplan.ptr.y, 0)

        self.wireplan.move(app.Point(0,5))
        self.assertEqual(self.wireplan.ptr.x, 10)
        self.assertEqual(self.wireplan.ptr.y, 5)

        self.wireplan.move(app.Point(-6,0))
        self.assertEqual(self.wireplan.ptr.x, 4)
        self.assertEqual(self.wireplan.ptr.y, 5)

        self.wireplan.move(app.Point(0,-3))
        self.assertEqual(self.wireplan.ptr.x, 4)
        self.assertEqual(self.wireplan.ptr.y, 2)
    
    
class Test_Process(unittest.TestCase):

    def test_process1_example(self):
        wires = [["U7","R6","D4","L4"],["R8","U5","L5","D3"]]
        output = app.process1(wires)

        p = app.WirePlan(wires)
        self.assertEqual(output, 6)

    def test_process1_test1(self):
        wires = [["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"]]
        output = app.process1(wires)
        self.assertEqual(output, 159)

    def test_process2_example(self):
        wires = [["U7","R6","D4","L4"],["R8","U5","L5","D3"]]
        plan = app.WirePlan(wires)

        x_ptr = plan.intersections
        self.assertEqual(x_ptr[0].x, 6)
        self.assertEqual(x_ptr[0].y, 5)
        self.assertEqual(x_ptr[1].x, 3)
        self.assertEqual(x_ptr[1].y, 3)

        x_ptr = list(map(plan.get_field_count, x_ptr))
        self.assertEqual(x_ptr[0], 30)
        self.assertEqual(x_ptr[1], 40)

    def test_process2_test1(self):
        wires = [["R75","D30","R83","U83","L12","D49","R71","U7","L72"],["U62","R66","U55","R34","D71","R55","D58","R83"]]
        output = app.process2(wires)
        self.assertEqual(output,610)
    
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

if __name__ == '__main__':
    unittest.main()