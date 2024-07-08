from abhishek.config_schemas.config_schema import Config
from abhishek.utils.config_utils import get_config
from abhishek.utils.data_utils import initialize_dvc
# , initialize_dvc_storage, make_new_data_version


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    initialize_dvc()


if __name__ == "__main__":
    version_data()  
