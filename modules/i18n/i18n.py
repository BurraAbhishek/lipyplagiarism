import gettext

localedir = './locale'

translate = gettext.translation('appname', localedir, fallback=True)
i18n = translate.gettext