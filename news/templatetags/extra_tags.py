from django import template

register = template.Library()


@register.simple_tag
def access_list(page_obj: list, index: int):
    """
    リストの要素のうち、インデックスで指定した要素を返す
    :param some_list: 要素を取得したいリスト
    :param index: 取得したいリストのインデックス
    :return: 指定したインデックスに格納されているリストの要素
    """
    try:
        result = page_obj[int(index)]
        return result
    except:
        return ""

@register.simple_tag
def access_2d_list(page_obj: list, row_index: int, col_index: int):
    """
    2次元リストの要素のうち、インデックスで指定した要素を返す
    :param some_list: 要素を取得したいリスト
    :param index: 取得したいリストのインデックス
    :return: 指定したインデックスに格納されているリストの要素
    """
    try:
        result = page_obj[int(row_index)][int(col_index)]
        return result
    except:
        return ""