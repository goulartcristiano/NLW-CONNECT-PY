from abc import ABC, abstractcmethod
from src.model.entities.eventos import Eventos


#CLASSE ABSTRATA NÃO PODE TER OBJETOS
class EventosRepositoryInterface(ABC):
    @abstractcmethod
    def insert(self, event_name: str) -> None: pass
    
    @abstractcmethod       
    def select_event(self, event_name: str) -> Eventos: pass