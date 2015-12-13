def serialize_ticket(number_list):
    return ",".join(map(str, sorted(map(int, number_list))))
