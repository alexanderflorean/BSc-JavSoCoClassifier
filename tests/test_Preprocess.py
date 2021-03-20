import regex
import pathmagic
# from nltk.tokenize import RegexpTokenizer
with pathmagic.context():
    from Preprocess import DataExtractor
    from Preprocess import Parser
#    from Preprocess import Preprocess

test_input_filename = 'test_data.java'

"""     Test class DataExtractor        """


def test_DataExtractor_extract_library_rows():
    test_input = get_test_input()
    rule = r'(?=import\s)(\w*.*)(?=;)'
    expected_result = regex.findall(rule, test_input)

    de = DataExtractor()
    de.set_raw_data(test_input)
    result = de.extract_library_rows()
    assert result == expected_result


def test_DataExtractor_extract_package_rows():
    test_input = get_test_input()
    rule = r'(?=package\s)(\w*.*)(?=;)'
    expected_result = regex.findall(rule, test_input)

    de = DataExtractor()
    de.set_raw_data(test_input)
    result = de.extract_package_rows()
    assert result == expected_result


def test_DataExtractor_extract_comments():
    test_input = get_test_input()
    expected_result = []
    regex_line_comments = r'((?<=\/\/\s*).*)'
    regex_row_comments = r'((?<=\/\*)[\s\S]+?(?=\*\/))'
    tmp = regex.findall(regex_line_comments, test_input)
    expected_result.extend(tmp)
    tmp = regex.findall(regex_row_comments, test_input)
    expected_result.extend(tmp)

    de = DataExtractor()
    de.set_raw_data(test_input)
    result = de.extract_comments()
    assert result == expected_result


def test_DataExtractor_extract_classes():
    test_input = get_test_input()
    expected_result = []
    rule_class_declaration = r'(?<=class\s).*?(?=[\s]*{)'
    rule_class_objects = r'(?<=public\s)\w+(?=.*\()'
    rule_new_object_calls = r'(?<=new\s)\w+(?=\()'
    rule_private_class_objects = r'(?<=private\s).*(?=\s\w+;|\s\w+\s=)'

    tmp = regex.findall(rule_class_declaration, test_input)
    expected_result.extend(tmp)
    tmp = regex.findall(rule_class_objects, test_input)
    expected_result.extend(tmp)
    tmp = regex.findall(rule_new_object_calls, test_input)
    expected_result.extend(tmp)
    tmp = regex.findall(rule_private_class_objects, test_input)
    expected_result.extend(tmp)

    de = DataExtractor()
    de.set_raw_data(test_input)
    result = de.extract_classes()
    assert result == expected_result


def test_DataExtractor_extract_public_functions():
    test_input = get_test_input()
    expected_result = []
    rule_1 = r'(?<=public\s.*)\w+(?=\()'
    rule_2 = r'(?<=\.).*?(?=\()'

    tmp = regex.findall(rule_1, test_input)
    expected_result.extend(tmp)
    tmp = regex.findall(rule_2, test_input)
    expected_result.extend(tmp)

    de = DataExtractor()
    de.set_raw_data(test_input)
    result = de.extract_public_functions()
    assert result == expected_result


"""     Test class Parser       """


def test_Parser_tokenize_words_and_characters():
    test_input = "@Override \n public boolean makeChange(BasePanel panel,BibDatabase secondary, NamedCompound undoEdit) { \n if (onDisk == null) {"

    expected_result = ['@', 'Override', 'public', 'boolean', 'makeChange', '(', 'BasePanel', 'panel', ',', 'BibDatabase', 'secondary', ',', 'NamedCompound', 'undoEdit', ')', '{', 'if', '(', 'onDisk', '==', 'null', ')', '{']
    parser = Parser()
    parser.tokenize_words_and_characters(test_input)
    assert parser.get_parsed_data() == expected_result


