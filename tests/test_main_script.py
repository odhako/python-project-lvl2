import pytest
from gendiff.scripts.gendiff_cli import main


def test_main_script():
    with pytest.raises(SystemExit):
        main()
