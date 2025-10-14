# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
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


# 11
class TestCreditCardValidation(unittest.TestCase):
    """
    Tests validate creditcard
    """

    def test_invalid_short_lenght(self):
        """Invalid card lenght"""
        self.assertEqual(validate_credit_card("123456"), "Invalid Card")

    def test_valid_card(self):
        """valid lenght"""
        self.assertEqual(validate_credit_card("12345689101112"), "Valid Card")

    def test_no_numeric_card(self):
        """Invalid not digit"""
        self.assertEqual(validate_credit_card("abcdefghijklmn"), "Invalid Card")

    def test_invalid_long_lenght(self):
        """Invalid card lenght"""
        self.assertEqual(validate_credit_card("123456"), "Invalid Card")


# 12
class TestDateValidation(unittest.TestCase):
    """
    Pruebas para validate_date.
    """

    def test_valid_date(self):
        """valid date"""
        self.assertEqual(validate_date(2024, 10, 14), "Valid Date")

    def test_invalid_year_under_date(self):
        """under year"""
        self.assertEqual(validate_date(1890, 10, 14), "Invalid Date")

    def test_invalid_year_over_date(self):
        """over year"""
        self.assertEqual(validate_date(2222, 10, 14), "Invalid Date")

    def test_invalid_month_under_date(self):
        """under month"""
        self.assertEqual(validate_date(2024, 0, 14), "Invalid Date")

    def test_invalid_month_over_date(self):
        """over month"""
        self.assertEqual(validate_date(2024, 15, 14), "Invalid Date")

    def test_invalid_day_under_date(self):
        """under day"""
        self.assertEqual(validate_date(2024, 10, 0), "Invalid Date")

    def test_invalid_day_over_date(self):
        """over day"""
        self.assertEqual(validate_date(2024, 10, 40), "Invalid Date")


# 13
class TestFlightEligibility(unittest.TestCase):
    """
    Pruebas para check_flight_eligibility.
    """

    def test_eligible_by_age_in_range(self):
        "Age elegible"
        self.assertEqual(check_flight_eligibility(35, False), "Eligible to Book")

    def test_eligible_by_frequent_flyer_under_age(self):
        "frequent elegible"
        self.assertEqual(check_flight_eligibility(16, True), "Eligible to Book")

    def test_eligible_by_frequent_flyer_over_age(self):
        "overage elegible"
        self.assertEqual(check_flight_eligibility(70, True), "Eligible to Book")

    def test_not_eligible_under_age(self):
        "underage not-elegible"
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_not_eligible_over_age(self):
        "overage not-elegible"
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


# 14
class TestUrlValidation(unittest.TestCase):
    """
    Pruebas para validate_url.
    """

    def test_valid_http_url(self):
        """valid http"""
        self.assertEqual(validate_url("http://google.com"), "Valid URL")

    def test_valid_https_url(self):
        """valid https"""
        self.assertEqual(validate_url("https://www.iteso.mx/home"), "Valid URL")

    def test_valid_max_length_url(self):
        """valid http max length"""
        long_url = "http://" + "a" * (248)
        self.assertEqual(validate_url(long_url), "Valid URL")

    def test_invalid_no_protocol(self):
        """invalid no http/s"""
        self.assertEqual(validate_url("www.google.com"), "Invalid URL")

    def test_invalid_too_long_http(self):
        """too long http"""
        long_url = "http://" + "a" * 256
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_valid_too_long_https(self):
        """long https"""
        long_url = "https://" + "a" * 256
        self.assertEqual(validate_url(long_url), "Valid URL")

    def test_invalid_empty_string(self):
        """empty"""
        self.assertEqual(validate_url(""), "Invalid URL")


