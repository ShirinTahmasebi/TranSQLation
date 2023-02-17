from utils.config_key_data_constants import CONFIG_KEYS_DATA
from utils.utils import *

config_sdss_templatization = {
    CONFIG_KEYS_DATA.ALL_DATA_PATHS: [
        {
            CONFIG_KEYS_DATA.NAME: 'SDSS - Train',
            CONFIG_KEYS_DATA.RAW_DATA_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_RAW,
            CONFIG_KEYS_DATA.TEMPLATIZED_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATIEZED,
            CONFIG_KEYS_DATA.TEMPLATE_LABELED_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_LABELED,
        },
        {
            CONFIG_KEYS_DATA.NAME: 'SDSS - Test',
            CONFIG_KEYS_DATA.RAW_DATA_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_RAW,
            CONFIG_KEYS_DATA.TEMPLATIZED_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATIEZED,
            CONFIG_KEYS_DATA.TEMPLATE_LABELED_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_LABELED,
        },
        {
            CONFIG_KEYS_DATA.NAME: 'SDSS - Validation',
            CONFIG_KEYS_DATA.RAW_DATA_PATH: CONSTANTS.DATA_DIR_VAL_SDSS_RAW,
            CONFIG_KEYS_DATA.TEMPLATIZED_PATH: CONSTANTS.DATA_DIR_VAL_SDSS_TEMPLATIEZED,
            CONFIG_KEYS_DATA.TEMPLATE_LABELED_PATH: CONSTANTS.DATA_DIR_VAL_SDSS_TEMPLATE_LABELED,
        }
    ],
    CONFIG_KEYS_DATA.TEMPLATES_LIST_PATH: CONSTANTS.DATA_DIR_SDSS_TEMPLATES_LIST
}