"""spelling and grammer checker"""
import language_tool_python


class LangChecker:
    # pylint: disable=too-few-public-methods
    """Class for spelling and grammer checking"""

    def __init__(self, corpus):
        """Initialize checker.

        Args:
            corpus (listlist((str))): input text.
        """
        self.__lang_tool = language_tool_python.LanguageTool('en-US')
        self.__disabled_rules = ['ARROWS', 'WHITESPACE_RULE', 'EN_COMPOUNDS']

        self.__suggestions = []

        self.__analyze_txt(corpus)

        self.__lang_tool.close()

    def __append_error(self, rule, suggestions, idx):
        """Add mistake and it info to list.

        Args:
            rule (dict[str,str]): dictionary of mistake's details.
            suggestions (list(dict[str, str])): list of rules.
            idx (int): slide no (starting from 0).
        """
        if len(rule.replacements) > 0 and rule.ruleId not in self.__disabled_rules:
            if rule.context[rule.offset: rule.offset + 1].isalnum():
                suggestions.append({
                    "mistake":
                    rule.context[rule.offset: rule.errorLength + rule.offset],
                    "exp": rule.message,
                    "top3": rule.replacements[:3],
                    "id": idx + 1})

    def __analyze_txt(self, corpus):
        """Iterate through text and find errors.

        Args:
            corpus (listlist((str))): input text.
        """
        for idx, slide_txt in enumerate(corpus):
            slide_suggestions = []

            for txt in slide_txt:
                if len(txt) > 2:
                    predict = self.__lang_tool.check(txt)
                    for rule in predict:
                        self.__append_error(
                            rule, slide_suggestions, idx)

            if len(slide_suggestions) > 0:
                self.__suggestions.append(slide_suggestions)

    def get_results(self):
        """Return collected errors and its suggestions.

        Returns:
            list(list(dict[str, str])): list of rules for each slide.
        """
        return self.__suggestions
