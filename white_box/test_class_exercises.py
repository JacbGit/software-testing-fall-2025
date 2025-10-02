# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


# 1
class TestWhiteBoxCheckNumberStatus(unittest.TestCase):
    """
    Check_number_status tests.
    """

    def test_check_number_negative(self):
        """
        checks -
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_zero(self):
        """
        checks 0
        """
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_positive(self):
        """
        checks +
        """
        self.assertEqual(check_number_status(1), "Positive")


# 2
class TestValidatePassword(unittest.TestCase):
    """
    Validate password unit tests.
    """

    def test_validate_password_empty(self):
        """
        Checks an empty password, expecting False.
        """
        self.assertFalse(validate_password(""))

    def test_validate_password_only_digits(self):
        """
        Checks a password with only digits, expecting False.
        """
        self.assertFalse(validate_password("12345678"))

    def test_validate_password_valid(self):
        """
        Checks a valid password, expecting True.
        """
        self.assertTrue(validate_password("Ab#deFg123"))

    def test_validate_password_only_special_chars(self):
        """
        Checks a password with only special characters.
        """
        self.assertFalse(validate_password("#@!$%&%$!@#"))


# 3
class TestCalculateTotalDiscount(unittest.TestCase):
    """
    Calculate total discount unit tests.
    """

    def test_calculate_total_discount_no_discount(self):
        """
        no discount
        """
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_ten_percent(self):
        """
        10% discount
        """
        self.assertEqual(calculate_total_discount(100), 10)
        self.assertEqual(calculate_total_discount(500), 50)

    def test_calculate_total_discount_twenty_percent(self):
        """
        20% discount
        """
        self.assertEqual(calculate_total_discount(501), 100.2)


# 4
class TestCalculateOrderTotal(unittest.TestCase):
    """
    Unit tests for the calculate_order_total function.
    """

    def test_no_discount(self):
        """no discount."""
        items = [{"quantity": 5, "price": 20}]
        self.assertEqual(calculate_order_total(items), 100)

    def test_5_percent_discount(self):
        """5% discount."""
        items = [{"quantity": 10, "price": 20}]
        self.assertAlmostEqual(calculate_order_total(items), 190)

    def test_10_percent_discount(self):
        """10% discount."""
        items = [{"quantity": 11, "price": 20}]
        self.assertAlmostEqual(calculate_order_total(items), 198)

    def test_multiple_items_mixed_discounts(self):
        """Tests a mix of discounts."""
        items = [
            {"quantity": 4, "price": 10},  # No discount: 40
            {"quantity": 8, "price": 10},  # 5% discount: 76
            {"quantity": 12, "price": 10},  # 10% discount: 108
        ]
        self.assertAlmostEqual(calculate_order_total(items), 224)

    def test_empty_order(self):
        """Empty order."""
        self.assertEqual(calculate_order_total([]), 0)


# 5
class TestCalculateShippingCost(unittest.TestCase):
    """
    Unit tests for the calculate_items_shipping_cost function.
    """

    def test_standard_shipping_light(self):
        """Standard shipping, light weight."""
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_medium(self):
        """Standard shipping, medium weight."""
        items = [{"weight": 8}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_heavy(self):
        """Standard shipping, heavy weight."""
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_light(self):
        """Express shipping, light weight."""
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_medium(self):
        """Express shipping, medium weight."""
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_heavy(self):
        """Express shipping, heavy weight."""
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """invalid method."""
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "turbo")


# 6
class TestValidateLogin(unittest.TestCase):
    """
    Unit tests for the validate_login function.
    """

    def test_successful_login(self):
        """valid login attempt."""
        self.assertEqual(validate_login("myusername", "password"), "Login Successful")

    def test_unsuccessful_login_short_usermame(self):
        """Invalid login attempt."""
        self.assertEqual(validate_login("myus", "password"), "Login Failed")

    def test_unsuccessful_login_longer_usermame(self):
        """Invalid login attempt."""
        self.assertEqual(
            validate_login("myusertoolongbecauseitneedstofail", "password"),
            "Login Failed",
        )

    def test_unsuccessful_login_short_password(self):
        """Invalid login attempt."""
        self.assertEqual(validate_login("myuser", "passwor"), "Login Failed")

    def test_unsuccessful_login_longer_password(self):
        """Invalid login attempt."""
        self.assertEqual(
            validate_login("myuser", "passwordtoolongfailure"), "Login Failed"
        )


# 7
class TestVerifyAge(unittest.TestCase):
    """
    Unit tests for the verify_age function.
    """

    def test_elegible_age(self):
        """Elegible."""
        self.assertEqual(verify_age(30), "Eligible")

    def test_notelegible_under_age(self):
        """Elegible."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_notelegible_over_age(self):
        """Elegible."""
        self.assertEqual(verify_age(66), "Not Eligible")


# 8
class TestCategorizeProduct(unittest.TestCase):
    """
    Unit tests for the categorize_product function.
    """

    def test_category_a(self):
        """Elegible."""
        self.assertEqual(categorize_product(25), "Category A")

    def test_category_b(self):
        """Elegible."""
        self.assertEqual(categorize_product(75), "Category B")

    def test_category_c(self):
        """Elegible."""
        self.assertEqual(categorize_product(150), "Category C")

    def test_category_d(self):
        """Elegible."""
        self.assertEqual(categorize_product(250), "Category D")

    def test_category_d_under_10(self):
        """Elegible."""
        self.assertEqual(categorize_product(9), "Category D")


# 9
class TestValidateEmail(unittest.TestCase):
    """
    Unit tests for the validate_email function.
    """

    def test_valid_email(self):
        """Valid Email"""
        self.assertEqual(validate_email("Jaime@iteso.mx"), "Valid Email")

    def test_invalid_email_short(self):
        """Valid Email"""
        self.assertEqual(validate_email("J@.x"), "Invalid Email")

    def test_invalid_email_long(self):
        """Valid Email"""
        self.assertEqual(
            validate_email(
                "Jaimecontrerasitesoypanfilopararellenarelespacio@iteso.com.mx"
            ),
            "Invalid Email",
        )

    def test_invalid_email_no_at(self):
        """Valid Email"""
        self.assertEqual(validate_email("Jaimeiteso.mx"), "Invalid Email")

    def test_invalid_email_no_dot(self):
        """Valid Email"""
        self.assertEqual(validate_email("Jaime@itesomx"), "Invalid Email")


# 10
class TestCelciusToFahrenheit(unittest.TestCase):
    """
    Unit tests for the celcius_to_fahrenheit function.
    """

    def test_0_point(self):
        """0"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_100negative(self):
        """-100"""
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_100(self):
        """100"""
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_over_100(self):
        """120"""
        self.assertEqual(celsius_to_fahrenheit(120), "Invalid Temperature")

    def test_under_negative_100(self):
        """-120"""
        self.assertEqual(celsius_to_fahrenheit(-120), "Invalid Temperature")


# 23
class TestTrafficLight(unittest.TestCase):
    """
    Unit tests for the TrafficLight function.
    """

    def test_traffic_light_initial(self):
        """Red check"""

        light = TrafficLight()
        self.assertEqual(light.get_current_state(), "Red")

    def test_traffic_light_green(self):
        """Change green"""

        light = TrafficLight()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Green")

    def test_traffic_light_yellow(self):
        """Change Yellow"""

        light = TrafficLight()
        light.change_state()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Yellow")

    def test_traffic_light_red(self):
        """Back to RED"""

        light = TrafficLight()
        light.change_state()
        light.change_state()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Red")
