# Flask Game Website

- This is a Flask-based website that hosts a game where users can play and share their thoughts about the game. User's play time for accomplish the goal will be recorded by the server and will list 10 fastest records.

## Structure

- **Blueprint**
  - **auth.py**: Contains routes for login, registration, and sending verification codes.
  - **Form.py**: Validates form input.
  - **Forum.py**: Routes to and contains functions for the forum page.

- **Static**: Contains Bootstrap, jQuery, and CSS files.
- **Templates**: Contains HTML files using Jinja templating.
- **venv**: Virtual Environment.
- **Instance**: SQLite database file.
- **Migration**: Database migrations.
- **app.py**: Flask configuration, SQLAlchemy configuration, and cookie session management.
- **config.py**: Configuration for verification forwarding.
- **decor.py**: Contains decorators to redirect unregistered users to the login page.
- **exts.py**: Prevents reference loops.
- **models.py**: Contains database models (ORM).

## Function
- When host as a server, the server can generate random verification code and send to the registors.
- Users can post and reply posts to the froum (**BEWARE**:no censorship).
- Users can search post by using keywords.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Set up the database: `flask db upgrade`
3. Run the Flask application: `flask run`

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.


## Acknowledgement

- The game is made following the Unity2d game guide from Udemy: Complete C# Unity Game Developer 2D
- The networking of the data from Unity WebGL is helped and implemented by ChatGPT.
