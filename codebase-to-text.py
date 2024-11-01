import argparse
from datetime import datetime
import shutil
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
    logger.error(f"An error occurred while cloning the repository: {e}")


def walk_repo(outfile: str, workdir: str, args):
  extensions = args.extensions.split(",")
  with open(outfile, 'w+') as f:
    for root, _, files in os.walk(workdir):
      for name in files:
        if extensions and not any(name.endswith(ext) for ext in extensions): continue
        file_path = os.path.join(root, name)
        if args.subdir and not file_path.startswith(f'./tmp/{args.subdir}'): continue
        logger.info(f'File {file_path} included')
        try:
          with open(file_path, 'r') as file_content:
            f.write(f"\n\n--- {file_path} ---\n\n")
            f.write(file_content.read())
        except Exception as e:
          logger.error(f"An error occurred while reading the file {file_path}, skipping...")


def format_outfile(repo_url: str, outdir: str) -> str:
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  name = "-".join(repo_url.split("/")[-2:]).split(".")[0]
  return f'./{outdir}/{name}-{timestamp}.txt'


def run(args):
  workdir = './tmp'
  clone(args.repo_url, workdir)
  walk_repo(
    outfile=format_outfile(args.repo_url, args.outdir), 
    workdir=workdir, 
    args=args
  )
  shutil.rmtree(workdir)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Clone a Git repo and process its contents.")
  parser.add_argument('repo_url', type=str, help='The URL of the repository to clone')
  parser.add_argument('--extensions', '-e', type=str, default='', help='Comma separated extensions to include in final output')
  parser.add_argument('--subdir', '-s', type=str, default='', help='Choose a subdirectory to copy from the repo')
  parser.add_argument('--outdir', '-o', type=str, default='out', help='Choose where the output contents shall be placed')
  run(parser.parse_args())