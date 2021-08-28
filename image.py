import pygame


def slice_and_assemble(image_name, button_size, slice_size, final_size):
    image = pygame.image.load(image_name)
    final_images = []

    buttons = slice_image(image, button_size)
    for button in buttons:
        slices = slice_image(button, slice_size)
        final_images.append(assemble_image(slices, final_size))

    return final_images


def slice_image(image, slice_size):
    slices = []
    rect = image.get_rect()

    for y in range(0, rect.height, slice_size[1]):
        for x in range(0, rect.width, slice_size[0]):
            slices.append(image.subsurface((x, y), slice_size))

    return slices


def assemble_image(slices, final_size):
    surface = pygame.Surface(final_size, pygame.SRCALPHA)

    slice_width = slices[0].get_width()
    slice_height = slices[0].get_height()

    # TOP LEFT
    surface.blit(slices[0], (0, 0))

    # TOP MIDDLE
    part = pygame.transform.scale(slices[1], (final_size[0] - 2 * slice_width, slice_height))
    surface.blit(part, (slice_width, 0))

    # TOP RIGHT
    surface.blit(slices[2], (final_size[0] - slice_width, 0))

    # MIDDLE LEFT
    part = pygame.transform.scale(slices[3], (slice_width, final_size[1] - 2 * slice_height))
    surface.blit(part, (0, slice_height))

    # MIDDLE
    part = pygame.transform.scale(slices[4], (final_size[0] - 2 * slice_width, final_size[1] - 2 * slice_height))
    surface.blit(part, (slice_width, slice_height))

    # MIDDLE RIGHT
    part = pygame.transform.scale(slices[5], (slice_width, final_size[1] - 2 * slice_height))
    surface.blit(part, (final_size[0] - slice_width, slice_height))

    # BOTTOM LEFT
    surface.blit(slices[6], (0, final_size[1] - slice_height))

    # BOTTOM MIDDLE
    part = pygame.transform.scale(slices[7], (final_size[0] - 2 * slice_width, slice_height))
    surface.blit(part, (slice_width, final_size[1] - slice_height))

    # BOTTOM RIGHT
    surface.blit(slices[8], (final_size[0] - slice_width, final_size[1] - slice_height))

    return surface
