# https://www.youtube.com/watch?v=nuwb1mBd7J4&list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD&index=5


def adv_deco(password):
    def adv_deco_inner(my_class):
        def inner(*args, **kwargs):
            if password != "zapel":
                print("Error!")
                raise ValueError("Bad password")
            else:
                print("message")
            return my_class(*args, **kwargs)

        return inner

    return adv_deco_inner


@adv_deco(password="zapel")
class MyClass:
    pass


if __name__ == "__main__":
    obj = MyClass()
