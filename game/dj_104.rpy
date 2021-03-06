# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: dj_104.rpy
#  description: (story scripts) Dongji Main Story 10.4
#  Story Author: Alan Li, Conway Tan
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dj_104:

label .s38villa:
    scene dj villa sleep with fade
    "中场休息之后，大家又讲了其他的故事。"
    "大家似乎都聊累了，你逐渐发现仍然在说话的人越来越少……"
    play sound sleeping
    conway"呼....呼...."
    "熬到现在感觉大家都坚持不住了。"
    ## Not important
    menu:
        "这时你："
        "大喊：“睡nmb起来嗨！” ":
            $ dunhuang_value += 10
            "你把房间的灯突然打开，惊醒了靡靡的众人。" with Fade(0.1, 0.0, 3.5, color="#fff")

        "我们也休息吧":
            $ dunhuang_value -= 10
            "于是大家各自回到房间去休息了。"
            "躺下之后你还在回忆着刚才大家聊的内容，慢慢进入梦乡..."
            scene black with Fade(2.0, 0.0, 0.1, color="#000")
            jump .s39villa

    "已经困的睁不开眼睛的冠军也应和着："
    conway"大家别睡，起来玩——啊”"
    han"算了，想睡的就睡，不想睡的我们去隔壁吧。"
    play sound sleeping
    "你们来到隔壁的房间，继续聊情感话题，但没聊多久，就又传来呼声，于是大家横七竖八地睡着了...."
    scene black with Fade(2.0, 0.0, 1.5, color="#000")
    jump .s39villa

label .s39villa:
    show text "2018年10月4日" at truecenter with dissolve
    pause 0.5
    image time2 = Text("凌晨4:30", xalign=0.5, yalign=0.55)
    show time2 with dissolve
    pause 1.0

    scene dj villa morning with fade
    play sound alarm_clock
    play music sqh_alarm fadein 2.0
    "随着此起彼伏的闹铃声，你醒了过来。"
    me"啊！！这就四点半了，我刚才梦里还在吃海底捞呢，狗日的冠军又没熟就下筷子！"
    "说着你打醒了睡在旁边的冠军。"
    "大家也陆续起床了。"
    zheng"大家把最厚的衣服都穿上啊"
    nuo"艹我没带厚衣服，小明把你的衣服给我穿"
    han"诺诺你今天总不需要化妆了吧？"
    shou"哈哈哈哈哈哈化妆就不等她了。"
    nuo"不化妆了md就睡了个午觉都没卸"
    stop music fadeout 2.0
    "洗漱完毕，大家前往另外一栋民宿，叫醒昨晚虚掉的壮壮和有容。"

label .s40villa:
    play music happy_1 fadein 2.0
    wqbh"诶，我房间怎么锁着了？"
    me"估计是小茶他们回来了吧。"
    wqbh"那我怎么拿厚衣服啊..."
    me"看看小天是不是在这边？"
    "你们俩走进另外一间房间，发现只有壮壮和有容。"
    me"emmmmm那小天不会是去学妹的房间了吧？"
    ## Not important
    menu:
        "这时你们怎么办？"
        "卧槽刺激啊，还是不打扰他们了":
            $ dunhuang_value -= 10

        "敲敲门问下他们要不要去看日出吧":
            wqbh"emmmmmm我敲敲门试试。"
            play sound knock_door
            "咚咚咚"
            wqbh"不行啊...没人理我"
            me"行吧...估计他们昨晚也挺难受，让他们好好休息吧。"

        "破门而入":
            $ dunhuang_value += 20
            "你一脚踹开了门，发现他俩被你突然惊醒。"
            me"emmmm那个啥...打扰了，你们要去看日出吗？"
            "两人""滚！"
            "你只好退了出来。"

    "于是你们叫醒了壮壮和有容。"
    me"那好像也没办法啊...壮壮你有多的外套吗？"
    zhuang"啥？有个p，冷死我了。"
    yourong"就算我有多的外套，她能当连衣裙了哈哈哈哈。"
    wqbh"算了...我这样也还行吧。"
    "你们走下楼，和大部队会合。"
    jump .s41road

label .s41road:
    scene dj sunrise road with fade
    nuo"累死我了艹为毛一直是上坡啊！"
    conway"看日出肯定得到地势高的地方啊憨憨。"
    yinyin"那诺诺这个身高可能优势不太明显"
    lian"哈哈哈哈我们可以给她做日出直播、文字解说。"
    "路上的人逐渐多起来了，不过都是三三两两的，像我们这样乌压压的一大群并不多见。"
    jump .s42sunrise

