from models import OfficeModel
from flask_sqlalchemy import sqlalchemy
from config import db
import uuid

class OfficeActions():
# Table actions:
    @classmethod
    def create(cls, usa_state: str, office_code: str):
        new_office = OfficeModel(usa_state=usa_state, office_code=office_code)
        db.session.add(new_office)
        db.session.commit()
        return new_office

    @ classmethod
    def delete(cls):
        OfficeModel.query.delete()
        db.session.commit()

    @ classmethod
    def get_offices(cls):
        offices = OfficeModel.query.all()
        return [
            {"usa_state": office.usa_state,
             "office_code": office.office_code
            } 
          for office in offices]

    @ classmethod
    def get_by_code(cls, office_code: str):
        return OfficeModel.query.filter(OfficeModel.office_code == office_code).first()

    @ classmethod
    def update_office(cls, uuid, usa_state, office_number , office_code):
        office = cls.get_office_by_uuid(uuid)
        office.office_number = office_number
        office.usa_state = usa_state
        office.office_code = office_code 
        db.session.commit()
        return office
     
