import random


class LoadBalancer:
    def __init__(self):
        self.servers_list = []
        self.servers_index = {}
        self.count = 0

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """

    def add(self, server_id):
        if server_id in self.servers_index:
            return
        self.servers_index[server_id] = self.count
        self.servers_list.append(server_id)
        self.count += 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """

    def remove(self, server_id):
        if server_id not in self.servers_index:
            return None
        index = self.servers_index[server_id]
        del self.servers_index[server_id]
        self.servers_list[index] = self.servers_list[-1]
        self.servers_index[self.servers_list[index]] = index
        self.servers_list.pop()
        self.count -= 1

    """
    @return: pick a server in the cluster randomly with equal probability
    """

    def pick(self):
        return self.servers_list[random.randint(0, self.count - 1)]