label .s42sunrise:
    scene dj sunrise plat1 with fade
    "不知道过了多久，终于到了目的地“观日台”。"
    "这时候竟然已经有挺多人在那里站着了，变成了一道天际线。"

    "登上山顶，远处略有微光，一望无际的都是暗暗的波涛，不时有些许渔船起起伏伏，别有意境。"
    "但...我们这边的画风似乎有点不一样……"

    scene dj sunrise plat2 with dissolve
    dan"艹这妖风也太大了，我都要被吹倒了"
    ming"哈哈哈哈冠军你这围巾包头就跟阿拉伯妇女一样"
    stop music fadeout 2.0
    yinyin"抖抖抖抖"
    zhuang"靠我们报团取暖吧"
    play music dj_island fadein 2.0
    han"来把那个小音响拿出来"
    lian"对对还有桃旗也举起来"
    
    "众人随着小音箱的旋律合唱东极岛之歌，桃旗迎风飘荡："
    "众人""""
    东极岛啊你人杰又地灵，太平洋的风儿最先吹到你
    
    东极岛东极岛，大陆最东的岛屿，海浪都来亲吻你，鱼儿都来拥抱你
    """
    "路人""你们是大学生吗？一起跑出来玩真好！"
    shou"对，我们是高中同学！"
    conway"算起来认识四年多了啊。"
    "众人""冠军快哭！"
    conway"才四年不长不长，哭个p"
    "……"

    scene dj sunrise plat3 with dissolve
    "渐渐的，海边泛起了一丝红色。"
    han"小明你这个手机指南针准不准啊，这咋南边日出呢？"
    ming"我也不晓得啊…"
    wqbh"这你们就不懂了吧？地理学过，北半球日出会偏南一点……"
    zhuang"对对对我也知道，我是地理课代表。"
    dan"不行，我们几个真的得抱着，要不然这个风吹的，真的容易朝后倒。"

    scene dj sunrise plat4 with dissolve
    "不知过了多久，远方泛起的红色越来越多了，但...似乎被一大片云挡住了日出了地方。"
    han"快看那，出来了！"
    nuo"哪哪？我咋没看到？"
    yourong"152的视角偏下，看不到也正常。"
    "众人""哈哈哈哈哈哈……"
    han"骗你的哈哈哈哈"
    nuo"？？？我有155了好吧！"
    lian"这有点不稳啊，离之前查的日出时间已经超了十分钟了。"
    shou"那片云不会一直挡着太阳吧..."
    "……"

    scene dj sunrise plat5 with dissolve
    "又过了快半小时，天也越来越亮了，周围的人纷纷离去。"
    "路人""今天太阳被云遮住了，起这么早太可惜了。"
    "你们也开始认同这种看法。"
    conway"来都来了，我们去海神庙逛逛吧。"
    zhuang"靠，还走路啊，有多远？"
    ming"三公里吧。"
    zhuang"靠我虚了，要睡觉"
    wqbh"你咋这么菜，昨晚不是提前回去睡了吗？"
    han"我也不太行了，昨晚一直都没睡。"
    ## May jump story
    ## AutoSave 2-5
    python:
        renpy.take_screenshot()
        renpy.save("12-5", "去不去后会无期标建？")

    menu:
        "于是众人决定分为两拨，你决定："
        "后会无期标建肯定要去啊！睡觉？睡个p！":
            $ dunhuang_value += 10
            
        "实在是肝不动了，回去睡觉":
            $ dunhuang_value -= 10
            stop music fadeout 2.0
            "你们一行拖着沉重的步伐，好像梦游一般，不知道怎么就回到了民宿，慌不择床的睡下了。"
            jump .s47villa

    "看起来，太阳真的完全被云遮住了，你们放弃了等待，顺着环岛公路朝着海神像的方向而去……"
    jump .s43sun

label .s43sun:
    scene dj sunrise final with dissolve
    "走着走着，突然发现东南方向突然一阵曙光，太阳终于从云层里钻出来了！大家一片欢呼。"
    dan"诺诺你赶紧拍照！"
    shou"对对，顺便修一下我们之后盗图。"
    nuo"？？盗图还这么光明正大？"
    "众人""大樱桃就是没素质哈哈哈哈……"
    play sound take_photo
    scene dj sunrise final with phototake
    stop music fadeout 2.0
    pause 0.5
    scene dj morning road1 with fade
    play music be_ordinary_instrument fadein 2.0
    "拍完照后，你们一路向着海神像而去，环岛小路竟然都是下坡。"
    lian"这种坡不跑起来真的好难受啊。"
    yourong"冲冲冲！"
    conway"走那么快干啥，我要拍年度图呢。"
    shou"谁给你拍你这也太磨叽了。"
    ## Not important
    menu:
        "这时你决定："
        "冲冲冲，冠军拍照太磨叽了，不知道啥时候才能到海神像":
            $ dunhuang_value += 10
            "你和连南兽兽等人冲下了坡，没想到这个坡那么长，根本停不下来。"
            "等到平地停下，才发现后面的人已经看不到踪影，你们决定先去海神像那边等他们。"
            jump .s45seagod

        "走那么快干啥，我也要拍美美的照片":
            jump .s44road

