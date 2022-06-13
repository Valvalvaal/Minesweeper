import settings

# Calculate the height of frames based on wanted percentages


def height_pct(percentage):
    return (settings.HEIGHT / 100) * percentage


def width_pct(percentage):
    return (settings.WIDTH / 100) * percentage
