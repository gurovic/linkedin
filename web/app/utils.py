from datetime import datetime

COUNTRY_CHOICES = [
    ('RU', 'Russian Federation'),
    ('US', 'United States'),
    ('CA', 'Canada'),
    ('GB', 'United Kingdom'),
    ('DE', 'Germany'),
    ('FR', 'France'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
]

def get_year():
    return datetime.now().year