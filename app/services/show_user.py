from app.services.genetate_user import generate_users


def show_users():
    users = generate_users(100)
    for user in users:
        print(f'Name: {user.name}, Email: {user.email}')