label .s44road:
    scene dj conway1 with dissolve
    "冠军把准备好的桃旗撑了起来，披到身上。"
    "你们站在山崖上，远处是大海。吹着晨风，沐浴着朝阳，你感觉到无比的舒适和惬意。"
    conway"我要这样"
    "……"
    play sound take_photo
    scene dj conway2 with phototake
    conway"不满意，再来"

    play sound take_photo
    scene dj conway3 with phototake
    "……" 
    conway"不行，你这拍的也太丑了。"
    nuo"靠，是人丑好吧，我不给你拍了，狗屎！"
    wqbh"你看看这个呢？"
    conway"诶...我再管理一下表情"
    "……" 
    play sound take_photo
    scene dj conway3 with phototake
    pause 0.5
    scene black with fade

    scene dj morning road2 with fade
    "许久，冠军终于拍完了，他举起桃旗的一角，淫淫、小明他们分别举起桃旗的另一角。"
    me"万千儿，给他们拍张照片！"
    play sound take_photo
    scene dj morning road2 with phototake
    pause 1
    "海风吹得很大，展开的旗子也鼓满了风。大家的头发都被吹得乱七八糟。"
    ming"诶呀呀呀——————卧槽！"
    "风实在是太大了，小明用拿着手机的手抓着旗子，结果一不小心手机被风吹到地上了。他赶快捡起来……"
    "一个大大的裂痕从摄像头延伸到了屏幕边缘。"
    ming"我正准备换新手机，算了算了。"
    "不愧是陈老板，有钱啊。"
    jump .s45seagod

label .s45seagod:
    scene dj seagod1 with fade
    "终于远远望到了海神像。"
    zheng"后会无期中似乎介绍过这个。"
    conway"是传说这是个叫财伯公的是上岛第一人，然后就成了东极岛的守护神。"
    wqbh"你咋记得这么清楚？"
    lian"你们不看看这片子主题曲是什么？"
    xld"什么？"
    ming"冠军金曲啊！不唱一个实在对不起大家。"
    conway"music 起！"
    conway"徘徊着的 在路上的 你要走吗 Via Via"
    conway"易碎的 骄傲着 那也曾是我的模样……"
    "……"

    scene dj seagod2 with fade
    "不知不觉大家走到了财伯公的裙子下面，四面都是一望无际的大海，大家沿着雕像底座坐好。"
    nuo"诶那边有个小姐姐喊她帮我们照个相吧。"
    dan"谁去？"
    ming"那肯定最骚的去啊！"
    "众人""那不就是你了？"
    "于是小明就去了。"
    conway"来大家赶紧凹造型，来个那些年的风格吧"
    shou"哈哈哈哈终于不是沙雕风了"
    "……"
    play sound take_photo
    scene dj seagod2 with phototake

    pause 2
    jump .s46road

label .s46road:
    scene dj seagod back with Fade(2.0, 0.1, 0.8)
    """
    海风吹在脸上，咸咸的，你们沿着小路朝回走，不在乎时间，只在乎旁边的人和他们的笑声。

    路过港口，发现身份证上尚无返程票的信息，但售票处小姐姐说离开船还有很久，这也正常。

    于是你们在海边一家小摊坐下，吃过老板煮的海鲜面，有些许沙子的味道，但也心满意足，回民宿各自休息了。
    """
    stop music fadeout 2.0
    jump .s47villa

label .s47villa:
    scene dj villa noon with Fade(2.0, 1.0, 2.0)
    "不知道睡了多久，你渐渐醒了，看到旁边睡着的壮壮，你决定赶紧拿手机拍下他的睡姿："
    scene dj villa noon with phototake
    play sound take_photo
    zhuang"扫黄了？"
    scene dj villa noon with phototake
    play sound take_photo
    zhuang"我没嫖"
    scene dj villa noon with phototake
    play sound take_photo
    zhuang"她自愿的"
    "……"
    "大家陆陆续续都起来了。"
    "老板娘""看这个天色，感觉台风马上要来了，你们订的那班船是停航之前最后一班了，要是错过就只能和我们一起待岛上咯。"
    dan"不怕！我们这回在群里禁言诺诺就行了。"
    nuo"？？？感到有被冒犯"
    "简单吃过午饭之后，大家收拾行李，准备出发了。"
    jump .s48road

label .s48road:
    scene dj postcard with fade
    play music rain fadein 2.0
    "这时外面乌云密布，狂风大作，原来这就是台风！真的是活久见，大家的伞被吹得东倒西歪，终于快要走到码头了。"
    lian"诶那有个小店好像可以买明信片，我们去看看吧。"
    "老板""大家赶紧看啊，一会我也要坐船走了。"
    lian"老板您这可以寄出吗？"
    "老板""可以啊，但得等我下次回岛，或者我帮你们带到舟山寄也行。"
    lian"不急不急，等您回来寄就好，还是东极岛上寄出来比较有趣。"
    "大家于是决定合买一套，纷纷拿起笔开始写起来。"
    ## Not important
    menu:
        "你是否要寄给在香港的妹妹呢？"
        "那肯定要寄啊，东极岛寄出的多有意思":
            $ dunhuang_value += 10
            "于是你给妹妹也寄了一张明信片，期待着她惊喜的表情。"

        "我买张明信片就行了，之后亲自带给她":
            "于是你买了一张明信片，写完贴上邮票放在包里。"
            jump .s50road

        "算了吧，没必要":
            $ dunhuang_value -= 10
    
    stop music fadeout 2.0
    jump .s49port

