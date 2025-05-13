import functools

AUTHORIZED_USERS = {"admin": {"train_model", "load_dataset"},  # actions allowed per role
                    "guest": {"generate_motion"}}

def requires_permission(action: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = get_current_user()  # assume this retrieves the current user's identity and role
            role = user.role
            if action not in AUTHORIZED_USERS.get(role, {}):
                raise PermissionError(f"User '{user.name}' lacks permission for {action}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage: protect a training function so only admins can run it
@requires_permission("train_model")
def run_training(cfg):
    ...  # existing training code (only runs if permission check passes)

# Example usage: requiring a token for accessing generation API
def generate_motion(prompt, token):
    expected_token = os.getenv("API_TOKEN")
    if token != expected_token:
        raise PermissionError("Invalid API token provided!")
    ...  # proceed to sanitize prompt and generate motion
