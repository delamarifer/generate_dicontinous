import glob
from pathlib import Path


for fn in Path("looped/").glob("*"):
    file_base_name = "_".join(fn.stem.split("_")[:-1])
    print(file_base_name)
    file_count = len(glob.glob1("Images", f"{file_base_name}*"))
    if file_count > 1 or Path(file_base_name).is_dir():
        outdir = Path("Images") / file_base_name
        outdir.mkdir(exist_ok=True)
        # fn.rename(outdir / fn.name)