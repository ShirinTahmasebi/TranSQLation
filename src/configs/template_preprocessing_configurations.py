from utils.config_key_data_constants import CONFIG_KEYS_DATA
from utils.contants import CONSTANTS
from imports import *
import sys
sys.path.append('../')

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
    CONFIG_KEYS_DATA.TEMPLATES_LIST_PATH_ALL: CONSTANTS.DATA_DIR_SDSS_ALL_TEMPLATES_LIST,
    CONFIG_KEYS_DATA.TEMPLATES_LIST_PATH_INTERSECTION: CONSTANTS.DATA_DIR_SDSS_INTERSECTION_TEMPLATES_LIST
}


config_sdss_input_creation_train = {
    CONFIG_KEYS_DATA.TEMPLATE_LABELED_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_LABELED,
    CONFIG_KEYS_DATA.TEMPLATE_INPUT_SIMPLE_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_INPUT_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_INPUT_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_INPUT_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_1_SIMPLE_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_MASKED_TASK_1_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_1_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_MASKED_TASK_1_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_1_SIMPLE_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_TOKENIZED_TASK_1_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_1_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_TOKENIZED_TASK_1_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_2_SIMPLE_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_MASKED_TASK_2_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_2_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_MASKED_TASK_2_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_2_SIMPLE_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_TOKENIZED_TASK_1_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_2_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TRAIN_SDSS_TEMPLATE_TOKENIZED_TASK_2_PROMPT_V1,
    CONFIG_KEYS_DATA.TOKENIZER: BertTokenizer.from_pretrained(CONSTANTS.BERT_MODEL_BERT_UNCASED),
}


config_sdss_input_creation_test = {
    CONFIG_KEYS_DATA.TEMPLATE_LABELED_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_LABELED,
    CONFIG_KEYS_DATA.TEMPLATE_INPUT_SIMPLE_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_INPUT_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_INPUT_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_INPUT_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_1_SIMPLE_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_MASKED_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_MASKED_TASK_1_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_MASKED_PROMPT_V1,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_1_SIMPLE_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_TOKENIZED_SIMPLE,
    CONFIG_KEYS_DATA.TEMPLATE_TOKENIZED_TASK_1_PROMPT_V1_PATH: CONSTANTS.DATA_DIR_TEST_SDSS_TEMPLATE_TOKENIZED_PROMPT_V1,
    CONFIG_KEYS_DATA.TOKENIZER: BertTokenizer.from_pretrained(CONSTANTS.BERT_MODEL_BERT_UNCASED),
}
