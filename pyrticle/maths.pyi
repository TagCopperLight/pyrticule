"""
This type stub file was generated by pyright.
"""

from . import particle


def fade_color(particle: particle.Particle, color: tuple[int, int, int], progress: float) -> tuple[int, int, int]:
    ...

def fade_alpha(particle: particle.Particle, alpha: int, progress: float) -> int:
    ...

def fade_alpha_exp(particle: particle.Particle, alpha: int, progress: float) -> int:
    ...

