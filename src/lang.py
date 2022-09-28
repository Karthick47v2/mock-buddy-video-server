import language_tool_python


class LangChecker:
    def __init__(self, corpus):
        self.__lang_tool = language_tool_python.LanguageTool('en-US')
        self.__disabled_rules = ['ARROWS', 'WHITESPACE_RULE', 'EN_COMPOUNDS']
        self.__mistake = []
        self.__mistake_exp = []
        self.__top3_suggestions = []

        self.__analyze_txt(corpus)

        self.__lang_tool.close()

    def __append_error(self, rule, mistake, mistake_exp, suggestions):
        if len(rule.replacements) > 0 and rule.ruleId not in self.__disabled_rules:
            if rule.context[rule.offset: rule.offset + 1].isalnum():
                mistake.append(
                    rule.context[rule.offset: rule.errorLength + rule.offset])
                mistake_exp.append(rule.message)
                suggestions.append(rule.replacements[:3])

    def __analyze_txt(self, corpus):
        for slide_txt in corpus:
            slide_mistake = []
            slide_mistake_exp = []
            slide_top3_suggestions = []

            for txt in slide_txt:
                if len(txt) > 2:
                    predict = self.__lang_tool.check(txt)
                    for rule in predict:
                        self.__append_error(
                            rule, slide_mistake, slide_mistake_exp, slide_top3_suggestions)

            if len(slide_mistake) > 0:
                self.__mistake.append(slide_mistake)
                self.__mistake_exp.append(slide_mistake_exp)
                self.__top3_suggestions.append(slide_top3_suggestions)

    def get_results(self):
        return self.__mistake, self.__mistake_exp, self.__top3_suggestions
