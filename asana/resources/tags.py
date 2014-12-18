# This file is automatically generated by generate.py using api.json

class Tags:
    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher

    def create(self, params={}):
        return self.dispatcher.post('/tags', params)

    def update(self, tag_id, params={}):
        path = '/tags/%d' % (tag_id)
        return self.dispatcher.put(path, params)

    def find_by_id(self, tag_id, params={}):
        path = '/tags/%d' % (tag_id)
        return self.dispatcher.get(path, params)

    def find_by_workspace(self, workspace_id, params={}):
        path = '/workspaces/%d/tags' % (workspace_id)
        return self.dispatcher.get(path, params)

    def find_all(self, params={}):
        return self.dispatcher.get('/tags', params)

    def create_in_workspace(self, workspace_id, params={}):
        path = '/workspaces/%d/tags' % (workspace_id)
        return self.dispatcher.post(path, params)