label .s49port:
    scene dj port with fade
    "众人离开明信片小店，一路艰难跋涉到港口，这时已经到了检票时间，你们赶忙进入候船厅。"
    play music hostility fadein 2.0
    han"咋回事我身份证又刷不出来票？"
    lian"我靠不会吧？？？"
    shou"这黑心店家还真敢报复我们？"
    "众人面面相觑，你赶紧给店家打电话，然而一直无人接听。"
    zheng"大家别慌，去问下售票处。"
    lian"来统一收下身份证，我们去问问。"

    "售票小姐姐拿过你们的身份证。"
    "小姐姐""这里显示的是你们的船票已经被取出来了，所以单靠身份证刷不出来信息了。"
    me"没有身份证也能取票吗？"
    "小姐姐""订票二维码也可以的。"
    conway"有没有可能查到是什么时候取出来的？"
    "小姐姐""系统里面看不到。"
    me"那现在还有余票吗？"
    "小姐姐""还是有一些的，不过你们要抓紧点，这会台风来袭，大家都在抢着离岛，票余量在不断减少……"
    shou"小姐姐你能再说一遍我们的情况吗？我们好像被黑心黄牛商家坑了，希望能录音做个取证。"
    "……"

    "你们按之前的方法，换了个手机号给老板打电话，果然接通了。"
    "老板""我没取你们的票啊，你们不会是在讹诈我吧？"
    me"谁有闲工夫讹诈你，现在台风来袭，如果我们困在岛上，等回去之后宁这边要担负的责任可能不小啊。"
    "老板""行，我去查查记录吧"
    shou"不要慌，反正还有票，再差也不过是亏点钱的事情。"
    conway"嗯，台风来袭，肯定不会把想走的游客丢在岛上的。"
    lian"再等一会老板的回复吧，实在不行我们就买票。"
    shou"我去跟大家说下现在的情况。"

    scene black with fade
    "距离停止检票时间只有不到二十分钟了，老板仍然没有消息，也不再接你的电话。"
    "……"
    scene black with fade
    "距离停止检票时间只有不到十五分钟了，老板仍然没有消息，换个电话打也无人接通。"
    "……"
    scene black with fade
    "距离停止检票时间只有不到十分钟了，老板仍然没有消息。"
    "你在手机淘宝上给老板发了最后通牒，终于老板回复了，仍一口咬定他们没有取票，是我们在讹诈他……"
    "……"

    scene dj port with fade
    "你们当即决定不再纠缠，去售票处重新购票登船。"
    zheng"怎么少了一个人？"
    "诡异的事情发生了，明明刚才分了两拨，一拨去售票处处理事故，一拨在大厅等候，这……？"
    shou"对了，刚才淫淫说要去给可可寄明信片，这都快半小时了，怎么还不回来，qq语音也不接？"
    lian"我靠，这样吧大家先上船吧，我和冠军去找他。"
    me"我跟你们俩一起去吧。"
    "说着你们三人冲出了大厅，没入大雨之中。"

    scene dj postcard out with fade
    "在这种大雨中根本不可能接收到手机的消息，完全联系不上淫淫啊……"
    "突然间，你好像看到了一个身影从另外一边冲进了大厅，大喊之下，果然是淫淫。"
    "你赶紧朝另外一边追回了朝明信片小店方向跑去的二人，一起检票登船。"
    yinyin"实在抱歉，我回去就发现那个小店已经关门了，在高德上找了下东极岛的邮局，投递到邮筒里面才回来，所以耽误了。" 
    jump .s51port

label .s50road:
    scene dj port with fade
    play music hostility fadein 2.0
    "众人离开明信片小店，一路艰难跋涉到港口。"
    "不行，还是得从东极岛寄给妹妹的明信片才有意义啊，要不然淘宝店岂不是很多。还是回去寄吧。"
    me"兽兽，你们先登船，我去给妹妹寄明信片。"
    shou"行，我跟大家说一声，你快去快回。"

    scene dj postcard out with fade
    "你冲进大雨之中，之前房东送的塑料雨衣在这种暴雨之下毫无用处，却发现之前那家明信片小店已经关闭。"
    me"该死，店主说也要登船离岛的，估计我们刚走他也走了……"
    me"来都来了，记得高德上看的邮局也不远，我直接扔桶里应该就行。赶紧跑过去吧，应该来得及。"
    play sound run_step
    "不知道跑了多久，终于看到了绿色的邮筒，投递成功。"
    "一看手机，发现距离停止登船只有不到十五分钟了，一路冲刺到码头大厅，突然听到有人在喊你，回头一看发现是连南。"
    "你招手之后，他又朝另外一个方向跑去了，你有些奇怪，后来才发现冠军跟他一起回来。"
    me"实在抱歉，我回去就发现那个小店已经关门了，在高德上找了下东极岛的邮局，投递到邮筒里面才回来，所以耽误了。"
    lian"没事没事，赶紧上船吧，马上就要开了。"
    jump .s51port

