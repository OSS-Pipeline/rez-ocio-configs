name = "ocio_configs"

version = "master"

authors = [
    "Sony Pictures Imageworks",
    "Foundry",
    "Academy of Motion Picture Arts and Sciences"
]

description = \
    """
    Color Configurations for OpenColorIO.
    """

requires = [
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "ocio-{version}".format(version=str(version))

def commands():
    # Helper environment variables.
    # Paths to the existing OCIO configurations.
    env.OCIO_CONFIGS_ACES_0_1_1_PATH.set("{root}/aces_0.1.1/config.ocio")
    env.OCIO_CONFIGS_ACES_0_7_1_PATH.set("{root}/aces_0.7.1/config.ocio")
    env.OCIO_CONFIGS_ACES_1_0_1_PATH.set("{root}/aces_1.0.1/config.ocio")
    env.OCIO_CONFIGS_ACES_1_0_2_PATH.set("{root}/aces_1.0.2/config.ocio")
    env.OCIO_CONFIGS_ACES_1_0_3_PATH.set("{root}/aces_1.0.3/config.ocio")
    env.OCIO_CONFIGS_NUKE_DEFAULT_PATH.set("{root}/nuke-default/config.ocio")
    env.OCIO_CONFIGS_SPI_ANIM_PATH.set("{root}/spi-anim/config.ocio")
    env.OCIO_CONFIGS_SPI_VFX_PATH.set("{root}/spi-vfx/config.ocio")

    # We setup a default one, here ACES 1.0.3
    env.OCIO_CONFIGS_DEFAULT.set(str(env.OCIO_CONFIGS_ACES_1_0_3_PATH))

    # We set the OCIO environment variable to the same value as OCIO_CONFIGS_DEFAULT.
    env.OCIO.set(str(env.OCIO_CONFIGS_DEFAULT))
