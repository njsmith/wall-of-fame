from github import Github
import attr
from pathlib import Path

KEY = (Path(__file__).parent / "github-key.txt").read_text().strip()

@attr.s(frozen=True)
class Hero:
    login = attr.ib()
    name = attr.ib(cmp=False)
    avatar_url = attr.ib(cmp=False)

def get_heroes(org_name, exclude_forks=True, exclude_repos=[]):
    heroes = set()

    g = Github(KEY)
    for repo in g.get_organization(org_name).get_repos():
        print("--", repo.name, "--")
        if repo.name in exclude_repos:
            print("(skipping b/c of exclude list)")
            continue
        if exclude_forks and repo.fork:
            print("(skipping because it's a fork)")
            continue
        for hero in repo.get_contributors():
            print(hero.login)
            heroes.add(Hero(hero.login, hero.name, hero.avatar_url))

    return heroes