label .s51port:
    scene dj port board with fade
    """
    检票后准备登船，你们才感受到台风的可怕。

    庞大的船体晃来晃去，登船的踏板随之舞蹈，你感觉自己就跟被两侧的船员一路甩上船的一样。

    一路摸爬滚打终于到了下仓，坐了下来，晃来晃去，你并不知道船是什么时候开的，就睡着了。
    """
    jump .s52ship

label .s52ship:
    scene ship middle with fade
    "迷迷糊糊之间，你感觉自己好像听到隐隐的惊叫声，你清醒过来，发现周围已经没有人了。"
    me"什么玩意，都下船了也不喊我？"
    "船舱依然非常晃荡，你站立不稳，扶着座椅走出船舱，却发现整个船似乎要翻了，海里似乎也有星星点点的人在呼救……"
    scene dream onship with dissolve
    ## Not important
    menu:
        "这时你该怎么办？"
        "我靠，我肯定在做梦吧":
            $ dunhuang_value -= 10
            "就在这时，船剧烈抖动，你被甩过了船舷……"

        "我靠，第一次坐船就遇到海难吗？就算是泰坦尼克号，为啥不给我分配个Rose":
            $ dunhuang_value += 20
            "随着你的臆想，只戴着海洋之心的Rose出现在了你的面前。"
            me"？？？"
            "Rose""You jump, I jump!"
            "随后Rose便跳下了海里，你正在疑惑，却发现自己被一股力量也带了下去……"
            
        "我靠，赶紧拨打110":
            "你竟然打通了110的电话。"
            me"喂？警察叔叔我好怕……"
            "就在这时，船剧烈抖动，你被甩过了船舷……"
    stop music fadeout 2.0
    play sound fall_in_water
    jump .s53sea

label .s53sea:
    scene black with vpunch
    """
    马上就没入水中，你强迫自己睁开眼睛，却怎么也睁不开！

    你在水里挣扎着，突然想起来自己小时候学过游泳，果然很顺利的在水里移动了起来，逐渐不那么慌了。

    但你发现了一件更诡异的事情，不管你怎么游动，你竟然一直在往下沉，而没有浮起来……

    而且，深蓝色的海洋里竟然没有一条鱼。
    """
    scene dream acientship with fade
    play sound terrible_ring fadein 2.0
    """
    不知道过了多久，你回头发现已经完全看不到海平面，耳边突然响起了一阵空灵的铃铛声……

    你朝四周看去，已经置身于一片废墟之中，脚也触到了海底浮动的尘沙。

    惊恐万分，仔细一看，原来这是一艘早已沉没的巨轮，地上散落的都是破损的古老石棺。
    """
    jump .s54grave

label .s54grave:    
    scene dream grave with dissolve
    "与其说是巨轮，不如说它更像是一个海底的古墓。"
    stop sound fadeout 2.0
    "等你意识到这一点，你已经不知不觉来到了一个石棺面前，上面的苔藓遮住了奇怪的花纹。"
    "这时之前的铃铛声却消失了，取代它的是一片死一样的寂静，仿佛整个世界的时间线都停止，除了远处有一排移动着的不明物体，正渐渐走远。"
    ## Not important
    menu:
        "这时你？"
        "我靠，这说不定是救援队啊，快来救救我！":
            $ dunhuang_value += 10
            "随着你嘴里跑出一串气泡，那排移动着的不明物体突然转向朝你飞速而来！" with vpunch
            "大惊之下，你赶快躲到石棺后面，等再站起来看，那些未知的东西已经不知去向。"

        "还是别了，还是静态的东西让人安心，闷声大发财吧":
            $ dunhuang_value -= 10

    play sound undersea fadein 2.0
    "正在你在纠结为什么自己没有窒息而死的时候，你突然听到身旁的石棺不知道为什么已经打开了一条缝，正发出了悉悉簌簌的声响……"
    "好像里面有一双惨白的眼睛正漫不经心地盯着你。"
    "你想大叫，却叫不出声……"
    scene black
    stop sound fadeout 2.0
    pause 1.5
    jump .s55ship

