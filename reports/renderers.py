from rest_framework.renderers import BaseRenderer


class DocxFileRenderer(BaseRenderer):
    media_type = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    format = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    charset = None
    render_style = "binary"

    def render(self, data, media_type=None, renderer_context=None):
        return data
