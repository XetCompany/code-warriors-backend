from .request.views import RequestListOrDetailModelViewSet, RequestCreateOrUpdateModelViewSet
from .request.views import add_response_to_request, delete_request_by_pk, end_request, get_requests_by_user_id

from .user.views import user_info

from .files.views import ImageView, VideoView

from .categories.views import get_categories
