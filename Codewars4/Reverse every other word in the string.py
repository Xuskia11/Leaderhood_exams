def reverse_alternate(st):
    st = st.split()
    lists = []
    for i in range(len(st)):
        if i % 2 == 1:
            lists.append(st[i][::-1])
        else:
            lists.append(st[i])
    return " ".join(lists)

