
### Quick Start
```py
#!/usr/bin/env python
from gslocalizator import GoogleSheetLocalizator as GSLr
from cfg import *


def main():
    with GSLr(GSL_CREDS_FILE, GSL_SPREADSHEET_ID) as gslr:
        gslr.tran(
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
        ).save(format="iOS")


if __name__ == '__main__':
    main()
```

## cell formater

Cell formater used to format cells in the spreadsheet.

for example:

title of key| title of lang1|title of lang2|...
-----|-----|-----|-----
Hello|Hello|您好|hhhh
world|world|世界|wwww

key_formater  only be used to cells that under "title of key".

![key_formater area](docs/key_formater_area.png)

You can custom your formater for keys and cells
```py
def cell_fmter(val: str) -> str:
    return re.sub("\s+", " ", val).strip().replace("%s", "%@").replace("\"", "\\\"")


def key_fmter(val: str) -> str:
    return re.sub("\s+", " ", val).strip().replace("%s", "%@")


def load():
    # ...
    with GSLr(GSL_CREDS_FILE, GSL_SPREADSHEET_ID) as gslr:
        gslr.tran(
            from_sheet_range='bizA!A1:F',
            with_key_column='key',
            from_value_column_to_file={
                'zh-Hans': '.datas/ios/strings_biz_a/zh-Hans.lproj/Localizable.strings',
                'zh-Hant': '.datas/ios/strings_biz_a/zh-Hant.lproj/Localizable.strings',
                'en': '.datas/ios/strings_biz_a/en.lproj/Localizable.strings',
                'ja': '.datas/ios/strings_biz_a/ja.lproj/Localizable.strings',
            },
            exclude_headers=['//'],
            cell_formater=cell_fmter
        ).request(
        ).save(format="iOS")
    # ...
```