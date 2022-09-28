from urllib.error import HTTPError
from urllib import request
from pptx import Presentation
from collections import Counter


class Slide:
    __PPTX_NAME = 'test.pptx'

    def __init__(self, url):
        self.__url = url.split('/')
        self.__url[-1] = 'export/pptx'
        self.__url = '/'.join(self.__url)

        self.__txt_lst = []
        self.__word_count = []
        self.__shape_count = 0
        self.__slide_count = 0
        self.__font_lst = []

        self.__load_pptx()

    def __load_pptx(self):
        try:
            request.urlretrieve(self.__url, Slide.__PPTX_NAME)
        except HTTPError:
            return{
                'stauts': 400
            }

    def __set_slide_count(self, slides):
        self.__slide_count = len(slides)

    def __extract_txt(self, runs, word_count, txt):
        for run in runs:
            if (run.font.name is not None):
                self.__font_lst.append(run.font.name)

            word_count.append(
                len(run.text.split(' ')))
            txt.append(run.text)

    def __increment_shape_count(self, type):
        if type == 13 or type == 6:
            self.__shape_count += 1

    def extract_pptx(self):
        with open(Slide.__PPTX_NAME, 'rb') as pptx:
            prs = Presentation(pptx)
            self.__set_slide_count(prs.slides)

            for slide in prs.slides:
                slide_txt_lst = []
                slide_word_count = []

                for shape in slide.shapes:
                    if shape.has_text_frame:
                        for para in shape.text_frame.paragraphs:
                            self.__extract_txt(
                                para.runs, slide_word_count, slide_txt_lst)
                    self.__increment_shape_count(shape.shape_type)

                self.__txt_lst.append(slide_txt_lst)
                self.__word_count.append(slide_word_count)

    def get_txt(self):
        return self.__txt_lst

    def get_data(self):
        return self.__slide_count, self.__word_count, self.__shape_count, dict(Counter(self.__font_lst))
