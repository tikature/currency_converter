from datetime import datetime
from flask import render_template

def get_landing_content():
    """
    Render landing page content using HTML template
    """
    current_time = datetime.now().strftime("%B %d, %Y")
    return render_template("landing_page.html", current_time=current_time)

def get_quick_stats():
    """
    Get quick stats for dashboard
    """
    return {
        'total_currencies': 180,
        'update_frequency': 'Real-time',
        'accuracy': '99.9%',
        'uptime': '24/7'
    }