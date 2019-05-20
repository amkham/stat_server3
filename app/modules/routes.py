from flask import render_template, jsonify, Response, json, request
from app import app, db
from .models import Subject, Statistic, Criterion, Location
import wikipedia


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/criterions_get')
def criterions():
    c = Criterion.query.all()
    json_post1 = []
    for crit in c: json_post1.append({
        'id': crit.id,
        'name': crit.name})
    print('Критерии ', json_post1)
    return jsonify(json_post1)


@app.route('/api/subjects_get')
def subject():
    s = Subject.query.all()
    json_post2 = []
    for sub in s: json_post2.append({
        'id': sub.id,
        'name': sub.name
    })
    print('Регионы ', json_post2)
    return jsonify(json_post2)


@app.route('/api/locations_get', methods=['GET', 'POST'])
def location():
    json_get = request.get_json(force=True)
    json_post3 = []
    for sub in json_get:
        location = Location.query.filter_by(regions_id=sub)
        for l in location:
            json_post3.append({
                'id': l.id,
                'location': l.location,
                'date': l.date,
                'value': l.value
            })
    print('Населенные пункты: ', json_post3)
    return jsonify(json_post3)


@app.route('/api/diagram', methods=['GET', 'POST'])
def diagram():
    json_get_filters = request.get_json(force=True)
    diagram_date = []
    s = []
    d = []
    for dig in json_get_filters:
        location2 = Statistic.query.filter_by(locations_id=dig)
        for loc in location2:
            s.append(loc.value)
            d.append(loc.date)
    diagram_date.append({
        'value': s,
        'date': d
    })
    print('значения', diagram_date)
    return jsonify(diagram_date)

@app.route('/api/pageSearche', methods=['GET','POST'])
def pageSeache():
    wikipedia.set_lang("ru")
    print('step1')
    json_locations_information = []
    json_get_pageName = request.get_data()
    print(json_get_pageName)
    wikipage = wikipedia.page(json_get_pageName)
    title = wikipage.original_title
    text = wikipage.summary
    image = wikipage.images
    json_locations_information.append({
        'title': title,
        'text': text,
        'image': image,
    }
    )
    print(json_locations_information)
    return jsonify(json_locations_information)
