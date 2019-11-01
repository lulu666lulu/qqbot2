'''
更新日期：2019-10-01
本文件配置公主连接Re:dive的相关游戏数据
'''



class _PriconneData(object):
    CHARA = {   # id: [台服官译简体, 常见别称, 带错别字别称]
        1000: ["未知"],
        1001: ["日和", "猫拳"],
        1002: ["优衣", "种田", "普田", "由衣", "结衣"],
        1003: ["怜", "剑圣", "普怜", "伶"],
        1004: ["禊", "炸弹人"],
        1005: ["茉莉", "跳跳虎", "老虎"],
        1006: ["茜里", "妹法"],
        1007: ["宫子", "布丁"],
        1008: ["雪", "小雪", "镜子", "伪娘", "男孩子", "男孩纸"],
        1009: ["杏奈", "中二", "煤气罐"],
        1010: ["真步", "狐狸", "真扎", "maho", "MAHO", "咕噜灵波"],
        1011: ["璃乃", "妹弓"],
        1012: ["初音", "hego", "星法", "星星法"],
        1013: ["七七香", "娜娜卡", "77k", "77香", "nanaka"],
        1014: ["霞", "侦探", "杜宾犬", "驴", "驴子"],
        1015: ["美里", "圣母"],
        1016: ["铃奈", "暴击弓", "暴弓", "爆击弓", "爆弓", "政委"],
        1017: ["香织", "狗子", "狗", "狗拳"],
        1018: ["伊绪", "老师", "魅魔"],

        1020: ["美美", "兔子", "兔兔", "萝卜霸断剑", "人参霸断剑", "天兔霸断剑"],
        1021: ["胡桃", "铃铛"],
        1022: ["依里", "姐法", "姐姐法"],
        1023: ["绫音", "熊锤"],

        1025: ["铃莓", "女仆", "妹抖"],
        1026: ["铃", "松鼠"],
        1027: ["惠理子", "病娇"],
        1028: ["咲恋", "充电宝", "青梅竹马", "幼驯染", "院长", "园长"],
        1029: ["望", "偶像", "小望"],
        1030: ["妮诺", "扇子"],
        1031: ["忍", "普忍", "鬼父"],
        1032: ["秋乃", "哈哈剑"],
        1033: ["真阳", "奶牛"],
        1034: ["优花梨", "黄骑", "酒鬼", "奶骑"],

        1036: ["镜华", "小仓唯", "xcw", "小苍唯", "8岁", "八岁", "喷水萝", "八岁喷水萝", "8岁喷水萝"],
        1037: ["智", "卜毛", "tomo"],
        1038: ["栞", "tp弓", "TP弓", "小栞", "白虎弓", "白虎妹"],

        1040: ["碧", "香菜", "香菜弓", "绿毛弓", "毒弓"],

        1042: ["千歌", "绿毛奶"],
        1043: ["真琴", "狼"],
        1044: ["伊莉亚", "伊利亚", "伊莉雅", "伊利雅", "yly"],
        1045: ["空花", "抖m", "抖M"],
        1046: ["珠希", "猫剑"],
        1047: ["纯", "黑骑", "saber", "SABER"],
        1048: ["美冬", "子龙", "赵子龙"],
        1049: ["静流", "姐姐"],
        1050: ["美咲", "大眼"],
        1051: ["深月", "眼罩", "抖s", "抖S"],
        1052: ["莉玛", "草泥马", "羊驼"],
        1053: ["莫妮卡", "毛二力"],
        1054: ["纺希", "裁缝"],
        1055: ["步未", "路人", "路人妹"],
        1056: ["流夏", "大姐", "大姐头"],
        1057: ["吉塔", "团长", "吉他"],
        1058: ["贪吃佩可", "吃货", "佩可", "公主"],
        1059: ["可可萝", "可可罗", "妈", "普白"],
        1060: ["凯留", "黑猫", "臭鼬"],
        1061: ["矛依未", "夏娜", "511", "无意义"],

        1063: ["亚里莎", "鸭梨瞎", "瞎子", "亚里沙", "鸭梨傻", "亚丽莎", "亚莉莎", "瞎子弓"],




        1068: ["拉比林斯达", "迷宫女王", "晶"],
        1069: ["真那", "霸瞳皇帝", "霸瞳", "千里真那"],
        1070: ["似似花", "变貌大妃", "448", "捏捏卡", "neneka"],
        1071: ["克莉丝提娜", "誓约女君", "克总", "女帝", "克"],

        1073: ["拉基拉基", "跳跃王", "垃圾垃圾"],

        1075: ["贪吃佩可(夏日)", "水吃", "水吃货", "水佩可", "水公主", "泳装吃货", "泳装公主", "佩可(夏日)"],
        1076: ["可可萝(夏日)", "水白", "水可", "水可可", "水可可萝", "水可可罗"],
        1077: ["铃莓(夏日)", "水女仆", "水妹抖"],
        1078: ["凯留(夏日)", "水黑", "水黑猫", "水臭鼬", "泳装黑猫", "泳装臭鼬"],
        1079: ["珠希(夏日)", "水猫剑", "水猫"],
        1080: ["美冬(夏日)", "水子龙"],
        1081: ["忍(万圣节)", "万圣忍", "瓜忍"],
        1082: ["宫子(万圣节)", "万圣布丁", "狼丁", "狼布丁"],
        1083: ["美咲(万圣节)", "万圣美咲", "万圣大眼"],
        1084: ["千歌(圣诞节)", "圣诞千歌", "圣千"],
        1085: ["胡桃(圣诞节)", "圣诞胡桃", "圣诞铃铛"],
        1086: ["绫音(圣诞节)", "圣诞熊锤", "蛋锤"],
        1087: ["日和(新年)", "新年日和", "春猫"],
        1088: ["优衣(新年)", "新年优衣", "春田", "新年由衣"],
        1089: ["怜(新年)", "春剑", "春怜", "春伶"],
        1090: ["惠理子(情人节)", "情人节病娇", "恋病", "情病", "恋病娇", "情病娇"],
        1091: ["静流(情人节)", "情人节静流", "情姐", "情人节姐姐"],
        1092: ["安", "胖安", "55kg"],
        1093: ["露"],
        1094: ["古蕾娅", "龙姬", "古雷娅", "古蕾亚", "古雷亚"],
        1095: ["空花(大江户)", "江户空花", "江户抖m", "江M", "江m"],
        1096: ["妮诺(大江户)", "江户扇子", "忍扇"],
        1097: ["雷姆", "蕾姆"],
        1098: ["拉姆"],
        1099: ["爱蜜莉雅", "艾米莉亚", "emt", "EMT"],
        1100: ["铃奈(夏日)", "瀑击弓", "水爆", "水爆弓", "水暴", "水暴弓", "泳装暴弓", "泳装爆弓"],
        1101: ["伊绪(夏日)", "水魅魔", "水老师", "泳装魅魔", "泳装老师"],
        1102: ["美咲(夏日)", "水大眼", "泳装大眼"],
        1103: ["咲恋(夏日)", "水电", "泳装充电宝", "泳装咲恋", "水着咲恋", "水电站", "水电宝"],
        1104: ["真琴(夏日)", "水狼", "浪"],
        1105: ["香织(夏日)", "水狗", "泃"],
        1106: ["真步(夏日)", "水狐狸", "水真步", "水maho"],
        1107: ["碧(编入生)", "生菜", "新香菜"],
        1108: ["クロエ", "华哥"],
        1109: ["チエル", "切露", "茄露", "茄噜", "切噜"],
        1110: ["ユニ"],
        1111: ["镜华(万圣节)", "万圣镜华", "万圣小仓唯", "万圣xcw", "猫仓唯", "黑猫仓唯", "猫cw", "猫唯", "猫仓", "喵唯"],
        1112: ["禊(万圣节)", "万圣炸弹人", "瓜炸弹人"],
        1113: ["美美(万圣节)", "ミミ（ハロウィン）", "万圣兔子", "万圣兔兔", "绷带兔", "绷带兔子", "万圣美美", "绷带美美"],
    }
