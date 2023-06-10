import os
from git import Repo
import time
from decouple import config
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp
import asyncio

local_repo_directory = os.path.join(os.getcwd(), "Curso-Python-102")
destination="master"

def clone_repo():
  if os.path.exists(local_repo_directory):
      print("Directory exitst, pulling changes from main branch")
      repo=Repo(local_repo_directory)
      origin=repo.remotes.origin
      origin.pull(destination)
  else:
    print("Directory does not exitst, cloning repository")
    Repo.clone_from("https://github.com/Jin7850/Curso-Python-102.git", local_repo_directory, branch=destination)

def chdirectory(path):
  os.chdir(path)

def create_branch(repo, branch_name):
  current=repo.create_head(branch_name)
  current.checkout

def update_file():
  print("Modifyinh the file")
  chdirectory(local_repo_directory)
  opened_file = open("file.txt",'a')
  opened_file.write("{0} added at {1} \n".format("I am a new string", str(time.time())))

   
def add_and_commit_changes(repo):
  print("Committing changes")
  repo.git.add(update=True)
  repo.git.commit("-m", "Adding a new line to the file.text file")

def push_changes(repo,branch_name):
  print("Push changes")
  repo.git.push("--set-upstream","origin", branch_name)

def main():
  repo=Repo.init(local_repo_directory)
  branch_name="feature/update-txt-file"+str(time.time())
  clone_repo()

  create_branch(repo,branch_name)
  update_file()
  add_and_commit_changes(repo)
  push_changes(repo)



if __name__=="__main__":
  main()