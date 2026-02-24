from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        event = request.form['event']
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Registration Confirmed</title>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }}
                .confirmation-container {{
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    max-width: 500px;
                    width: 100%;
                    padding: 40px;
                    text-align: center;
                    animation: slideIn 0.5s ease-out;
                }}
                @keyframes slideIn {{
                    from {{
                        opacity: 0;
                        transform: translateY(-30px);
                    }}
                    to {{
                        opacity: 1;
                        transform: translateY(0);
                    }}
                }}
                .success-icon {{
                    width: 80px;
                    height: 80px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 20px;
                    font-size: 40px;
                    color: white;
                }}
                h2 {{
                    color: #333;
                    margin-bottom: 10px;
                    font-size: 28px;
                }}
                p {{
                    color: #666;
                    margin-bottom: 30px;
                    font-size: 16px;
                    line-height: 1.6;
                }}
                .details {{
                    background: #f8f9fa;
                    border-radius: 10px;
                    padding: 25px;
                    margin-bottom: 20px;
                    text-align: left;
                }}
                .detail-row {{
                    display: flex;
                    justify-content: space-between;
                    padding: 12px 0;
                    border-bottom: 1px solid #e0e0e0;
                }}
                .detail-row:last-child {{
                    border-bottom: none;
                }}
                .detail-label {{
                    font-weight: 600;
                    color: #555;
                }}
                .detail-value {{
                    color: #333;
                }}
                a {{
                    display: inline-block;
                    padding: 15px 30px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: 600;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
                }}
                a:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
                }}
            </style>
        </head>
        <body>
            <div class="confirmation-container">
                <div class="success-icon">✓</div>
                <h2>Thank you {name}!</h2>
                <p>You have successfully registered for {event}</p>
                <div class="details">
                    <div class="detail-row">
                        <span class="detail-label">Name:</span>
                        <span class="detail-value">{name}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Email:</span>
                        <span class="detail-value">{email}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Phone:</span>
                        <span class="detail-value">{phone}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Event:</span>
                        <span class="detail-value">{event}</span>
                    </div>
                </div>
                <p style="font-size: 14px; color: #999;">Confirmation sent to {email}</p>
                <a href="/">Back to Registration</a>
            </div>
        </body>
        </html>
        """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


print("CI/CD Pipeline Triggered Successfully")