import unittest
import whenhome as wh


class WhenHomeTest(unittest.TestCase):

    #  wh.calculate_home_time

    def test_go_home_time(self):
        current_time = wh.str2dict("16:00")
        up_time = wh.str2dict("8:00")
        home_time = current_time
        self.assertEqual(wh.calculate_home_time(current_time, up_time), home_time)

    def test_definitly_go_home_time(self):
        current_time = wh.str2dict("16:20")
        up_time = wh.str2dict("8:13")
        home_time = wh.str2dict("16:07")
        self.assertEqual(wh.calculate_home_time(current_time, up_time), home_time)

    def test_stay_at_work_a_bit_more(self):
        current_time = wh.str2dict("16:08")
        up_time = wh.str2dict("6:55")
        home_time = wh.str2dict("17:13")
        self.assertEqual(wh.calculate_home_time(current_time, up_time), home_time)

    def test_stay_at_work_for_some_time(self):
        current_time = wh.str2dict("12:44")
        up_time = wh.str2dict("3:06")
        home_time = wh.str2dict("17:38")
        self.assertEqual(wh.calculate_home_time(current_time, up_time), home_time)

    def test_stay_at_work_but_it_is_lunch_time(self):
        current_time = wh.str2dict("13:00")
        up_time = wh.str2dict("4:00")
        home_time = wh.str2dict("17:00")
        self.assertEqual(wh.calculate_home_time(current_time, up_time), home_time)

    #  wh.how_much_work_time_left

    def test_time_left_to_go_home(self):
        up_time = wh.str2dict("8:00")
        result_time = wh.str2dict("0:00")
        self.assertEqual(wh.how_much_work_time_left(up_time), result_time)

    def test_time_left_to_definitly_go_home(self):
        up_time = wh.str2dict("8:13")
        result_time = wh.str2dict("0:-13")
        self.assertEqual(wh.how_much_work_time_left(up_time), result_time)

    def test_time_left_to_stay_at_work_a_bit_more(self):
        up_time = wh.str2dict("6:55")
        result_time = wh.str2dict("1:05")
        self.assertEqual(wh.how_much_work_time_left(up_time), result_time)

    def test_time_left_to_stay_at_work_for_some_time(self):
        up_time = wh.str2dict("3:06")
        result_time = wh.str2dict("4:54")
        self.assertEqual(wh.how_much_work_time_left(up_time), result_time)

    def test_time_left_to_stay_at_work_but_it_is_lunch_time(self):
        up_time = wh.str2dict("4:00")
        result_time = wh.str2dict("4:00")
        self.assertEqual(wh.how_much_work_time_left(up_time), result_time)

if __name__ == '__main__':
    unittest.main()
