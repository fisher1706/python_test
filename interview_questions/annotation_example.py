def check_passwd(
        username: str,
        password: str,
        min_length: int = 8,
        check_username: bool = True
) -> bool:
    pass


if __name__ == "__main__":
    print(check_passwd.__annotations__)
