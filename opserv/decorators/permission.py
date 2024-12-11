def require_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Checking permission {permission}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
