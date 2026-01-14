"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from importlib.metadata import metadata

project_metadata = metadata("imsosorry")
project: str = project_metadata["Name"]
release: str = project_metadata["Version"]
REPO_LINK: str = project_metadata["Project-URL"].replace("repository, ", "")
copyright: str = "Let's build a ..."  # noqa: A001
author: str = "Let's build a ... community"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.linkcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "releases",
]

autoapi_type: str = "python"
autoapi_dirs: list[str] = ["../../src"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Add any paths that contain templates here, relative to this directory.
templates_path: list[str] = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme: str = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list[str] = ["_static"]

releases_github_path = REPO_LINK.removeprefix("https://github.com/")
releases_release_uri = f"{REPO_LINK}/releases/tag/v%s"


def linkcode_resolve(domain: str, info: dict) -> str | None:
    """linkcode_resolve."""
    if domain != "py":
        return None
    if not info["module"]:
        return None

    import importlib  # noqa: PLC0415
    import inspect  # noqa: PLC0415
    import types  # noqa: PLC0415

    mod = importlib.import_module(info["module"])

    val = mod
    for k in info["fullname"].split("."):
        val = getattr(val, k, None)
        if val is None:
            break

    filename = info["module"].replace(".", "/") + ".py"

    if isinstance(
        val,
        (
            types.ModuleType,
            types.MethodType,
            types.FunctionType,
            types.TracebackType,
            types.FrameType,
            types.CodeType,
        ),
    ):
        try:
            lines, first = inspect.getsourcelines(val)
            last = first + len(lines) - 1
            filename += f"#L{first}-L{last}"
        except (OSError, TypeError):
            pass

    return f"{REPO_LINK}/blob/main/src/{filename}"
