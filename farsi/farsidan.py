from hazm import *
import sqlite3
import re


chunker_model = r"models\chunker.model"
pos_tagger_model = r"models\pos_tagger.model"


def translate_pos_tags_to_persian(tag_list):
    translation_dict = {
        'PRON': 'فاعل',
        'ADP': 'حرف اضافه',
        'VERB': 'فعل',
        'PUNCT': 'علامت‌های نگارشی',
        'EZ': "مضاف الیه",
        'ADJ': 'صفت',
        'CCONJ': 'حرف ربط',
        'NOUN': 'اسم',
        'NOUN,EZ': 'مفعول',
        'ADV': 'قید',

    }

    translated_tags = []

    for word, tag in tag_list[0]:
        if tag in translation_dict:
            translated_tags.append((translation_dict[tag], word))
        else:
            translated_tags.append((tag, word))

    return translated_tags

# در تابع naghsh خود
def naghsh(self):
    self.ui.result_naghsh.clear()
    text = self.ui.lineEdit_naghsh.text()
    try:
        int(text)
    except:
        normalizer = Normalizer()
        normalize_text = normalizer.normalize(text)
        tokenize_text = [word_tokenize(txt) for txt in sent_tokenize(normalize_text)]
        model_path = pos_tagger_model
        tagger = POSTagger(model=model_path)
        token_tag_list = tagger.tag_sents(tokenize_text)

        translated_tags = translate_pos_tags_to_persian(token_tag_list)

        result_text = ""
        for tag, word in translated_tags:
            result_text += f"{tag}:{word}\n"

        self.ui.result_naghsh.setText(result_text)
    def translate_bakhs(tree):
        translation_dict = {
            'NP': 'عبارت اسمی',
            'VP': 'عبارت فعلی',
            'PP': 'عبارت حرف اضافه‌ای',
            'ADVP': 'عبارت قیدی',
            # موارد دیگر اضافه شوند بر اساس نیاز
        }

        for key, value in translation_dict.items():
            tree = tree.replace(f'[{key}', f'[{value}')

        return tree

def bakhsh(self):
    text = self.ui.lineEdit_bakhsh.text()
    try:
        int(text)
    except:
        tagger = POSTagger(model=pos_tagger_model)
        chunker = Chunker(model=chunker_model)
        tagged = tagger.tag(word_tokenize(str(text)))
        result_tree = chunker.parse(tagged)

        output = []

        for subtree in result_tree.subtrees():
            if subtree.label() == 'NP':
                output.append(f"{subtree.leaves()[0][0]}:عبارت اسمی")
            elif subtree.label() == 'VP':
                output.append(f"{subtree.leaves()[0][0]}:عبارت فعلی")
            elif subtree.label() == 'PP':
                output.append(f"{subtree.leaves()[0][0]}:حرف اضافه")
            elif subtree.label() == 'ADVP':
                output.append(f"{subtree.leaves()[0][0]}:عبارت قید")
         

    result = '\n'.join(output)
    self.ui.result_bakhsh.setText(result)

def rishe_fel(self):
    user_input = self.ui.lineEdit_fel.text()
    try:
        int(user_input)
    except:
        word_list = user_input.split(",")
        lemmatizer = Lemmatizer()
        result = []
        for word in word_list:
            output = lemmatizer.lemmatize(word)
            result.append(output)
        result = str(result)
        result = result.replace("[","")
        result = result.replace("]","")
        result = result.replace("'","")
        self.ui.result_fel.setText(result)

def mofrad(self):
    user_input = self.ui.lineEdit_mofrad.text()
    try:
        int(user_input)
    except:
        user_input = self.ui.lineEdit_mofrad.text()
        word_list = user_input.split(",")  
        stemmer = Stemmer()
        result = []
        for word in word_list:
            output = stemmer.stem(word)
            result.append(output)
        result = str(result)
        result = result.replace("[","")
        result = result.replace("]","")
        result = result.replace("'","")
        self.ui.result_mofrad.setText(result)

conn = sqlite3.connect('dic.db')
cursor = conn.cursor()      
def get_meaning(word):
    cursor.execute("SELECT Mean FROM Words WHERE Word=?", (word,))
    meaning = cursor.fetchone()
    if meaning:
        return meaning[0]  # Return the meaning if found
    else:
        return "Meaning not found for '{}'".format(word)


def mani(self):
    user_input = self.ui.lineEdit_mani.text()
    try:
        int(user_input)
    except:
        word_list = user_input.split(",")
        result = ""
        for word in word_list:
            meaning = get_meaning(word)
            result+=meaning
        def remove_content(text):
            text = re.sub(r'\[.*?\]', '', text)
            text = re.sub(r'\(.*?\)', '', text)
            text = re.sub(r'\[|\]', '', text)
            text = re.sub(r'\(|\)', '', text)
            return text
        clean_text = remove_content(result)
        self.ui.result_mani.setText(clean_text)


    