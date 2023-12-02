import time
t0=time.time()
s='''on x=-28..16,y=-48..0,z=-7..44
on x=-9..42,y=-28..23,z=-5..48
on x=-39..13,y=-42..6,z=-39..14
on x=-35..18,y=-38..12,z=0..47
on x=-24..30,y=-46..6,z=1..48
on x=-47..-2,y=-36..12,z=-26..28
on x=-42..7,y=-48..4,z=-42..12
on x=-16..34,y=-34..19,z=-12..33
on x=-43..4,y=-16..35,z=-49..1
on x=1..45,y=-37..12,z=-24..22
off x=30..47,y=-2..8,z=25..44
on x=-40..6,y=-23..29,z=-5..39
off x=-37..-20,y=-42..-23,z=-42..-31
on x=-28..18,y=-20..26,z=-39..13
off x=30..40,y=-12..2,z=-14..3
on x=-4..41,y=-48..2,z=-31..23
off x=-11..1,y=-8..2,z=8..17
on x=-26..23,y=-33..12,z=1..46
off x=16..33,y=33..42,z=14..33
on x=-48..-1,y=-5..47,z=-40..7
on x=57565..90931,y=26499..35340,z=13098..30238
on x=12526..30462,y=-47593..-23231,z=53349..82894
on x=-91468..-65718,y=-5018..16034,z=-44293..-22624
on x=-27227..-6248,y=-40269..-13926,z=-78988..-63072
on x=3506..22610,y=62535..80794,z=17259..50792
on x=40376..51341,y=-63200..-43375,z=41471..61477
on x=8080..22197,y=3859..38352,z=67380..81053
on x=1552..12025,y=-14844..14749,z=-93591..-76724
on x=-11556..18749,y=4423..13302,z=63492..97778
on x=55222..88212,y=23821..46975,z=-4542..16574
on x=-61423..-39389,y=6266..14798,z=-65380..-46741
on x=-77838..-67024,y=-31207..-18158,z=-27575..-7129
on x=-81397..-70175,y=-31698..-4468,z=17360..30653
on x=-34942..-14208,y=-86721..-57389,z=-44462..-15624
on x=28293..37615,y=54913..70753,z=44795..60378
on x=-14689..2178,y=-78248..-62048,z=-25046..-11381
on x=-43367..-15800,y=15347..49611,z=47892..68887
on x=17298..38698,y=63715..78876,z=-19159..-1078
on x=5545..32230,y=70330..77003,z=-39779..-10047
on x=15711..38161,y=11178..23247,z=62912..96742
on x=-78364..-52921,y=-4149..20442,z=-43822..-23451
on x=-2043..10291,y=63545..92912,z=-23692..1811
on x=52430..72696,y=-7304..15557,z=-57003..-48979
on x=4290..16794,y=-56202..-36267,z=64889..84487
on x=58149..73002,y=-32056..-321,z=45707..61502
on x=-92535..-71614,y=-14445..-9868,z=-33553..-10996
on x=52964..83914,y=-56670..-27499,z=17329..34563
on x=-4772..21856,y=29778..39361,z=-80367..-60893
on x=37212..58320,y=48080..67507,z=22443..39369
on x=-3349..4038,y=-42044..-34489,z=69227..85868
on x=-45006..-32722,y=-30720..-11951,z=56186..84549
on x=-7689..27577,y=-12822..22041,z=78946..80465
on x=33203..56209,y=14482..31642,z=56726..73482
on x=-42633..-14727,y=-16013..-3704,z=-82977..-60874
on x=-27620..-4368,y=-77767..-63095,z=24638..48293
on x=-70148..-43581,y=-2416..17050,z=-64874..-44396
on x=-47146..-30044,y=38306..60675,z=-64601..-41001
on x=-79530..-78117,y=-3116..8851,z=-23691..-3172
on x=46778..66546,y=-60904..-34009,z=-30872..-2675
on x=13768..39056,y=-37358..-26538,z=-79313..-53374
on x=9153..38127,y=-21602..5851,z=54990..82623
on x=17933..33387,y=-20067..-8352,z=56088..85736
on x=-74337..-53322,y=42882..47952,z=-37976..-31560
on x=-44765..-20887,y=64370..90871,z=-7955..19952
on x=-78643..-66896,y=26430..38878,z=6012..27389
on x=-11374..5429,y=40091..42394,z=-85912..-63552
on x=-36720..-22900,y=70217..75710,z=-7291..14193
on x=54804..79502,y=-33417..-2960,z=-33411..-10599
on x=-14690..15248,y=33208..55945,z=57795..72235
on x=-20657..570,y=-16338..-2719,z=-88238..-74298
on x=59883..72834,y=-56033..-40707,z=-26043..-5237
on x=-3522..10804,y=70147..89299,z=-37306..-19082
on x=-73328..-41278,y=-50672..-37278,z=-45749..-23154
on x=-37661..-11219,y=65972..95397,z=7489..26740
on x=4648..23315,y=-74707..-63601,z=-45671..-21953
on x=-73245..-44143,y=-11397..27130,z=33643..50646
on x=23427..31406,y=-40010..-22631,z=-69608..-58305
on x=-28851..-2567,y=61584..83543,z=18076..37159
on x=-36523..-25734,y=-39891..-27134,z=-73131..-58257
on x=12346..45691,y=-85792..-53521,z=-35812..-15243
on x=12520..26313,y=-19948..725,z=60247..92751
on x=40031..66621,y=-36963..-10146,z=-61370..-46098
on x=-61357..-42243,y=-70774..-37208,z=3015..23957
on x=-44255..-36032,y=64902..83822,z=-38707..-7320
on x=2615..26712,y=-67359..-45408,z=-75348..-38118
on x=-34475..-11487,y=-51075..-31791,z=-69242..-53855
on x=-50478..-19117,y=-22662..3011,z=-77482..-65102
on x=-75766..-43367,y=569..21233,z=47653..62539
on x=-16711..13174,y=66621..84715,z=30924..51703
on x=36505..56709,y=56803..66839,z=-30463..-23769
on x=-41935..-24686,y=51585..71635,z=-50138..-41708
on x=-24618..-8520,y=-92511..-70045,z=-31123..-11326
on x=-44787..-21109,y=-10120..4934,z=-86974..-64127
on x=-37201..-4038,y=-54506..-32587,z=-81799..-62907
on x=-29237..-20213,y=-57249..-34092,z=45594..72689
on x=-71309..-67214,y=-37692..-36381,z=3640..22746
on x=-3547..7699,y=-31608..-7361,z=-78088..-75610
on x=48449..78570,y=-20875..6499,z=-58599..-41679
on x=26640..46143,y=-93488..-64983,z=3884..23294
on x=55729..68431,y=-56992..-51330,z=7717..16657
on x=-70881..-40862,y=43699..68293,z=-41757..-16061
on x=-66091..-49306,y=-73470..-47817,z=-12616..9220
on x=32569..49130,y=49633..73334,z=-33549..-6711
on x=47554..65310,y=49102..55632,z=-38831..-11759
on x=-35265..-20298,y=36353..45956,z=-66084..-56530
on x=31030..33800,y=62000..82984,z=7545..29519
on x=-25990..7669,y=-38453..-25563,z=61530..85956
on x=-47912..-33964,y=30209..67779,z=48521..59963
on x=5684..15179,y=53175..73170,z=16929..54488
on x=-59354..-29913,y=52682..73787,z=-14796..-2131
on x=34084..52480,y=-55546..-20859,z=-60756..-53769
on x=40943..67063,y=52145..79330,z=-36911..-891
on x=-73304..-48514,y=-38583..-16021,z=24392..37006
on x=-41231..-20861,y=54056..70426,z=-37768..-12525
on x=38016..54122,y=52543..68936,z=-7233..12538
on x=70189..83008,y=-1022..18128,z=-16493..-7936
on x=-92011..-66733,y=3706..17083,z=18952..39596
on x=53238..84760,y=-54249..-35232,z=14232..40140
on x=64776..76657,y=27901..49623,z=-25183..-10958
on x=25860..46172,y=-70154..-64499,z=-24720..-413
on x=-7550..12707,y=-33861..-26819,z=74065..85896
on x=71196..76824,y=-19822..3483,z=-35932..-13158
on x=-86420..-58375,y=-22743..13548,z=21137..47500
on x=53092..63052,y=-67270..-37810,z=3762..26182
on x=-57975..-35066,y=48959..60434,z=21593..35021
on x=-60903..-35118,y=-19788..-13877,z=43710..66595
on x=-17137..2200,y=-42951..-15725,z=68300..89327
on x=-34868..-19211,y=-69403..-51544,z=31958..50653
on x=-60711..-44701,y=54746..62883,z=-11054..7348
on x=-28380..-14837,y=49324..75633,z=34372..52678
on x=10273..13925,y=-83985..-65836,z=-40883..-21930
on x=-22786..-8368,y=-92062..-66976,z=-8871..10273
on x=6001..29817,y=60841..78150,z=-21560..5974
on x=-16117..9624,y=-38050..-28860,z=55450..76632
on x=-4303..6115,y=35360..55718,z=42240..71260
on x=30529..58072,y=-80864..-53460,z=14833..27204
on x=-45298..-33766,y=44943..54544,z=36400..62460
on x=-41980..-26271,y=-76868..-51988,z=-9060..19313
on x=-32623..-6939,y=-66244..-47050,z=38706..63218
on x=-45584..-11160,y=62385..89525,z=6190..27078
on x=-54034..-43653,y=26105..48013,z=-56295..-42027
on x=-95679..-61660,y=-3324..9667,z=-14824..20238
on x=-5181..8383,y=-89084..-73477,z=4244..27316
on x=63213..80642,y=-46995..-19185,z=28458..40793
on x=-46529..-16089,y=5956..26059,z=-82869..-70434
on x=-22666..-9659,y=-83789..-59819,z=16239..33972
on x=-24529..-10505,y=-68395..-44985,z=-43459..-31810
on x=-86703..-68267,y=-25393..-5702,z=9722..38572
on x=19443..39413,y=30648..56526,z=51278..71489
on x=22304..33057,y=66975..90263,z=-1817..24013
on x=50145..68615,y=20323..42544,z=-39938..-5088
on x=204..8225,y=-20134..-4559,z=-90467..-73343
on x=-11771..-1240,y=-79508..-69290,z=31779..41841
on x=-44319..-25397,y=-59323..-44809,z=41138..65009
on x=-69142..-47933,y=-20140..5164,z=-65468..-36685
on x=34954..59983,y=51261..68628,z=429..36253
on x=25511..35598,y=-82471..-51345,z=8986..43333
on x=-2299..28751,y=19297..42840,z=-79575..-58217
on x=-98377..-70557,y=-17063..6429,z=1382..18686
on x=59412..88687,y=-20414..12473,z=-28382..-3990
on x=-46452..-24271,y=9717..28295,z=-77541..-69295
on x=-58123..-25200,y=-75909..-52306,z=23348..36183
on x=-50780..-30310,y=-33058..-28846,z=54733..68695
on x=-62920..-58191,y=23018..46504,z=26935..35840
on x=-53442..-21431,y=25880..48511,z=47200..71448
on x=32350..46922,y=45111..65023,z=-35283..-28540
on x=-70086..-50615,y=28086..33877,z=28764..56396
on x=23197..37854,y=-57704..-36416,z=-74626..-46087
on x=46586..65668,y=30254..59418,z=-50680..-26614
on x=-48638..-24854,y=-67971..-52554,z=-39193..-15566
on x=-34394..-12243,y=52461..80424,z=10521..23171
on x=-188..9519,y=68374..86419,z=-44618..-23169
on x=59310..75659,y=3837..23700,z=23841..45856
on x=-54868..-32564,y=46901..83593,z=11382..35311
on x=-54295..-36208,y=6868..44222,z=49289..71447
on x=-73757..-47984,y=48346..52043,z=-27269..1023
on x=31143..47984,y=-27415..10239,z=-77675..-53538
on x=-51075..-28705,y=29406..50405,z=60261..64407
on x=-24435..-3480,y=-73705..-65429,z=31120..58450
on x=-77894..-42583,y=-28849..-13479,z=-68839..-32078
on x=-30144..-3873,y=33899..52656,z=62539..83700
on x=3771..29713,y=46955..69183,z=-55590..-33020
on x=-82486..-64967,y=-3315..15390,z=-50370..-30971
on x=-18561..-9247,y=61180..78846,z=16883..21316
on x=-22459..368,y=6267..14584,z=-92243..-76717
on x=-93964..-68612,y=590..19875,z=-19094..-3812
on x=-85384..-72525,y=-14316..9021,z=-37469..-21077
on x=-20171..10587,y=-45934..-13740,z=-83530..-63366
on x=-3613..19552,y=2872..26108,z=67591..90335
on x=-54797..-29244,y=52502..75968,z=22631..41978
on x=-31709..-19073,y=-78023..-57867,z=-16044..-1695
on x=42907..64591,y=-60494..-41697,z=7396..34274
on x=-22169..13493,y=-63675..-43704,z=-70146..-42938
on x=-9398..-1009,y=79521..86699,z=-7578..-426
on x=67163..69237,y=-40928..-27442,z=-37200..-14848
on x=-68270..-48997,y=-3215..22691,z=-57315..-36115
on x=-62319..-41948,y=-42354..-15381,z=52464..64318
on x=-91325..-73355,y=-22923..-10674,z=-34655..-6215
on x=-11600..9609,y=-32693..-20365,z=56661..78797
on x=3002..8854,y=-60380..-47370,z=-60935..-47433
on x=-18864..-4001,y=-80823..-56965,z=27467..49339
on x=50065..59019,y=27173..47054,z=29151..52347
on x=-84983..-67041,y=6215..30411,z=-7894..23526
on x=66436..75714,y=-57869..-36031,z=-2629..4449
on x=55871..63911,y=48093..73117,z=-15687..7964
on x=30484..65332,y=37802..57883,z=13640..35473
on x=-3024..13221,y=69479..94018,z=-19781..12330
on x=-76841..-40967,y=44705..64363,z=-12342..3987
on x=-50317..-30669,y=15134..44544,z=45641..62331
on x=-1097..19010,y=-92028..-70161,z=17898..34117
on x=-56910..-34510,y=43871..65037,z=18479..40607
on x=-4087..30841,y=-47782..-16180,z=66517..91004
on x=63556..90817,y=5663..21156,z=-17275..3069
on x=-63..11495,y=-38165..-33947,z=66164..85162
on x=13705..21270,y=-56487..-41847,z=48244..79848
on x=43882..58033,y=-17825..6864,z=-61163..-41014
on x=-603..18764,y=-13707..7626,z=-97578..-62655
on x=-87646..-54123,y=26249..52965,z=1952..14629
on x=-68480..-61994,y=-19265..-5374,z=38032..42034
on x=4892..32392,y=59673..80857,z=11972..45013
on x=-31423..-16100,y=20332..31485,z=54386..71319
on x=-27668..276,y=-88140..-72843,z=-11224..2662
off x=-66569..-39172,y=40067..59785,z=-46779..-25063
off x=42078..50404,y=-8658..7192,z=49971..79381
on x=57638..65415,y=19822..32660,z=-55691..-22924
off x=6091..24900,y=53905..62370,z=-66817..-37882
on x=25136..30308,y=37241..52373,z=-75408..-47124
off x=-39586..-25323,y=60317..72507,z=-5430..19838
on x=60008..79444,y=-16196..22191,z=28310..40549
on x=-72513..-44230,y=-28714..-13259,z=42369..57467
on x=28366..61477,y=-71686..-44177,z=-25642..-12073
off x=-98592..-65990,y=-7494..6861,z=-18836..-1684
off x=41062..54176,y=6902..40549,z=48577..63780
on x=4209..22243,y=16593..41260,z=-90714..-66265
on x=73646..78591,y=7745..28374,z=-19062..4113
off x=-16527..5877,y=-33347..-14564,z=72131..93031
on x=-2601..11915,y=-79662..-76402,z=-19400..-9072
on x=-66043..-52950,y=42449..70740,z=-16397..-8029
on x=31097..49815,y=-70407..-54948,z=-34374..-15818
on x=46213..66123,y=24919..52347,z=39536..60489
off x=-40579..-25363,y=-55492..-36032,z=46465..56187
on x=-58587..-47075,y=-26673..7137,z=-74289..-47998
off x=-71115..-43182,y=5916..16003,z=47055..62648
off x=18056..38394,y=-72256..-45492,z=30393..62619
on x=-86105..-57637,y=19623..34937,z=-28353..-6857
off x=34767..61884,y=24847..43595,z=-57628..-34385
on x=42494..61669,y=61950..64256,z=4508..37093
on x=4938..25400,y=20137..41850,z=66454..79866
off x=66753..77341,y=-26195..-13496,z=2736..36812
off x=9161..36208,y=-71872..-57681,z=-59800..-34255
on x=22803..41931,y=-7230..7249,z=-81263..-63685
on x=62128..86492,y=2594..15499,z=-24195..-10571
off x=2219..19847,y=12592..32436,z=-86119..-67674
on x=-56278..-34092,y=54621..61289,z=-21708..-19242
off x=-63041..-48277,y=-19613..12784,z=-72622..-45931
on x=57563..80235,y=-42045..-21769,z=-40799..-13361
on x=6220..8134,y=-74186..-56164,z=-50907..-20022
off x=-75502..-44226,y=5877..20737,z=-61065..-39871
on x=48277..68969,y=-36081..-27834,z=18263..36607
off x=-93101..-71686,y=-7843..3116,z=-17057..12847
on x=36193..51512,y=8748..35447,z=-68334..-58639
off x=-19203..-10949,y=40540..60605,z=44840..64661
on x=61087..79558,y=33642..52095,z=28059..47944
on x=67571..86130,y=-47358..-21910,z=-13665..-1076
off x=-5529..17584,y=-18687..-5784,z=-94943..-73274
off x=-65181..-39057,y=37403..41422,z=29593..53758
off x=9348..23505,y=50333..57501,z=45117..63584
on x=-15124..-6499,y=7082..20135,z=72325..96017
on x=60549..77585,y=7711..25932,z=-32123..-2195
on x=-16996..5758,y=-66306..-51786,z=-57328..-41405
on x=-31438..-14060,y=-82035..-62914,z=28869..56660
on x=34767..62680,y=63661..78805,z=5456..21739
on x=23029..34746,y=-36310..-34645,z=-78969..-64494
on x=-44102..-26259,y=-8791..22215,z=-86237..-62784
off x=49345..60898,y=41927..49623,z=29688..41802
off x=67218..77648,y=8499..32074,z=309..23300
off x=-59809..-29273,y=-44275..-11556,z=52869..59154
off x=-7673..-5248,y=-59866..-25933,z=-78436..-53354
on x=60149..64230,y=17720..40138,z=-35925..-32781
on x=-90944..-74097,y=-32220..-21035,z=1878..8099
off x=-22563..-7189,y=69911..87126,z=16741..43536
on x=13763..25760,y=-59665..-48977,z=49037..67509
on x=7708..30846,y=24868..56328,z=47465..72954
off x=45744..52061,y=-2106..28618,z=-80394..-52551
on x=-69552..-55846,y=-47887..-22859,z=-23859..-9154
off x=-49632..-35997,y=-62267..-50340,z=2889..21563
on x=-39042..-34966,y=54696..77783,z=13010..46587
off x=-54652..-33019,y=-35233..-15490,z=58507..83564
off x=-49857..-31653,y=38484..50592,z=38533..56655
on x=40348..47016,y=-15552..-5294,z=50420..70694
off x=31271..43474,y=59286..77778,z=-3705..14499
off x=43476..60776,y=25882..39944,z=-63918..-44075
off x=-85323..-60474,y=-3767..1993,z=-24858..-5631
off x=59538..75559,y=16018..50491,z=-44591..-19953
on x=54273..91124,y=4853..31649,z=25520..46720
on x=-15271..3187,y=49068..70558,z=-64590..-39318
off x=-11166..1561,y=61100..80919,z=41278..48900
off x=-68170..-35507,y=15380..31052,z=44928..64928
on x=-79141..-63267,y=-38097..-17803,z=27565..39793
off x=35617..62914,y=17357..37935,z=-67537..-46955
off x=75258..88375,y=18743..32541,z=-21301..2102
off x=-51965..-14899,y=-82956..-52244,z=7707..16866
on x=-45266..-41350,y=-6426..18559,z=-73051..-56683
off x=6388..16150,y=68541..96433,z=-21319..3526
off x=-78796..-70623,y=7464..24358,z=-13457..19379
off x=57312..83670,y=-10302..11924,z=16389..33808
off x=-20655..5758,y=-88891..-74610,z=-14711..6771
off x=60755..87364,y=-4354..11468,z=-40103..-26166
off x=-51582..-29242,y=-9493..-3586,z=-71318..-61376
off x=49474..82569,y=35178..49303,z=-3013..17859
on x=17996..51804,y=60639..71390,z=14591..45698
off x=-4255..885,y=-86958..-68991,z=14233..52190
off x=-2525..15884,y=68182..88218,z=2639..16932
on x=22391..54046,y=21513..46833,z=-62874..-45827
off x=52662..72579,y=-25444..-12483,z=-56130..-36016
off x=54278..63949,y=36259..60155,z=17189..39193
off x=-11094..24227,y=-82795..-61018,z=76..32728
on x=-45794..-31326,y=-34389..-13750,z=47540..68919
on x=-17654..8599,y=25564..52506,z=-71942..-58407
off x=-35316..-10580,y=-60585..-37451,z=52982..60640
off x=42468..63388,y=-53755..-44232,z=14914..28572
off x=-90493..-63942,y=896..19749,z=24800..36043
off x=-21349..-19329,y=54201..73291,z=41420..61713
on x=15742..45245,y=45281..70499,z=34362..47718
on x=29532..68244,y=39054..66054,z=-40729..-25214
off x=-72688..-67520,y=-33082..-5024,z=-35069..-18313
off x=55205..65565,y=-40221..-27266,z=-52799..-36100
off x=-25658..-10567,y=-49110..-23999,z=-80909..-68443
off x=34428..53648,y=-85582..-62651,z=-21365..-3068
off x=-8355..26521,y=62047..93907,z=4541..25168
off x=64821..88457,y=22550..43490,z=2179..29791
off x=25..33417,y=58094..63212,z=-55323..-41795
off x=43920..70330,y=7595..21495,z=51592..59757
off x=-40552..-30302,y=-84294..-50462,z=25161..30986
off x=-43082..-26100,y=-48341..-27684,z=57974..68776
on x=63307..98099,y=5239..6835,z=-10290..7604
off x=-56051..-37896,y=-54998..-28049,z=-54865..-25544
on x=-90780..-70620,y=21967..48491,z=-27294..5978
on x=-54501..-26623,y=15690..38226,z=-62407..-42603
on x=-37188..-7940,y=-44155..-27767,z=54654..69550
on x=-43941..-18987,y=-80909..-49264,z=23182..52495
off x=-37956..-7791,y=-60872..-29579,z=48062..79477
on x=-45315..-34660,y=-43012..-24766,z=-69803..-51792
on x=-29071..1693,y=59904..88299,z=-27228..-8428
on x=71463..80739,y=-5557..9188,z=31987..34232
off x=69685..92757,y=15383..33721,z=2492..13716
off x=31129..48645,y=14907..32702,z=51374..69471
on x=-27354..-11896,y=53951..79566,z=19012..30611
on x=-10617..15746,y=-85619..-58865,z=-37058..-6481
off x=7510..32970,y=-2176..9990,z=-82335..-65371
on x=26157..52974,y=21017..49726,z=56310..71614
on x=-90923..-65168,y=-26173..-7273,z=12486..29477
on x=49051..75622,y=-55612..-27911,z=35019..40277
off x=18242..35160,y=-78992..-47098,z=-55649..-34785
on x=46549..59075,y=-51550..-27864,z=-65729..-36745
on x=-88707..-59767,y=-22290..-7702,z=-18116..10257
off x=-28367..-1172,y=-38705..-32225,z=65254..82624
off x=8132..24457,y=67446..89556,z=2649..20586
off x=-58620..-53438,y=34898..60181,z=27961..37874
on x=-5212..15843,y=17175..21721,z=-82048..-66953
off x=-34571..-3519,y=15800..26425,z=-83105..-64876
off x=-42841..-25628,y=-37013..-15996,z=57254..89725
on x=64596..87002,y=-636..9416,z=-23576..-607
on x=-19886..-15182,y=-41900..-26203,z=-71734..-50009
on x=-51000..-28187,y=-53585..-32748,z=42750..63329
on x=33094..58194,y=-66082..-41581,z=37005..52569
off x=-88093..-78109,y=-16275..7951,z=-21058..1805
off x=-35424..-17859,y=-91788..-74602,z=4659..22350
on x=34636..44622,y=49201..70860,z=-51045..-34152
off x=57533..89201,y=-19686..8041,z=20134..53867
on x=-72336..-50630,y=3272..19475,z=-73377..-41567
on x=-39941..-20090,y=44207..65660,z=38358..46288
off x=25773..52885,y=-19505..-1242,z=47756..67747
off x=-66654..-39150,y=-61014..-40867,z=34863..56457
off x=55029..79772,y=26767..42575,z=-28493..-22469
off x=12260..26817,y=-42201..-28002,z=-87775..-59299
on x=11403..35365,y=54876..78258,z=30994..63386
off x=51120..69484,y=-19375..-5359,z=32407..63494
off x=-78490..-75303,y=-27728..-11076,z=-26007..40
on x=-31321..-16229,y=-38342..-30414,z=-76015..-52813
off x=16047..20947,y=-20240..13385,z=-93147..-70379
off x=336..17722,y=-93976..-74467,z=-21364..-4290
on x=-87077..-72111,y=-19311..2385,z=-19722..11948
on x=-43084..-36372,y=45712..79823,z=-35896..-17054
on x=51948..84441,y=-20034..16460,z=-49997..-39453
on x=-801..22161,y=-27356..-9033,z=64701..77370
off x=-17951..-3999,y=-22008..-5995,z=74415..87205
on x=36551..55317,y=-6322..7074,z=45902..60732
off x=-77898..-46110,y=-7761..14727,z=-66524..-27225
off x=30110..58658,y=-80172..-45638,z=9785..40800
on x=-45418..-11683,y=47555..61363,z=-61328..-43598
on x=-80008..-69072,y=-1319..17150,z=-21743..-4143
off x=-86580..-49644,y=33570..44522,z=2446..22556
on x=58440..69330,y=42013..49828,z=-38416..-10905
on x=-9908..4199,y=36609..69919,z=52916..76179
on x=51626..69610,y=-36470..-23324,z=7185..32596
on x=56569..81453,y=-21538..437,z=41732..49370
on x=36553..49666,y=-11893..8686,z=-82624..-48977
on x=2986..29502,y=-54434..-49660,z=-63927..-38189
off x=-5293..9459,y=-67681..-55149,z=48505..66469
on x=-46715..-36399,y=-76263..-62952,z=-48274..-19984
on x=-54416..-28922,y=42872..75760,z=-54458..-16424
off x=-42207..-10237,y=23871..47599,z=-77359..-50055
on x=29280..62784,y=-66700..-41256,z=-56890..-26180
on x=-28625..-11913,y=-60101..-38069,z=-57492..-37098
on x=-89088..-60937,y=9529..37643,z=-11865..7850
off x=-80400..-49614,y=-43525..-28655,z=26499..51995
on x=5353..30424,y=65230..91478,z=-32520..-5102
off x=-81229..-63087,y=-12508..16907,z=-27119..-17105
on x=34340..63142,y=20..26920,z=53898..71455
off x=1014..17545,y=-75840..-47576,z=36094..60264
off x=-46217..-18879,y=30016..54146,z=55825..63549
off x=29308..54759,y=-62506..-56240,z=-27967..3765
off x=44146..45970,y=9779..37326,z=-72844..-49270
on x=-15311..6239,y=-4435..19231,z=76084..96718
off x=-84687..-69536,y=16529..28274,z=-16189..-5583
on x=-73836..-42104,y=-23097..9342,z=-63732..-50625
off x=-43484..-29966,y=-65904..-39849,z=-54334..-28671
off x=61637..68600,y=-44250..-21193,z=-43509..-24790
on x=54915..59902,y=46331..70655,z=-24790..-20283'''.split('\n')
t=[[[0]*101 for i in range(101)] for i in range(101)]
u=[]
for i in s:
    j,k=i.split()
    x,y,z=k.split(',')
    a,xa=x.split('=')
    b,yb=y.split('=')
    c,zc=z.split('=')
    x1,x2=map(int,xa.split('..'))
    y1,y2=map(int,yb.split('..'))
    z1,z2=map(int,zc.split('..'))
    u.append((j=='on',x1,x2+1,y1,y2+1,z1,z2+1))
    if not(50<x1 or 50<y1 or 50<z1 or -50>x2 or -50>y2 or -50>z2):
        for x in range(x1,x2+1):
            if -50<=x<=50:
                for y in range(y1,y2+1):
                    if -50<=y<=50:
                        for z in range(z1,z2+1):
                            if -50<=z<=50:
                                if j=='on':
                                    t[x][y][z]=1
                                else:
                                    t[x][y][z]=0