# 15
class TestDiscountCalculation(unittest.TestCase):
    """
    Pruebas para calculate_quantity_discount.
    """

    def test_no_discount_lower(self):
        """no discount lower"""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_no_discount_upper(self):
        """no discount upper"""
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent_discount_lower(self):
        """5% lower"""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_five_percent_discount_upper(self):
        """5% upper"""
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_over_conditions_discount(self):
        """10% discount"""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_between_conditions_discount(self):
        """10% discount between conditions"""
        self.assertEqual(calculate_quantity_discount(5.5), "10% Discount")

    def test_invalid_quantity_zero(self):
        """invalid quantity"""
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")


# 16
class TestFileSizeValidation(unittest.TestCase):
    """
    Pruebas para check_file_size.
    """

    def test_valid_size_lower(self):
        """0 Valid size"""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_valid_size_upper(self):
        """upper valid size"""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_valid_size_in_range(self):
        """In range valid size"""
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_invalid_size_negative(self):
        """Invalid negative size"""
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_invalid_size_over_limit(self):
        """size over limit"""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


# 17
class TestLoanEligibility(unittest.TestCase):
    """Pruebas check_loan_eligibility."""

    def test_not_eligible_low_income(self):
        """not elegible"""
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_standard_loan_between_income(self):
        """standard loan between income"""
        self.assertEqual(check_loan_eligibility(45000, 701), "Standard Loan")

    def test_secured_loan(self):
        """secured loan"""
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_premium_loan(self):
        """premium loan"""
        self.assertEqual(check_loan_eligibility(80000, 751), "Premium Loan")

    def test_standard_loan_high_income(self):
        """standard loan high income"""
        self.assertEqual(check_loan_eligibility(80000, 750), "Standard Loan")

    def test_standard_loan_with_income_lower_bound(self):
        """standard loan low income"""
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")


# 18
class TestShippingCost(unittest.TestCase):
    """
    Pruebas calculate_shipping_cost.
    """

    def test_little_package_cost(self):
        """little package"""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package_cost(self):
        """medium package"""
        self.assertEqual(calculate_shipping_cost(5, 20, 20, 20), 10)

    def test_over_dimensions_package_cost(self):
        """overdimension package"""
        self.assertEqual(calculate_shipping_cost(1, 10, 31, 10), 20)

    def test_little_package_overdimension_cost(self):
        """little package overdimension"""
        self.assertEqual(calculate_shipping_cost(1, 15, 10, 10), 20)

    def test_medium_package_underdimension_cost(self):
        """medium package underdimension"""
        self.assertEqual(calculate_shipping_cost(5, 10, 20, 20), 20)

    def test_little_package_overweight_cost(self):
        """little package overweight"""
        self.assertEqual(calculate_shipping_cost(2, 10, 10, 10), 20)

    def test_medium_package_underweight_cost(self):
        """underweight package cost"""
        self.assertEqual(calculate_shipping_cost(1, 20, 20, 20), 20)


# 19
class TestQuizGrading(unittest.TestCase):
    """
    Pruebas para grade_quiz.
    """

    def test_pass(self):
        """pass"""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass(self):
        """conditional pass"""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail_no_correct(self):
        """No correct"""
        self.assertEqual(grade_quiz(0, 0), "Fail")

    def test_fail_too_many_incorrect(self):
        """too many incorrect"""
        self.assertEqual(grade_quiz(10, 4), "Fail")


# 20
class TestUserAuthenticationLogger(unittest.TestCase):
    """
    Pruebas para grade_quiz.
    """

    def test_admin_auth(self):
        """admin"""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_user_auth(self):
        """user"""
        self.assertEqual(authenticate_user("12345", "12345678"), "User")

    def test_user_admin(self):
        """user admin"""
        self.assertEqual(authenticate_user("admin", "12345678"), "User")

    def test_invalid_user_pass(self):
        """invalid pass"""
        self.assertEqual(authenticate_user("12345", "1234567"), "Invalid")

    def test_invalid_user(self):
        """invalid user"""
        self.assertEqual(authenticate_user("1234", "12345678"), "Invalid")