def test_Parser_tokenize_everything_from_parsed_data():
    test_input = [
        "@Override \n public boolean makeChange(BasePanel ",
        " panel,BibDatabase secondary, NamedCompound undoEdit) { \n ",
        "if (onDisk == null) {",
    ]

    expected_result = ['@', 'Override', 'public', 'boolean', 'makeChange', '(', 'BasePanel', 'panel', ',', 'BibDatabase', 'secondary', ',', 'NamedCompound', 'undoEdit', ')', '{', 'if', '(', 'onDisk', '==', 'null', ')', '{']

    parser = Parser(test_input)
    parser.tokenize_everything_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_tokenize_only_words():
    test_input = "Eighty-seven miles_to go, yet.  OnWard! No.Stopping.here"
    expected_result = ['Eighty', 'seven', 'miles_to', 'go', 'yet', 'OnWard', 'No', 'Stopping', 'here']

    parser = Parser([])
    parser.tokenize_only_words(test_input)
    assert parser.get_parsed_data() == expected_result


def test_Parser_remove_java_keywords_from_parsed_data():
    test_input = [
        "import",
        "sf.sp",
        "program",
        "package",
        "if",
        "its",
        "true",
        "return",
        "falsehopes",
    ]
    expected_result = [
        "sf.sp",
        "program",
        "its",
        "falsehopes",
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.remove_java_keywords_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_single_characters_from_parsed_data():
    test_input = [
        "package",
        "net",
        ".",
        "collab",
        ";",
        "function",
        "(",
        "c",
        ")",
        "}",
    ]
    expected_result = [
        "package",
        "net",
        "collab",
        "function",
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.remove_single_characters_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_remove_numeric_items_from_parsed_data():
    test_input = [
        "23",
        "import",
        "sp.sf.collab",
        "variable3",
        ";",
        "num14",
        "1",
        ".",
    ]
    expected_result = [
        "import",
        "sp.sf.collab",
        "variable3",
        ";",
        "num14",
        ".",
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.remove_numeric_items_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_remove_stopwords_from_parsed_data():
    test_input = [
        'import',
        'sf.sp',
        'program',
        'package',
        'if',
        'its',
        'true',
        'return',
        'falsehopes',
        'at',
        'how',
        'will'
    ]
    expected_result = [
        'import',
        'sf.sp',
        'program',
        'package',
        'true',
        'return',
        'falsehopes'
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.remove_stopwords_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_separate_compound_strings_from_parsed_data():
    test_input = [
        'EntryChange',
        'LogFactory',
        'isModifiedLocally',
        'memEntry',
        'getFieldNames',
        'alltogether',
        'weather',
        'Logger',
        'JComponent',
        'POISX',
    ]
    expected_result = [
        'Entry',
        'Change',
        'Log',
        'Factory',
        'is',
        'Modified',
        'Locally',
        'mem',
        'Entry',
        'get',
        'Field',
        'Names',
        'alltogether',
        'weather',
        'Logger',
        'JComponent',
        'POISX',
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.separate_compound_words_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_lower_case_parsed_data():
    test_input = [
        'EntryChange',
        'LogFactory',
        'isModifiedLocally',
        'memEntry',
        'getFieldNames',
        'alltogether',
        'weather',
        'Logger',
        'JComponent',
    ]
    expected_result = [
        'entrychange',
        'logfactory',
        'ismodifiedlocally',
        'mementry',
        'getfieldnames',
        'alltogether',
        'weather',
        'logger',
        'jcomponent',
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.lower_case_parsed_data()
    assert parser.get_parsed_data() == expected_result


def test_Parser_stem_words_from_parsed_data():
    test_input = [
        'It',
        'is',
        'important',
        'to',
        'by',
        'very',
        'pythonly',
        'while',
        'you',
        'are',
        'pythoning',
        'with',
        'python',
        '.',
        'All',
        'pythoners',
        'have',
        'pythoned',
        'poorly',
        'at',
        'least',
        'once',
        '.',
    ]

    expected_result = [
        'It',
        'is',
        'import',
        'to',
        'by',
        'veri',
        'pythonli',
        'while',
        'you',
        'are',
        'python',
        'with',
        'python',
        '.',
        'all',
        'python',
        'have',
        'python',
        'poorli',
        'at',
        'least',
        'onc',
        '.',
    ]

    parser = Parser()
    parser.set_data(test_input)
    parser.stem_words_from_parsed_data()
    assert parser.get_parsed_data() == expected_result


def get_test_input(size=-1):
    with open('../tests/' + test_input_filename) as f:
        test_input = f.read(size)
    return test_input