label .s55ship:
    shou"快醒醒，你在叫什么？？？吵死了" with vpunch
    scene ship back with fade
    play music melody_of_night_17 fadein 2.0
    "你清醒过来，发现旁边的兽兽正在嫌弃你。"
    "原来是个梦啊。md肯定盗墓笔记看多了，不过...为什么内心中总有一丝想回到沉船呢？"
    "你看了看表，发现已经睡了三个小时了，船应该也快到舟山了，看到周围东倒西歪的友人，趁机拍下了他们优雅的睡姿。"
    jump .s56port

label .s56port:
    scene zs port back with fade
    "船终于到了舟山，走出来才发现天竟然已经完全黑了，码头的路灯惨淡地发着微弱的光。"
    "下雨的码头是混乱的，夹杂着人群的呼叫，狂风还在刮着人的脸，好在雨下的小了，淅淅沥沥的。"
    zheng"这怎么跟鬼片一样……"
    wqbh"这风刮的好冷啊"
    han"我们先去吃饭吧？"
    lian"要不就去上次购物的那个商城？刚好在那歇歇，再去民宿。"
    ming"那可是个小别墅呢！"
    scene zs mall with fade
    "于是你们分头打车前往商城吃饭，虽说舟山是个小城市，商城人真的巨多，你们十来个人只好分散开再找地方。"
    "吃完饭，果然好多了，之前不舒服的诺诺居然作死一定要吃DQ。"
    me"呵，女人。"
    jump .s57taxi

label .s57taxi:
    scene taxi night with fade
    "从商圈出来，大家分头打出租前往今晚的小别墅，第一次住别墅，你们都有点小兴奋。"
    stop music fadeout 2.0

    scene ghost lost with fade
    "等到下车，才发现司机竟然把你们带到了一个看起来荒无人烟的大路旁边。"
    play music paradise_island fadein 2.0
    wqbh"这是目的地吗？怎么跟我们一起的其他人拍的照不太一样？"
    me"emmmmm高德地图上显示的是这个没错啊……"
    jump .s58lost

label .s58lost:
    "外面确实有些冷清，路灯非常暗淡。"
    "而且最让人诡异的是，周围的小别墅竟然都跟空宅一样，一点也没有生活气息，黑暗的窗户透露着空洞的眼神。"
    "你突然想起了梦里的那个石棺，不禁起了一身鸡皮疙瘩。"
    me"那个...万千你别怕，我们把手电都打开，多说话就没事了。"
    wqbh"我才不怕呢，我看倒是你吓得要死吧哈哈哈哈。"
    lian"桃神你可是神啊，怎么能怕鬼呢？"
    me"……"

    scene ghost lost with fade
    "不多时，你们走着走着却发现有点不太对劲，怎么...这周围的环境跟五分钟前这么像呢？"
    play sound route_replan
    "高德地图雷萌萌版""正在为您重新规划路线……"
    wqbh"这咋一直在重新规划？你会不会带路啊？"
    me"我确实按照规划的路线走的啊...是有点不太对劲...."
    wqbh"靠你别吓我，我还没遇到过鬼打墙"
    "你定了定神，用手电筒好好照了照周围，熟悉的别墅、熟悉的小花园、熟悉的铁栅栏门……"
    lian"你们有谁看过盗墓笔记或者鬼吹灯？"
    wqbh"你闭嘴吧"
    lian"如果遭遇了这种循环，有一个好方法就是留一个人在这看着前面的人走。"
    me"那...谁来做观察的这个人..."
    "你们三个陷入了沉默..."

    wqbh"神经病啊你们，自己吓唬自己，我们跟在别墅的人开个位置共享不就行了，让他们来接我们。"
    me"好有道理！！！"
    "于是你们站在原地等待救援，直到阿郑出现在你们的视野范围内，终于舒了一口气。"
    "但是...你仍然在思考为什么刚才会出现这种情况..."
    "难道是沾了什么不干净的东西？你不禁回忆起当时做的那个梦……"
    stop music fadeout 2.0
    jump .s59villa

label .s59villa:
    scene ghost out with fade
    play music melody_of_night_17 fadein 2.0
    "等到了别墅，你之前的担忧都消失了，果然和伙伴们在一起，就不怕什么了。"
    "大家笑笑闹闹，吵吵嚷嚷地抢浴室，这种气氛之下，就算是鬼也不敢来吧。"
    "你舒了一口气，收拾了下东西，准备去洗澡。"
    lian"太狗屎了，这鬼台风把航班都取消了，我这可咋回去啊……"
    nuo"你要不紧急求助下邱？我每次误车都找他。"
    lian"有道理，不知道这么晚了，还有没有救……"
    "谁叫连老板土豪呢，飞机来回啧啧啧，还是我们坐火车的稳。"
    jump .s60shower

