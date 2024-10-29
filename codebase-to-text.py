from datetime import datetime
import shutil
import sys
import git
import os
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def clone(repo_url: str, workdir: str):
  if not os.path.exists(workdir):
    os.makedirs(workdir)

  try:
    git.Repo.clone_from(repo_url, workdir)
    logger.info(f"Repository cloned to {workdir}")
  except Exception as e:
    logger.info(f"An error occurred while cloning the repository: {e}")


def walk_repo(outfile: str, workdir: str):
  with open(outfile, 'w+') as f:
    for root, _, files in os.walk(workdir):
      for name in files:
        file_path = os.path.join(root, name)
        try:
          with open(file_path, 'r') as file_content:
            f.write(f"\n\n--- {file_path} ---\n\n")
            f.write(file_content.read())
        except Exception as e:
          logger.info(f"An error occurred while reading the file {file_path}, skipping...")


def run(repo_url: str):
  workdir = './tmp'
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  outfile = f'./out/{repo_url.split("/")[-1].split(".")[0]}-{timestamp}.txt'
  clone(repo_url, workdir)
  walk_repo(outfile, workdir)
  shutil.rmtree(workdir)


if __name__ == '__main__':
  repo_url = sys.argv[1]
  flags = sys.argv[2:]
  run(repo_url, flags)