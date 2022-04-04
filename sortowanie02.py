import time

liczby = [2024, 4361, 3193, 2357, 2522, 3778, 4538, 4803, 1846, 2211, 4854, 4679, 987, 303, 164, 2841, 1121, 1344, 429, 4929, 2210, 4043, 4988, 4031, 1638, 502, 2450, 450, 677, 3245, 2730, 148, 2234, 1222, 4226, 1801, 318, 532, 121, 1909, 3274, 4153, 549, 2134, 221, 2184, 2242, 1529, 3747, 4816, 3829, 2320, 2635, 1629, 2022, 2918, 3859, 4325, 3880, 3152, 2202, 1836, 1369, 803, 2674, 4240, 586, 4655, 545, 3649, 2186, 3099, 689, 1691, 4902, 1813, 2233, 1379, 4367, 381, 236, 2975, 4720, 1751, 446, 454, 3554, 3445, 4777, 734, 144, 3808, 2876, 1589, 3120, 731, 1102, 1160, 4815, 995, 4079, 4227, 1193, 4991, 3621, 4609, 2124, 2873, 2428, 998, 2967, 4932, 4818, 780, 2144, 3641, 576, 1313, 201, 2330, 3256, 2388, 3932, 2056, 2743, 4183, 4326, 3534, 2966, 1704, 1438, 3572, 2167, 4137, 4337, 4232, 874, 2035, 4304, 2904, 2440, 2805, 3108, 2183, 682, 2532, 1262, 367, 2710, 4854, 1320, 3511, 2296, 4406, 2193, 941, 2240, 4891, 1545, 4446, 1909, 3978, 940, 4401, 1662, 963, 4977, 2505, 111, 4271, 1702, 3392, 4129, 866, 3307, 2149, 4609, 2547, 404, 1783, 1404, 3207, 722, 4160, 3620, 2666, 2829, 4820, 2827, 1597, 3776, 1943, 355, 1999, 3601, 4744, 2190, 3264, 4845, 4113, 3105, 1411, 4240, 4633, 2151, 3009, 510, 3635, 1374, 4171, 4137, 3275, 3586, 3462, 2379, 4267, 4038, 102, 2022, 1148, 4743, 3245, 4538, 2982, 526, 4096, 424, 3637, 85, 2975, 2196, 3102, 3809, 2940, 2514, 3490, 1823, 3593, 3606, 3955, 3485, 2561, 446, 3251, 4946, 2435, 4148, 4791, 2513, 412, 1647, 1021, 428, 4694, 2040, 881, 2265, 414, 1712, 3327, 872, 4909, 763, 2399, 1965, 967, 1335, 2452, 145, 2367, 384, 2103, 4446, 3081, 4240, 1447, 357, 2451, 34, 1424, 2835, 2686, 3244, 3894, 1150, 1592, 467, 189, 2230, 3687, 1763, 1928, 4983, 4808, 1021, 193, 1309, 582, 792, 3462, 3214, 3716, 1249, 1021, 3722, 381, 4298, 1724, 293, 341, 1899, 255, 2025, 1179, 3851, 4756, 4061, 2161, 1378, 3685, 1595, 4701, 1695, 4853, 3840, 2376, 4106, 3253, 4318, 2891, 2563, 3470, 3022, 3655, 2457, 214, 4441, 4583, 4659, 1851, 843, 1264, 4080, 2953, 4172, 3771, 140, 3140, 1883, 808, 728, 2651, 244, 1265, 2273, 4610, 794, 3390, 4795, 4128, 4913, 1657, 4906, 4647, 4639, 528, 555, 1626, 880, 106, 1746, 3616, 2952, 549, 1363, 3549, 3928, 110, 2066, 1243, 3966, 3096, 2334, 3657, 640, 4018, 4258, 204, 3743, 2050, 3222, 2949, 4564, 2295, 3402, 4850, 4749, 3621, 307, 2806, 2272, 59, 2539, 3340, 1081, 1830, 3272, 4488, 3847, 4649, 2632, 572, 483, 4713, 4440, 4792, 2976, 3303, 694, 3489, 4782, 2042, 3985, 1288, 779, 2106, 1266, 1882, 3283, 3646, 3644, 1109, 340, 4366, 2110, 3486, 3809, 2940, 742, 4020, 4343, 3487, 4045, 1865, 3808, 419, 4836, 1415, 3566, 2276, 567, 4189, 3046, 4311, 9, 4038, 2804, 3585, 569, 2319, 3946, 1982, 4488, 3932, 1140, 4621, 3356, 3109, 4661, 1370, 4061, 4569, 1653, 1432, 4280, 1954, 1069, 4041, 4768, 722, 45, 2489, 3778, 538, 3421, 4341, 1658, 2537, 2220, 472, 2419, 2190, 1673, 4083, 4358, 2825, 4056, 2995, 1089, 242, 4109, 3621, 735, 2698, 890, 3776, 4404, 1983, 537, 3703, 1511, 3368, 1875, 3937, 3801, 4969, 1080, 3366, 3922, 54, 56, 1466, 634, 2913, 341, 903, 1753, 3968, 4614, 616, 4715, 3298, 1280, 1642, 3455, 616, 1491, 3191, 3872, 3960, 3364, 3245, 3616, 1128, 3961, 1411, 2723, 4131, 2939, 502, 4271, 4707, 1826, 2763, 2341, 4986, 2041, 2745, 4060, 570, 2215, 3088, 1795, 2558, 2790, 1622, 366, 1352, 3742, 2260, 3727, 3341, 696, 4367, 4931, 80, 2360, 3418, 4551, 2400, 3417, 430, 3527, 4762, 2716, 3002, 803, 3882, 3241, 4573, 4588, 4299, 3583, 4203, 3394, 3472, 3675, 4072, 4557, 2246, 3720, 3671, 2454, 2510, 3938, 2187, 3708, 2708, 4739, 1032, 2522, 2111, 3386, 3284, 2223, 1018, 4924, 2166, 3834, 1717, 472, 4524, 4830, 1827, 3872, 474, 3102, 749, 2597, 4407, 2882, 2335, 3943, 3744, 4296, 1350, 638, 2251, 1490, 2095, 4317, 3832, 3706, 1378, 4035, 2748, 3348, 2393, 2514, 1997, 3866, 4116, 1222, 3331, 4671, 1584, 2068, 622, 902, 3982, 3876, 3247, 3296, 4079, 2346, 2110, 310, 3855, 3645, 3549, 3940, 3894, 2533, 1917, 1711, 1351, 762, 1966, 3067, 144, 1988, 581, 4361, 20, 4068, 3763, 365, 2637, 1936, 3257, 4895, 3065, 1974, 3379, 4965, 4342, 1412, 3891, 2034, 4661, 2074, 2129, 3660, 2826, 4605, 744, 2954, 1711, 1880, 3635, 892, 3346, 1795, 252, 4383, 1193, 4348, 1998, 1288, 3717, 1555, 2097, 1805, 4720, 2284, 956, 1400, 3217, 2377, 3242, 4018, 4998, 3259, 3178, 2785, 79, 105, 3943, 3680, 2327, 1510, 3404, 375, 1272, 4153, 4280, 898, 2312, 4084, 2596, 4203, 4696, 1526, 3394, 1532, 1395, 815, 11, 6, 220, 3912, 2531, 960, 205, 4260, 3403, 2613, 4951, 4743, 172, 3755, 17, 2110, 2223, 577, 4265, 1475, 2352, 3396, 912, 3853, 4896, 4543, 4755, 4698, 2591, 1674, 697, 3616, 1532, 2137, 4846, 4833, 3293, 3183, 4247, 2450, 715, 1404, 896, 2686, 1444, 4960, 1006, 4679, 3066, 1814, 3067, 4127, 4803, 4641, 4205, 4356, 4805, 516, 3675, 2355, 3224, 1745, 1451, 620, 705, 3420, 4252, 3687, 1678, 3635, 2390, 722, 4272, 4089, 11, 4259, 3960, 4769, 1431, 283, 3096, 2339, 3816, 400, 1353, 312, 4037, 839, 3145, 133, 1291, 887, 4426, 2554, 4433, 4838, 4622, 52, 352, 70, 1643, 2850, 307, 3032, 3621, 3427, 839, 2102, 3920, 3209, 3460, 4282, 1064, 2231, 2765, 2397, 3921, 226, 2625, 4529, 1869, 3078, 3511, 3273, 4915, 3041, 390, 1584, 1798, 213, 2522, 1058, 2539, 329, 4432, 4685, 4636, 1700, 3942, 28, 3328, 4906, 18, 2847, 4835, 4721, 4019, 1149, 3512, 4261, 1730, 227, 492, 3070, 2463, 4311, 981, 1044, 1762, 232, 688, 1959, 4513, 650, 2591, 2967, 755, 4326, 4686, 1277, 3269, 1325, 2409, 2589, 66, 4788, 3168, 4418, 3022, 905, 1051, 3119, 3069, 408, 924, 557, 4206, 2578, 311, 4919, 1361, 4178, 4949, 4585, 395, 2508, 2001, 959, 1081, 247, 4046, 4152, 578, 4152, 734, 4253, 1965, 250, 170, 75, 2547, 1460, 3350, 1317, 3470, 1337, 2860, 2045, 1499, 985, 3211, 3658, 485, 3597, 640, 3878, 136, 4767, 4496, 4166, 1681, 4906, 3735, 4466, 2058, 1288, 4246, 4161, 4469, 526, 3375, 4015]

#liczby=[8,10,5,12,9,3,1,7]

def sortuj(liczby):
    if(len(liczby) <= 1):
        return liczby
    dzielacy=liczby[0]
    wieksze=[]
    mniejsze=[]
    for i in range(1,len(liczby)):
        if liczby[i] > dzielacy:
            wieksze.append(liczby[i])
        else:
            mniejsze.append(liczby[i])
    tmp=[]
    tmp.extend(sortuj(mniejsze))
    tmp.append(dzielacy)
    tmp.extend(sortuj(wieksze))
    return tmp
    


miliseconds=time.time()
print(sortuj(liczby))
print(time.time()-miliseconds)
