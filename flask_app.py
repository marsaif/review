
import json
from flask import Flask, jsonify , render_template, request
from ReviewCrud import add_review, approve_review_by_id, delete_review_by_id, get_review_by_id, get_reviews, update_review2

from modules import Review, Serializer
app = Flask(__name__)

@app.route('/')
def review():
    return render_template('review.html')

@app.route('/share',methods = ['POST'])
def share():
    review = Review()
    review.first_name = request.form['first_name']
    review.last_name = request.form['last_name']
    review.email = request.form['email']
    review.review_title = request.form['review-title']
    review.review = request.form['review']
    review.service = request.form['service']
    review.job = request.form['job']
    review.post_code = request.form['post-code']
    review.phone_number = request.form['phone-number']
    id = add_review(review)
    return render_template('share_review.html',id=id)

@app.route('/delete_review/<id>',methods = ['GET'])
def delete_review(id):
     delete_review_by_id(id)
     return {'response' : 'deleted'}
    
@app.route('/approve_review/<id>',methods = ['GET'])
def approve_review(id):
     approve_review_by_id(id)
     return {'response' : 'approved'}

@app.route('/reviews',methods = ['GET'])
def show_reviews() : 
    reviews = get_reviews()
    return render_template('reviews.html',reviews=reviews)

@app.route('/show/<id>',methods = ['GET'])
def show_review(id) : 
    review = get_review_by_id(id)
    return render_template('show_review.html',review=review)

@app.route('/delete/<id>',methods = ['GET'])
def delete_review2(id) : 
    delete_review_by_id(id)
    reviews = get_reviews()
    return render_template('reviews.html',reviews=reviews)

@app.route('/modify/<id>',methods = ['GET'])
def modify_review(id) : 
    review = get_review_by_id(id)
    return render_template('modify_review.html',review=review)

@app.route('/update_review',methods = ['POST'])
def update_review() :
    review = get_review_by_id(request.form['id'])
    review.first_name = request.form['first_name']
    review.last_name = request.form['last_name']
    review.email = request.form['email']
    review.review_title = request.form['review-title']
    review.review = request.form['review']
    review.service = request.form['service']
    review.job = request.form['job']
    review.post_code = request.form['post-code']
    review.phone_number = request.form['phone-number']
    update_review2()
    reviews = get_reviews()
    return render_template('reviews.html',reviews=reviews)

@app.route('/revs',methods = ['GET'])
def get_reviews_json():
    reviews = get_reviews()
    return json.dumps(Serializer.serialize_list(reviews))


