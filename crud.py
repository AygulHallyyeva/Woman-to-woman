from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, and_
from models import Employee, Employer, employerImages, employeeImages
from sqlalchemy import func, or_
from upload_depends import upload_image


def create_employee(req, db: Session):
    employee = db.query(Employee).filter(
        or_(
            Employee.first_name == req.first_name,
            Employee.last_name == req.last_name,
            Employee.email == req.email,
            Employee.phone_number == req.phone_number,
            Employee.required == req.required
        )
    ).first()
    new_add = Employee(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True


def read_employee(db: Session):
    result = db.query(
        Employee, 
    ).options(joinedload(Employee.images).load_only('img')).all()
    return result


def delete_employee(id, db: Session):
    db.query(employeeImages).filter(employeeImages.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    new_delete = db.query(Employee).filter(Employee.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    return True


def search_employee(q, db: Session):
    result = db.query(Employee)\
        .filter(
            or_(
                func.lower(Employee.first_name).like(f'%{q}%'),
                func.lower(Employee.last_name).like(f'%{q}%'),
            )
        ).all()
    return result


def create_employer(req, db: Session):
    employer = db.query(Employer).filter(
        or_(
            Employer.first_name == req.first_name,
            Employer.last_name == req.last_name,
            Employer.email == req.email,
            Employer.phone_number == req.phone_number,
            Employer.required == req.required
        )
    ).first()
    new_add = Employer(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True


def read_employer(db: Session):
    result = db.query(
        Employer,
    ).options(joinedload(Employer.image).load_only('img')).all()
    return result


def delete_employer(id, db: Session):
    db.query(employerImages).filter(employerImages.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    new_delete = db.query(Employer).filter(Employer.id == id)\
        .delete(synchronize_session=False)
    db.commit()
    return True


def search_employer(q, db: Session):
    result = db.query(Employer)\
        .filter(
            or_(
                func.lower(Employer.first_name).like(f'%{q}%'),
                func.lower(Employer.last_name).like(f'%{q}%'),
            )
        ).all()
    return result


def create_employer_image(id, file, db: Session):
    upload_image_name = upload_image('profile', file)
    new_add = employerImages(
        img = upload_image_name,
        employer_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def create_employee_image(id, file, db: Session):
    upload_image_name = upload_image('profile', file)
    new_add = employeeImages(
        img = upload_image_name,
        employee_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add