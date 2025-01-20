from faker  import Faker
from models import db, Product, Service
from app import app

# Initialize Faker
faker = Faker()

def seed_products(num=10):
    """Seed the database with fake products."""
    for _ in range(num):
        product = Product(
            name=faker.unique.word().capitalize(),
            category_name=faker.word(),
            subcategory_name=faker.word(),
            description=faker.sentence(),
            price=round(faker.random.uniform(10, 1000), 2),
            image_url=faker.image_url(),
            clicks=faker.random.randint(0, 100)
        )
        db.session.add(product)
    db.session.commit()
    print(f"Seeded {num} products.")

def seed_services(num=10):
    """Seed the database with fake services."""
    for _ in range(num):
        service = Service(
            name=faker.unique.word().capitalize(),
            description=faker.sentence(),
            price=round(faker.random.uniform(20, 500), 2),
            category_name=faker.word(),
            subcategory_name=faker.word(),
            service_img=faker.image_url(),
            clicks=faker.random.randint(0, 100)
        )
        db.session.add(service)
    db.session.commit()
    print(f"Seeded {num} services.")

if __name__ == "__main__":
    # Example usage: Call these functions after initializing the database
    with app.app_context():
        seed_products(15)  # Seed 15 products
        seed_services(15)  # Seed 15 services
