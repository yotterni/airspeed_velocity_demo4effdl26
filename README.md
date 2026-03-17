# Airspeed velocity demo

A short demonstration of [`airspeed_velocity`](https://github.com/airspeed-velocity/asv) for YSDA EffDL'26 final seminar.

## What is this tool?
In brief, `airspeed_velocity` (`asv`) is a `pytest` for the code performance. But with web ui and ability to compare peak memory and speed through the commit history.

You will probably get intereseted after viewing the [deployed `numpy` benchmark demo](https://pv.github.io/numpy-bench/) from `asv` creators.

## Setup 

Clone the repo:

```bash
git clone https://github.com/yotterni/airspeed_velocity_demo4effdl26.git
```

If you still don't have `uv` on your machine, install via:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
(check astral [docs](https://docs.astral.sh/uv/getting-started/installation/)  for more information).

Finally, do the sweet part:

```bash
cd airspeed_velocity_demo4effdl26
uv sync
```

The rest is inside the `asvelocity_demo.ipynb`. Have a 


## References
- [`uv`](https://docs.astral.sh/uv/)
- [`airspeed_velocity`](https://github.com/airspeed-velocity/asv)
- `asv` [docs](https://asv.readthedocs.io/en/latest/)
- a good [video](https://youtu.be/OsxJ5O6h8s0?si=zkhi4-qYzyfjmGlP) from 2014 - not for getting bored by viewing the legacy frontend, but for the clear explanation of the author's phylosophy
- a YT [video](https://www.youtube.com/watch?v=edLQ8KRpupQ) with benchmarking `scipy` via `asv`