# 21
class TestWeatherAdvisory(unittest.TestCase):
    """
    Pruebas para la función get_weather_advisory.
    """

    def test_high_temp_and_humidity(self):
        """High temp High Humidity"""
        self.assertEqual(
            get_weather_advisory(40, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """-1 temp"""
        self.assertEqual(get_weather_advisory(-1, 80), "Low Temperature. Bundle Up!")

    def test_no_advisory(self):
        """No advisory"""
        self.assertEqual(get_weather_advisory(25, 60), "No Specific Advisory")

    def test_no_advisory_high_temp(self):
        """High temp no advise"""
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")

    def test_no_advisory_high_humidity(self):
        """High humid no advise"""
        self.assertEqual(get_weather_advisory(25, 80), "No Specific Advisory")

    def test_no_advisory_at_zero(self):
        """0 temperature"""
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")


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


# 24
class TestUserAuthentication(unittest.TestCase):
    """
    Pruebas para la clase UserAuthentication.
    """

    def test_initial_state(self):
        """Test Estado Inicial"""
        auth = UserAuthentication()
        self.assertEqual(auth.state, "Logged Out")

    def test_login(self):
        """Test login"""
        auth = UserAuthentication()
        res = auth.login()
        self.assertEqual(auth.state, "Logged In")
        self.assertEqual(res, "Login successful")

    def test_logout(self):
        """Test logout"""
        auth = UserAuthentication()
        auth.login()
        res = auth.logout()
        self.assertEqual(auth.state, "Logged Out")
        self.assertEqual(res, "Logout successful")

    def test_logout_while_out(self):
        """Failed Logout"""
        auth = UserAuthentication()
        res = auth.logout()
        self.assertEqual(auth.state, "Logged Out")
        self.assertEqual(res, "Invalid operation in current state")

    def test_login_while_in(self):
        """Failed Login"""
        auth = UserAuthentication()
        auth.login()
        res = auth.login()
        self.assertEqual(auth.state, "Logged In")
        self.assertEqual(res, "Invalid operation in current state")


# 25


# 26
class TestElevatorSystem(unittest.TestCase):
    """
    Pruebas para ElevatorSystem.
    """

    def test_initial_state(self):
        """Revisar el estado inicial"""
        elevator = ElevatorSystem()
        self.assertEqual(elevator.state, "Idle")

    def test_move_up(self):
        """Intentar mover hacia arriba"""
        elevator = ElevatorSystem()
        res = elevator.move_up()
        self.assertEqual(res, "Elevator moving up")
        self.assertEqual(elevator.state, "Moving Up")

    def test_move_down(self):
        """Ir hacia abajo"""
        elevator = ElevatorSystem()
        res = elevator.move_down()
        self.assertEqual(res, "Elevator moving down")
        self.assertEqual(elevator.state, "Moving Down")

    def test_stop_move_up(self):
        """Detener el movimiento hacia arriba"""
        elevator = ElevatorSystem()
        elevator.move_up()
        res = elevator.stop()
        self.assertEqual(res, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_stop_move_down(self):
        """Detener el movimiento hacia abajo"""
        elevator = ElevatorSystem()
        elevator.move_down()
        res = elevator.stop()
        self.assertEqual(res, "Elevator stopped")
        self.assertEqual(elevator.state, "Idle")

    def test_failed_stop(self):
        """fallo al intentar parar estando parado"""
        elevator = ElevatorSystem()
        res = elevator.stop()
        self.assertEqual(res, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Idle")

    def test_failed_up(self):
        """Intentar subir sin que sea idle"""
        elevator = ElevatorSystem()
        elevator.move_up()
        res = elevator.move_up()
        self.assertEqual(res, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Up")

    def test_failed_down(self):
        """Intentar bajar siendo no idle"""
        elevator = ElevatorSystem()
        elevator.move_down()
        res = elevator.move_down()
        self.assertEqual(res, "Invalid operation in current state")
        self.assertEqual(elevator.state, "Moving Down")
