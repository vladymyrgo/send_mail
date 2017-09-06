mails = {
}


avoid_list = {
}


final_set = mails.difference(avoid_list)

FINAL_LIST = sorted(final_set)  # IMPORTANT. It returns ordered list (because set is not ordered)
