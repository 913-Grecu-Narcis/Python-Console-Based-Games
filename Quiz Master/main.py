from business.service import Service
from infrastructure.file_repo import FileRepo
from presentation.ui import UI

repo = FileRepo()
service = Service(repo)
ui = UI(service)

ui.main_menu()
