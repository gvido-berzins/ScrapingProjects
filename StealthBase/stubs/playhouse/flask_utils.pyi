from _typeshed import Incomplete

class PaginatedQuery:
    paginate_by: Incomplete
    page_var: Incomplete
    page: Incomplete
    check_bounds: Incomplete
    query: Incomplete
    model: Incomplete
    def __init__(self, query_or_model, paginate_by, page_var: str = ..., page: Incomplete | None = ..., check_bounds: bool = ...) -> None: ...
    def get_page(self): ...
    def get_page_count(self): ...
    def get_object_list(self): ...
    def get_page_range(self, page, total, show: int = ...): ...

def get_object_or_404(query_or_model, *query): ...
def object_list(template_name, query, context_variable: str = ..., paginate_by: int = ..., page_var: str = ..., page: Incomplete | None = ..., check_bounds: bool = ..., **kwargs): ...
def get_current_url(): ...
def get_next_url(default: str = ...): ...

class FlaskDB:
    database: Incomplete
    base_model_class: Incomplete
    def __init__(self, app: Incomplete | None = ..., database: Incomplete | None = ..., model_class=..., excluded_routes: Incomplete | None = ...) -> None: ...
    def init_app(self, app) -> None: ...
    def get_model_class(self): ...
    @property
    def Model(self): ...
    def connect_db(self) -> None: ...
    def close_db(self, exc) -> None: ...
