"""
    Se for implementar uma aplicação CLI e prints personalizados,
    aperfeiçoar:

    Examples:
        >>> # cli.py
        >>> from rich import print
        >>> from rich.table import Table
        >>> from rich.console import Console
        >>> from typer import Argument, Typer
        >>> [funções que serão utilizadas no CLI]
        >>>
        >>> console = Console()
        >>> app = Typer()
        >>>
        >>> @app.command()
        >>> def funcao_chamada_no_cli(
        >>>     param = Argument('default', help='Explica sobre o argumento')
        >>> ):
        >>>     table = Table()
        >>>     # Uso do typer e rich
        >>>     funcao_importada_para_uso()
        >>>     # Uso do typer e rich

        >>> # test_cli.py
        >>> from typer.testing import CliRunner
        >>> from pjt_pkg_template.cli import app
        >>> from pytest import mark
        >>>
        >>> runner = CliRunner()
        >>>
        >>>
        >>> @mark.parametrize('argumento', [x, y, z])
        >>> def test_configurar_um_teste_para_cli(argumento):
        >>>     resultado = runner.invoke(app)
        >>>     # Se o acerte for igual a 1, está quebrando.
        >>>     # Do contrário, o app invocado do CLI está tudo certo.
        >>>     assert resultado.exit_code == 0
        >>>

        >>> # pyproject.toml
        >>> [tool.poetry.scripts]
        >>> saudacao = 'pjt_pkg_template.cli:checando_cli'
"""