label .s60shower:
    scene ghost shower with fade
    "走进浴室，打开热水，你不禁轻轻哼起了东极岛之歌。"
    "在冷天洗热水澡真是天下第一幸福的事情，唯一的遗憾是这个浴室竟然是个百叶窗，万一有人馋我的身子，在外面偷窥，我这美好的躯体……"
    "突然间，你依稀感觉百叶窗外真的有一双眼睛，还是那双惨白惨白的眼睛。"
    "突然外面传来万千的叫声："
    wqbh"桃神搞快点！你咋这么墨迹，跟诺诺阿姨一样" with vpunch
    "你猛然回过神来……"
    "靠，这个狗屁噩梦，我就别自己吓唬自己了。"
    jump .s61villa

label .s61villa:   
    scene ghost room1 with fade
    "洗漱完毕，你走出浴室，坐到床上玩手机。"
    lian"完蛋了啊，过十一点了，12306都关了……"
    qly"没事你别担心， 我刚看到还有一班K的无座，回去肯定能回去的。"
    lian"无座，杀了我吧5555"
    """
    不知为何，你很想在百度里搜一下东极岛海域的沉船故事，但好像没有什么相关的，却有一条人人网里的消息：“临安，渔阳，东极，沙州，是一个不可言说的秘密。”

    临安是杭州，沙州是敦煌，那渔阳又是哪？

    你很快搜了一下，渔阳竟然是北京的密云区。

    杭州、密云、东极，这不是大樱桃的前三次出行吗？为什么？？？
    
    这不可能啊，没有《后会无期》，就算是游客也不会来东极岛，在十年前为什么有人提到这个地方。

    但这三个地方的组合，好像没有其他的解释了。而且...这个留言和沉船又有什么关系？你陷入了沉思...
    """
    wqbh"你在干什么？这么苦大仇深？不会还在怕鬼吧？"
    me"没有没有，你洗完了？这么快？"
    wqbh"我又不是诺诺，占着浴室就不出来了。"
    me"我问你，杭州，北京，东极岛和敦煌有什么关系吗？"
    wqbh"能有什么关系？天南海北的。"
    me"好吧..."

    conway"大家都洗完了吧，抓紧的，我们来玩樱桃罂粟"
    nuo"靠我不玩，这宅子有点可怕。"
    han"有啥可怕的，就我们几个人，门一锁又没有别人。"
    lian"走走走，去检查下看看光线符不符合条件。"
    me"好，我也来。"
    jump .s62villa

label .s62villa:
    scene ghost livingroom dark with fade
    "你们来到楼下的客厅，把灯都关上之后，发现窗帘效果并不太好。"
    "外面的路灯的光仍然能透进来，达不到玩樱桃罂粟的环境条件。"
    conway"哎太可惜了。"
    zheng"这咋还有个亮的没关上？"
    "果然一个有个暗淡的光源照亮了楼梯的一个角落。"
    lian"？？？我们刚才把所有楼下的灯都关了啊，奇怪了"
    "你们都围了上去。"
    conway"这是小米的智能夜灯吧，可能刚才自动触发了。"
    "你突然发现，这个小夜灯照亮的角落里的装饰花纹，那么的熟悉，但还是想不起来是哪见过。"
    yinyin"算了算了，玩不成了，我们看电影吧。"
    shou"好啊！这个卧室有个智能投影呢！贼爽！"
    "说着众人又回到楼上，你突然意识到，这个花纹，和梦里海底石棺上的，是那么的相似……"
    jump .s63villa

label .s63villa:
    scene ghost room movie with dissolve
    "你心乱如麻，跟着众人来到有投影的那个卧室。众人正叽叽喳喳讨论要看什么。"
    yinyin"这个别墅的氛围感觉很适合看鬼片啊！"
    conway"滚！！！我不要看。"
    dan"这么多人你有啥怕的"
    "你默默地坐在床头，脑海中的景象一次又一次的在眼前重复，这些真的是巧合吗？还是我们已经被某种未知力量吸引着才来到这里。"
    "杭州、密云、东极，这看似是我们自己选择的，或许又是命中注定？"
    wqbh"桃神！"
    "你突然从思绪中惊醒。"
    wqbh"你怎么了？"
    me"没什么没什么"
    wqbh"他们说要看个惊悚片...我...可以坐在你旁边吗？"
    me"看什么惊悚片啊，有毒毒，嫌这个鬼屋不够可怕吗？"
    jump .s64villa

