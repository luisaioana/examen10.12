from Domain.Validator import Validator
from Repository.Repository import Repository
from Service.Service import Service
from UI.UI import UI

repository = Repository('statistics.txt')
validator = Validator()
service = Service(repository, validator)
ui = UI(service)

if __name__ == '__main__':
    ui.run()