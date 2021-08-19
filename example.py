#!/usr/bin/env python
from gslocalizator.string_file import SaveFormat
from gslocalizator import GoogleSheetLocalizator as GSLr
from cfg import *


def request_ios(gslr: GSLr):
    gslr.reset()
    gslr.tran(
        from_sheet_range='bizA!A1:E',
        with_key_column='key',
        from_value_column_to_file={
            'zh-Hans': '.datas/ios/strings_biz_a/zh-Hans.lproj/Localizable.strings',
            'zh-Hant': '.datas/ios/strings_biz_a/zh-Hant.lproj/Localizable.strings',
            'en': '.datas/ios/strings_biz_a/en.lproj/Localizable.strings',
            'ja': '.datas/ios/strings_biz_a/ja.lproj/Localizable.strings',
        },
        exclude_headers=['//']
    ).tran(
        from_sheet_range='main!A1:E',
        with_key_column='iOS（IM）Key',
        from_value_column_to_file={
            'zh-Hans': '.datas/ios/strings_main/zh-Hans.lproj/Localizable.strings',
            'zh-Hant': '.datas/ios/strings_main/zh-Hant.lproj/Localizable.strings',
            'en': '.datas/ios/strings_main/en.lproj/Localizable.strings',
            'ja': '.datas/ios/strings_main/ja.lproj/Localizable.strings',
        },
        exclude_headers=['//']
    ).request(
    ).save(format=SaveFormat.iOS)


def request_android(gslr: GSLr):
    gslr.reset()
    gslr.tran(
        from_sheet_range='bizA!A1:E',
        with_key_column='key',
        from_value_column_to_file={
            'zh-Hans': '.datas/android/strings_biz_a/values-zh-rCN/strings.xml',
            'zh-Hant': '.datas/android/strings_biz_a/values-zh-rTWj/strings.xml',
            'en': '.datas/android/strings_biz_a/values/strings.xml',
            'ja': '.datas/android/strings_biz_a/values-ja-rJP/strings.xml',
        },
        exclude_headers=['//']
    ).tran(
        from_sheet_range='main!A1:E',
        with_key_column='iOS（IM）Key',
        from_value_column_to_file={
            'zh-Hans': '.datas/android/strings_main/values-zh-rCN/strings.xml',
            'zh-Hant': '.datas/android/strings_main/values-zh-rTWj/strings.xml',
            'en': '.datas/android/strings_main/values/strings.xml',
            'ja': '.datas/android/strings_main/values-ja-rJP/strings.xml',
        },
        exclude_headers=['//']
    ).request(
    ).save(format=SaveFormat.Android)


def request_flutter(gslr: GSLr):
    gslr.reset()
    gslr.tran(
        from_sheet_range='bizA!A1:E',
        with_key_column='key',
        from_value_column_to_file={
            'zh-Hans': '.datas/flutter/strings_biz_a/intl_zh_CN.arb',
            'zh-Hant': '.datas/flutter/strings_biz_a/intl_zh_TW.arb',
            'en': '.datas/flutter/strings_biz_a/intl_en.arb',
            'ja': '.datas/flutter/strings_biz_a/intl_ja.arb',
        },
        exclude_headers=['//']
    ).tran(
        from_sheet_range='main!A1:E',
        with_key_column='iOS（IM）Key',
        from_value_column_to_file={
            'zh-Hans': '.datas/flutter/strings_main/intl_zh_CN.arb',
            'zh-Hant': '.datas/flutter/strings_main/intl_zh_TW.arb',
            'en': '.datas/flutter/strings_main/intl_en.arb',
            'ja': '.datas/flutter/strings_main/intl_ja.arb',
        },
        exclude_headers=['//']
    ).request(
    ).save(format=SaveFormat.Flutter)


def main():
    with GSLr(GSL_CREDS_FILE, GSL_SPREADSHEET_ID) as gslr:
        request_ios(gslr)
        request_android(gslr)
        request_flutter(gslr)


if __name__ == '__main__':
    main()
