from repository.file_repository import FileRepo
from service.game_service import Service
from ui.ui import UI

file_repo = FileRepo('sentences.txt')
service = Service(file_repo)
ui = UI(service)

ui.main_menu()
