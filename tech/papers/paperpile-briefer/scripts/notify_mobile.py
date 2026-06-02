# /// script
# requires-python = ">=3.11"
# ///
"""Send a mobile-friendly notification via ntfy, webhook, or Gmail."""

from __future__ import annotations

import argparse
import json
import os
import smtplib
import ssl
import urllib.request
from email.mime.text import MIMEText
from pathlib import Path


def load_env_file(path: str) -> None:
    if not path:
        return
    env_path = Path(path).expanduser()
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key.startswith("export "):
            key = key.removeprefix("export ").strip()
        value = value.strip().strip('"').strip("'")
        if key in {"GMAIL_ADDRESS", "GMAIL_APP_PASSWORD", "NTFY_TOPIC", "NTFY_SERVER", "MOBILE_WEBHOOK_URL", "NOTIFY_EMAIL_TO"}:
            os.environ.setdefault(key, value)


def post_ntfy(title: str, message: str, url: str) -> bool:
    topic = os.environ.get("NTFY_TOPIC", "").strip()
    if not topic:
        return False
    server = os.environ.get("NTFY_SERVER", "https://ntfy.sh").rstrip("/")
    req = urllib.request.Request(f"{server}/{topic}", data=message.encode("utf-8"), method="POST")
    req.add_header("Title", title)
    req.add_header("Tags", "books")
    if url:
        req.add_header("Click", url)
    urllib.request.urlopen(req, timeout=15).read()
    print("[OK] Mobile notification sent via ntfy")
    return True


def post_webhook(title: str, message: str, url: str) -> bool:
    webhook = os.environ.get("MOBILE_WEBHOOK_URL", "").strip()
    if not webhook:
        return False
    payload = json.dumps({"title": title, "message": message, "url": url}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(webhook, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    urllib.request.urlopen(req, timeout=15).read()
    print("[OK] Mobile notification sent via webhook")
    return True


def send_email(title: str, message: str, url: str) -> bool:
    gmail_address = os.environ.get("GMAIL_ADDRESS", "").strip()
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if not gmail_address or not gmail_app_password:
        return False
    body = message if not url else f"{message}\n\n{url}"
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = title
    msg["From"] = gmail_address
    msg["To"] = os.environ.get("NOTIFY_EMAIL_TO", gmail_address)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(gmail_address, gmail_app_password)
        server.send_message(msg)
    print("[OK] Mobile notification sent via Gmail")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--env-file", default="")
    args = parser.parse_args()

    load_env_file(args.env_file)
    for sender in (post_ntfy, post_webhook, send_email):
        try:
            if sender(args.title, args.message, args.url):
                return 0
        except Exception as exc:
            print(f"[WARN] Notification failed via {sender.__name__}: {exc}")
    print("[SKIP] No mobile notification channel configured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
