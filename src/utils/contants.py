## For creating constant variables (public static final variables)
# https://stackoverflow.com/a/2688086

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Contants(object):
    
    @constant
    def IS_ROBERTA():
        return True
    
    @constant
    def BERT_MODEL_BERT_CASED():
        return "bert-base-cased"
    
    @constant
    def BERT_MODEL_BERT_UNCASED():
        return "bert-base-uncased"
    
    @constant
    def BERT_MODEL_CODEBERT():
        return "microsoft/codebert-base"
    
    @constant
    def BERT_MODEL_CODE_BERT():
        if Contants.IS_ROBERTA.__get__(0):
            return "microsoft/codebert-base"

    # TODO Shirin: Revise all the uses!
    @constant
    def BERT_MODEL_NAME():
        return Contants.BERT_MODEL_CODE_BERT.__get__(0)

    @constant
    def MAX_TOKEN_COUNT():
        return 512
    
    @constant
    def NUMBER_OF_EPOCHS():
        return 2
    
    # Optimizer parameters
    @constant
    def LEARNING_RATE():
        return 2e-5

    @constant
    def NUMBER_OF_WARM_UP_STEPS():
        return 5

    @constant
    def DATA_DIR_TRAIN_RAW():
        return 'data/processed_data/train/basic.csv'
    
    @constant
    def DATA_DIR_TRAIN_WITH_CLS():
        return 'data/processed_data/train/with_cls.csv'

    @constant
    def DATA_DIR_TRAIN_TOKENIZED_BERT():
        return 'data/processed_data/train/tokenized_bert.csv'

    @constant
    def DATA_DIR_TRAIN_TOKENIZED_CODEBERT():
        return 'data/processed_data/train/tokenized_codebert.csv'

    @constant
    def DATA_DIR_TEST_RAW():
        return 'data/processed_data/test/basic.csv'
    
    @constant
    def DATA_DIR_TEST_WITH_CLS():
        return 'data/processed_data/test/with_cls.csv'

    @constant
    def DATA_DIR_TEST_TOKENIZED_BERT():
        return 'data/processed_data/test/tokenized_bert.csv'

    @constant
    def DATA_DIR_TEST_TOKENIZED_CODEBERT():
        return 'data/processed_data/test/tokenized_codebert.csv'

    @constant
    def DATA_DIR_VAL_RAW():
        return 'data/processed_data/val/basic.csv'
    
    @constant
    def DATA_DIR_VAL_WITH_CLS():
        return 'data/processed_data/val/with_cls.csv'

    
    @constant
    def DATA_DIR_VAL_TOKENIZED_BERT():
        return 'data/processed_data/val/tokenized_bert.csv'

    @constant
    def DATA_DIR_VAL_TOKENIZED_CODEBERT():
        return 'data/processed_data/val/tokenized_codebert.csv'
    
    @constant
    def TABLE_TYPE_ID():
        return 100

    @constant
    def ATTRIBUTE_TYPE_ID():
        return 200

    @constant
    def FUNCTION_TYPE_ID():
        return 300

    ## Define the constants here!

CONSTANTS = Contants()