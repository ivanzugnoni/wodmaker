from rest_framework import pagination


class BasePagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 1200
    max_page_number = 1000
    page_size_query_param = "page_size"


class Pagination(BasePagination):
    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param)
        if page_size and page_size.lower() == "none":
            return None
        return super().get_page_size(request)
