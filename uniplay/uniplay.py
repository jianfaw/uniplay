"""TO-DO: Write a description of what this XBlock is."""
# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from django.template import Context, Template


class UniPlayerXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    display_name = String(default='Universal Player', scope=Scope.content, help='video name')
    play_url = String(
        default='<embed src="http://static.video.qq.com/TPout.swf?vid=l0019lkpy23&auto=0" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>',
        scope=Scope.content, help='video link')

    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the UniPlayerXBlock, shown to students
        when viewing courses.
        """
        context = {
            'display_name': self.display_name,
            'play_url': self.play_url,
        }
        html = self.render_template("public/html/uniplay_view.html", context)
        frag = Fragment(html.format(self=self))
        frag.add_css(self.load_resource("public/css/uniplay.css"))
        frag.add_javascript(self.load_resource("public/js/src/uniplay_view.js"))
        frag.initialize_js('uniPlayInitView')
        return frag

    def studio_view(self, context=None):
        context = {
            'display_name': self.display_name,
            'play_url': self.play_url,
        }
        html = self.render_template("public/html/uniplay_edit.html", context)
        frag = Fragment(html)
        frag.add_css(self.load_resource("public/css/uniplay.css"))
        frag.add_javascript(self.load_resource("public/js/src/uniplay_edit.js"))
        frag.initialize_js('uniPlayInitEdit')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_video(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        # assert data['hello'] == 'world'

        self.display_name = data['display_name']
        self.play_url = data['play_url']
        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [("UniPlayerXBlock", "<uniplay/>")]
