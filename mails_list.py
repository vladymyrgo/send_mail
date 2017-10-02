mails = set()


avoid_list = set()


final_set = mails.difference(avoid_list)

FINAL_LIST = sorted(final_set)  # IMPORTANT. It returns ordered list (because set is not ordered)

FINAL_LIST = [[mail] for mail in FINAL_LIST]
