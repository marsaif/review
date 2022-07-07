

from modules import Review , session


def add_review(review : Review) -> int :
    session.add(review)
    session.commit()
    return review.id

def delete_review_by_id(id) -> None : 
    session.query(Review).filter(Review.id==id).delete()
    session.commit()

def approve_review_by_id(id) -> None : 
    review = session.query(Review).filter(Review.id==id).first()
    review.published = True
    session.commit()

def get_reviews() :
    reviews = session.query(Review).filter(Review.published==True).all()
    return reviews

def get_review_by_id(id) :
    review = session.query(Review).filter(Review.id==id).first()
    return review

def update_review2() : 
    session.commit()