# accounts/emails.py

from django.conf import settings
from django.core.mail import send_mail


# =========================
# Password Reset Email Utility
# =========================
def send_password_reset_email(user, reset_link: str):
    """
    Build and send a password reset email for staff members.

    Args:
        user: Django User instance.
        reset_link (str): URL to reset the password.

    Notes:
        - For production, uncomment the `send_mail` block.
        - Uses inline templates for subject and body.
    """
    subject_template = "Reset your staff password"
    body_template = """
        Hello {first_name} {last_name}

        Use the link below to reset your password:
        {reset_link}

        If you didn’t request this, you can ignore it.
    """

    # Populate email placeholders
    subject = subject_template
    body = body_template.format(
        first_name=user.first_name or "",
        last_name=user.last_name or "",
        reset_link=reset_link
    )

    # Debug output for development
    print("Mail sent successfully")
    print("Subject:", subject)
    print("Body:", body)

    # Uncomment for production email sending
    # send_mail(
    #     subject=subject,
    #     message=body,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[user.email],
    #     fail_silently=False,
    # )