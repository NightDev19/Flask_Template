from App import App
if __name__ == '__main__':
    App = App('App')
    app = App.create_app()

    with app.app_context():
        App.db.create_all()
    app.run(debug=True)
