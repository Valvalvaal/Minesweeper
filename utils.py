import settings

# Calculate the height of frames based on wanted percentages


def height_pct(percentage):
    return (settings.HEIGHT / 100) * percentage


def width_pct(percentage):
    return (settings.WIDTH / 100) * percentage


def select_difficulty():
    """
    TODO #2 Implement function to select a predetermined
    difficulty level or a custom one.
    """
    pass
