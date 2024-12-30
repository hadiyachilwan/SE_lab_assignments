# test_newotp.py
import unittest
from unittest.mock import patch
from otp2 import generate_otp, send_otp_email


class TestNewOtp(unittest.TestCase):
    def test_generate_otp(self):
        # Test if OTP has the correct length
        otp = generate_otp(6)
        self.assertEqual(len(otp), 6)

        # Test if OTP contains only digits
        self.assertTrue(otp.isdigit())

        # Test if OTP length can be customized
        otp = generate_otp(8)
        self.assertEqual(len(otp), 8)

        # Test invalid length
        with self.assertRaises(ValueError):
            generate_otp(0)

    @patch('newotp.smtplib.SMTP')
    def test_send_otp_email(self, mock_smtp):
        # Mock SMTP server
        mock_server = mock_smtp.return_value

        # Valid email test
        result = send_otp_email("123456", "your_email@gmail.com", "your_app_password", "recipient_email@example.com")
        self.assertTrue(result)
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with("your_email@gmail.com", "your_app_password")
        mock_server.send_message.assert_called_once()

        # Simulate email failure
        mock_server.send_message.side_effect = Exception("SMTP error")
        result = send_otp_email("123456", "your_email@gmail.com", "your_app_password", "recipient_email@example.com")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
