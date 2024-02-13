from find_ft_type import all_thing_is_obj

ft_list = ["Hello, ", "tata"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tuto"}
ft_dict = {"Hello": "tata"}

print(all_thing_is_obj(ft_list))
print(all_thing_is_obj(ft_tuple))
print(all_thing_is_obj(ft_set))
print(all_thing_is_obj(ft_dict))
print(all_thing_is_obj("Brian"))
print(all_thing_is_obj(10))
