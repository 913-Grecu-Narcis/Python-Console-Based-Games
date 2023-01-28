from game_service.game_service import GameService
from repo.repository import Repo
from ui.ui import UI

repo = Repo()
service = GameService(repo)

ui = UI(service)

ui.main_menu()
