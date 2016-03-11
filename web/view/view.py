from flask import render_template, request, abort, session

class normalView():
    template_path = "dashboard.html"

    @classmethod
    def get(self):
        return self.render(self.template_path)

    @classmethod
    def post(self):
        return self.render(self.template_path)

    @classmethod
    def error(self):
        abort(404)

    @classmethod
    def as_view(self):
        if request.method == 'GET':
            return self.get()
        elif request.method == 'POST':
            return self.post()
        else:
            return self.error()

    @classmethod
    def render(self, *args, **kwargs):
        self.mysession = dict(session)
        kwargs['mysession'] = self.mysession
        return render_template(*args, **kwargs)
