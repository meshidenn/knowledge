"""
Gmail SMTP で分析結果をメール送信
引数: 送信するMarkdownファイルのパス
"""

import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def markdown_to_html(md: str) -> str:
    """簡易 Markdown → HTML 変換"""
    lines = md.split("\n")
    html_lines = []
    for line in lines:
        s = line.strip()
        if s.startswith("### "):
            html_lines.append(f'<h3 style="color:#333;margin:20px 0 8px;font-size:15px;">{s[4:]}</h3>')
        elif s.startswith("## "):
            html_lines.append(f'<h2 style="color:#1a1a1a;margin:24px 0 12px;font-size:17px;border-bottom:1px solid #eee;padding-bottom:6px;">{s[3:]}</h2>')
        elif s.startswith("# "):
            html_lines.append(f'<h1 style="color:#000;margin:0 0 16px;font-size:20px;">{s[2:]}</h1>')
        elif s.startswith("- "):
            c = s[2:]
            if "⚡High" in c:
                c = c.replace("⚡High", '<span style="color:#d85a30;font-weight:600;">⚡High</span>')
            elif "🔵Medium" in c:
                c = c.replace("🔵Medium", '<span style="color:#378add;font-weight:600;">🔵Medium</span>')
            html_lines.append(f'<div style="margin:2px 0 2px 16px;font-size:14px;line-height:1.6;">• {c}</div>')
        elif s.startswith("  "):
            html_lines.append(f'<div style="margin:1px 0 1px 32px;font-size:13px;color:#555;line-height:1.6;">{s}</div>')
        elif s == "---":
            html_lines.append('<hr style="border:none;border-top:1px solid #eee;margin:16px 0;">')
        elif s:
            html_lines.append(f'<p style="margin:4px 0;font-size:14px;line-height:1.6;">{s}</p>')
    return "\n".join(html_lines)


def send_email(filepath: str):
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_address or not gmail_app_password:
        print("[ERROR] GMAIL_ADDRESS or GMAIL_APP_PASSWORD not set")
        sys.exit(1)

    content = Path(filepath).read_text()
    filename = Path(filepath).stem  # e.g. "2026-03-22" or "2026-W13"

    # サブジェクト判定
    high_count = content.count("⚡High")
    if "週次トレンド" in content:
        subject = f"📊 Weekly Trends {filename}"
    elif high_count > 0:
        subject = f"🔥{high_count} HF Papers {filename}"
    else:
        subject = f"📄 HF Papers {filename}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = gmail_address
    msg["To"] = gmail_address

    msg.attach(MIMEText(content, "plain", "utf-8"))

    html_body = f"""
<div style="max-width:640px;margin:0 auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#1a1a1a;">
{markdown_to_html(content)}
<div style="margin-top:32px;padding-top:16px;border-top:1px solid #eee;font-size:12px;color:#999;">
    <a href="https://huggingface.co/papers" style="color:#666;">HF Daily Papers</a> |
    Automated by GitHub Actions + Claude Code
</div>
</div>"""
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_address, gmail_app_password)
        server.send_message(msg)

    print(f"[OK] Email sent: {subject}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_email.py <markdown_file_path>")
        sys.exit(1)
    send_email(sys.argv[1])
