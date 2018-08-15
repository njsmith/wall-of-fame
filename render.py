import pickle

with open("trio-heroes.pickle", "rb") as f:
    heroes = pickle.load(f)

heroes = sorted(heroes, key=lambda hero: hero.login.lower())

heroes = [hero for hero in heroes if hero.login != "njsmith"]

with open("trio-heroes.html", "w") as f:
    f.write("""
    <html>
    <meta charset="utf-8">
    <link href="./style.css" rel="stylesheet">
    <body>
    """)
    for hero in heroes:
        def render_name(name):
            if name is None:
                return "&nbsp;"
            else:
                return name

        f.write("""
        <div class="hero">
          <img class="avatar" src="{hero.avatar_url}">
          <span class="login">@{hero.login}</span>
          <span class="name">{name}</span>
        </div>
        """.format(hero=hero, name=render_name(hero.name)))
    f.write("""
    </body>
    </html>
    """)