label .s64villa:
    "电影开始了，紧凑的剧情吸引着你，但...另一方面，你又觉得自己真的很疲倦，视野逐渐模糊……"
    stop music fadeout 2.0
    scene black with Fade(2.5, 0.0, 0.0)
    pause 2
    scene ghost room movie with fade
    "等你再次醒来，电影还在播放，身边却已经没有人了。"
    me"都去睡觉了吗？这群人能这么好心把整个床让给我？？"

    scene black with dissolve
    "走出房门，外面竟然漆黑一片，之前楼道里的小夜灯也熄灭了，你疑惑着，拿出手机打开手电筒。"
    scene ghost stair light
    "四周静的可怕……"
    me"怎么连南这会儿不磨牙了？"
    play sound terrible_ring fadein 2.0
    """
    就在这时，天花板上突然响起了弹珠掉落的声音，但...这层的上面是楼顶啊？？？

    隐隐的，你好像又听见了海底古墓中类似的空灵的铃铛声，似乎从对面那个上锁的小房间传来。

    你发觉到自己心跳加速，不断安慰自己这只不过是个梦，但这真的是个梦吗？
    """

    "突然间你好像被人捂住了嘴巴，挣扎了几下就软在地上……" with vpunch
    with vpunch
    with vpunch
    pause 0.3
    with hpunch
    with hpunch
    pause 0.3
    with vpunch
    with vpunch
    pause 0.3
    image blur_ghost_stair = im.Blur("images/ghost/ghost stair light.png", 15)
    scene blur_ghost_stair with Dissolve(2)
    with vpunch
    with vpunch
    with vpunch

    stop sound fadeout 2.0
    "昏迷前，依稀看到对面那个上锁的小房间门把手转动了一下……"
    scene black with Fade(2.5, 0.0, 0.0)
    jump .s65villa

label .s65villa:
    with vpunch
    with vpunch
    wqbh"桃神！要结局揭秘了，快醒醒！"
    scene ghost room movie with Fade(0.0, 0.0, 2.0)
    me"靠我怎么睡过去了。"
    "电影很快放完了，值得庆幸的是，大家还都在这个屋子里。"

    scene ghost door dark with dissolve
    play music paradise_island fadein 2.0
    "结束后，部分人熬不动准备休息了，你也走出房门，路过对面那个上锁的小屋子时，突然发现门把手上多了一把钥匙。"
    ## Not important
    menu:
        "这时你："
        "询问大家有人进过这个屋子吗？这个钥匙是怎么回事？":
            "众人纷纷表示没有进过这个屋子。"
            conway"钥匙可能本身就在上面吧？"
            yinyin"可能是你记错了吧，别自己吓唬自己了。"
            "……要不还是进去看看吧。"

        "老子怕过谁，拧开把手，进屋一探究竟":
            $ dunhuang_value += 20
            jump .s66villa
            
        "可能是自己之前记错了，回屋睡觉吧":
            $ dunhuang_value -= 10
            "等睡醒已经是快十二点了，这次很幸运的是，你没有再陷入奇怪的梦境。"
            jump dj_105.s68villa

label .s66villa:
    scene ghost room utility with fade
    "打开房门，你发现里面只不过是一个普通的储物室，里面落满了灰尘，好像很久都没有人进来过了。"
    "你打量着周围，没有发现什么奇怪的东西，但房间里却散发着一股淡淡的清香，同时又带着一点点海腥气。"
    "似乎没有什么奇怪的……"
    "毕竟是海边的度假别墅，清香可能是清洁用品或杀虫剂吧。"
    wqbh"诶你偷偷躲在这里干啥？"
    me"你怎么出来了，不是在继续看电影吗？"
    wqbh"我有些困了，起来走动走动。"
    me"那我问你一个问题吧，这个储物间有什么奇怪的地方吗？我好像梦到过这里。"
    wqbh"奇怪的地方？"
    wqbh"嗯...看起来没什么大问题，但是..."
    me"但是什么！"
    wqbh"这既然是个储物间，为什么后面还有一扇门？"
    me"什么？"
    wqbh"你看，这些大箱子的后面不是还有一扇门吗？被堵住了。"
    ## Not important
    menu:
        "这时你："
        "感觉这里不太对劲，还是离开储物间回去看电影吧":
            $ dunhuang_value -= 10
            "于是你们又回到电影房，看完电影，等睡醒已经是快十二点了。"
            "这次很幸运的是，你没有再陷入奇怪的梦境。"
            jump dj_105.s68villa

        "和万千儿一起把箱子挪开，打开后面那扇门一探究竟":
            $ dunhuang_value += 10
            jump .s67villa

        "找个理由把万千儿支开，自己开门一探究竟":
            "没想到万千儿发现了你的用意，执意要和你一起开门。"
            jump .s67villa

label .s67villa:
    "这些箱子还挺沉，终于挪开了，仔细观察这扇门，发现门缝上密布着蜘蛛网，应该好几年都没有打开过了。"
    "你们俩对视了一眼，终于鼓起勇气扭动门把手，发现后面好像被顶住了，无法推开。"
    me"好吧，可能这只是房东的自己的小秘密。"
    wqbh"我看你最近神神秘秘的，到底发生什么了？"
    me"其实我只是做了两个奇怪的梦而已。"
    "你把事情的前因后果给她讲了一遍，两个人都陷入了沉默，沉默又是今晚的康桥。"
    "……"
    conway"诶你们俩在这干啥？"
    "……"
    scene ghost room movie with dissolve
    "于是你们又回到电影房，看完电影，然后休息了。"
    scene black with Fade(1.5, 1.0, 0.0)
    jump dj_105.s68villa