print(sum(sum(sum(i) for i in j) for j in t))
t1=time.time()
tot=0
xs=sorted(set(i[1] for i in u)|set(i[2] for i in u))
q=0
for lx,rx in zip(xs,xs[1:]):
    q+=1
    #if q%10==0:print('Working on',q,'out of',len(xs)-1)
    ys=sorted(set(i[3] for i in u if not(i[1]>=rx or i[2]<=lx))|set(i[4] for i in u if not(i[1]>=rx or i[2]<=lx)))
    for ly,ry in zip(ys,ys[1:]):
        zs=sorted(set(i[5] for i in u if not(i[1]>=rx or i[2]<=lx or i[3]>=ry or i[4]<=ly))|set(i[6] for i in u if not(i[1]>=rx or i[2]<=lx or i[3]>=ry or i[4]<=ly)))
        for lz,rz in zip(zs,zs[1:]):
            state=0
            for on,x1,x2,y1,y2,z1,z2 in u:
                if x1<=lx and rx<=x2 and y1<=ly and ry<=y2 and z1<=lz and rz<=z2:
                    if on:
                        state|=1
                    else:
                        state&=0
            #print(state,rz,lz,ry,ly,rx,lx)
            tot+=state*(rz-lz)*(ry-ly)*(rx-lx)
print(tot)
t2=time.time()
print()
print('Part 1:',t1-t0,'seconds')
print('Part 2:',t2-t1,'seconds')
print('Total: ',t2-t0,'seconds')
