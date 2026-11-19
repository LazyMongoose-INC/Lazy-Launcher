# Инвентаризация модов LazyMongoose Modpack 1.12.2

Дата извлечения: 19 ноября 2026 года

Источник: `Launcher.log`, commit `2538140ba451601edb204d3491edd39f50187481`, blob `eb640f019cef0b07b23a8e46233953f01bcad2ea`.

## Основание

Строка 42577 (в 1-based нумерации) содержит сообщение Forge:

`[21:45:14] [Netty Server IO #3/INFO] [FML]: Client attempting to join with 180 mods : ...`

Это handshake со списком клиентских модов, передаваемым при подключении к интегрированному серверу. Forge в строке 37893 отдельно сообщает: `Forge Mod Loader has successfully loaded 180 mods`.

Извлечено ровно 180 записей. Сохраняются mod id и версия в том виде, в каком их сообщил Forge. Это инвентаризация по runtime-журналу, а не список проверенных JAR-файлов и не разрешение на их распространение.

## Список модов

1. `buildcraftlib` — `8.0.0`
2. `cyclopscore` — `1.6.2`
3. `p455w0rdslib` — `2.3.161`
4. `astralsorcery` — `1.10.27`
5. `enderiointegrationforestry` — `5.3.72`
6. `quarryplus` — `12.5.7`
7. `buildcraftenergy` — `8.0.0`
8. `cofhcore` — `4.6.6`
9. `draconicevolution` — `2.3.27`
10. `projecte` — `1.12.2-PE1.4.1`
11. `thermalinnovation` — `0.3.6`
12. `musicplayer` — `2.1.1.342`
13. `immersivecables` — `1.3.2`
14. `endercore` — `1.12.2-0.5.78`
15. `neat` — `1.4-17`
16. `thaumicjei` — `1.6.0`
17. `hammercore` — `2.0.6.32`
18. `jeibees` — `0.9.0.5`
19. `cookingforblockheads` — `6.5.0`
20. `placebo` — `1.6.0`
21. `calculator` — `5.0.12`
22. `ae2stuff` — `0.7.0.4`
23. `bookshelf` — `2.3.590`
24. `forgelin` — `1.8.4`
25. `ironbackpacks` — `1.12.2-3.0.8-12`
26. `xreliquary` — `1.12.2-1.3.4.796`
27. `stg` — `1.12.2-1.2.3`
28. `llibrary` — `1.7.9`
29. `uteamcore` — `2.2.5.375`
30. `wct` — `3.12.97`
31. `cofhworld` — `1.4.0`
32. `sonarcore` — `5.0.19`
33. `ftblib` — `5.4.7.2`
34. `waila` — `1.8.26`
35. `itank` — `1.2.1-1.12.2`
36. `mekanismgenerators` — `1.12.2-9.8.3.390`
37. `enderioconduitsrefinedstorage` — `5.3.72`
38. `chickens` — `6.0.4`
39. `librarianliblate` — `9.4`
40. `fpsreducer` — `mc1.12.2-1.20`
41. `thaumcraft` — `6.1.BETA26`
42. `mcmultipart` — `2.5.3`
43. `mysticalagradditions` — `1.3.2`
44. `texfix` — `4.0`
45. `twilightforest` — `3.11.1021`
46. `enderioconduits` — `5.3.72`
47. `refinedstorage` — `1.6.9`
48. `farmersdelight` — `1.1.6`
49. `industrialforegoing` — `1.12.2-1.12.2`
50. `unidict` — `1.12.2-3.0.10`
51. `arche@@VERSION` — ``
52. `enderiomachines` — `5.3.72`
53. `biomesoplenty` — `7.0.1.2445`
54. `redstoneflux` — `2.1.1`
55. `buildcraftsilicon` — `8.0.0`
56. `chunkanimator` — `1.12.2-1.2`
57. `aromabackup` — `3.0.0.0.b135`
58. `botania` — `r1.10-364`
59. `gendustry` — `1.6.5.8`
60. `helpfixer` — `1.12.1-1.5.18`
61. `teslacorelib_registries` — `1.0.18`
62. `improvableskills` — `12.4.68`
63. `solarflux` — `12.4.11`
64. `ic2` — `2.8.170-ex112`
65. `yac` — `2.1.158`
66. `buildcraftbuilders` — `8.0.0`
67. `pewter` — `1.2.0`
68. `buildcraftfactory` — `8.0.0`
69. `veinminer` — `0.38.1`
70. `advanced_solar_panels` — `4.3.0`
71. `teslacorelib` — `1.0.18`
72. `enderioinvpanel` — `5.3.72`
73. `gunpowderlib` — `1.12.2-1.1`
74. `FML` — `8.0.99.99`
75. `thermalexpansion` — `5.5.7`
76. `enderiointegrationtic` — `5.3.72`
77. `aromabackuprecovery` — `3.0.0.0.b135`
78. `enderioconduitsappliedenergistics` — `5.3.72`
79. `worldedit` — `6.1.10`
80. `buildcraftcompat` — `8.0.0`
81. `bigreactors` — `1.12.2-0.4.5.68`
82. `bibliotheca` — `1.3.6-1.12.2`
83. `irontanks` — `2.4.0+mc1.12.2`
84. `instantunify` — `1.1.2`
85. `codechickenlib` — `3.2.3.358`
86. `scalinghealth` — `1.3.37`
87. `buildcraftcore` — `8.0.0`
88. `wailaharvestability` — `1.1.12`
89. `industrialwires` — `1.7-36`
90. `forgelin_continuous` — `2.0.0.1`
91. `unloader` — `1.0.1`
92. `ic2cropplugin` — `1.1`
93. `tesla` — `1.0.63`
94. `ae2wtlib` — `1.0.34`
95. `cucumber` — `1.1.3`
96. `tatw` — `1.0.1.2.b27`
97. `mixinbooter` — `11.15`
98. `mycommands` — `1.12.2-01`
99. `librarianlib` — `9.4`
100. `renderlib` — `1.4.5`
101. `jee` — `1.0.8`
102. `itemfilters` — `1.0.4.2`
103. `jei` — `4.16.5.1027`
104. `buildcrafttransport` — `8.0.0`
105. `everlastingabilities` — `1.5.2`
106. `nei` — `2.4.3`
107. `mekanism` — `1.12.2-9.8.3.390`
108. `thermalfoundation` — `2.6.7`
109. `timeinabottled` — `2.0`
110. `bdlib` — `1.14.4.1`
111. `wawla` — `2.6.275`
112. `potionfingers` — `r1.0-2`
113. `subcommonlib` — `1.2.0.1`
114. `mcp` — `9.42`
115. `clumps` — `3.1.2`
116. `expequiv` — `12.3.17`
117. `appliedenergistics2` — `rv6-stable-7`
118. `gravisuite` — `3.1.1`
119. `enderiointegrationticlate` — `5.3.72`
120. `compactmachines3` — `3.0.18`
121. `aroma1997core` — `2.0.0.2.b167`
122. `iskalliumreactors` — `0.5.16`
123. `conarm` — `1.2.5.10`
124. `surge` — `2.0.77`
125. `inventorytweaks` — `1.64+dev.151.822d839`
126. `creeperconfetti` — `1.4.2`
127. `harvestcraft` — `1.12.2zb`
128. `foamfixcore` — `7.7.4`
129. `omlib` — `3.0.1-162`
130. `joypadsplitscreenmod` — `1.12.0-0.22`
131. `quarryplus_ct` — `12.5.7`
132. `ichunutil` — `7.2.2`
133. `inventorypets` — `2.0.15`
134. `enderstorage` — `2.4.6.137`
135. `exnihilocreatio` — `1.12.2-0.4.5`
136. `forge` — `14.23.5.2860`
137. `quickleafdecay` — `1.2.4`
138. `brandonscore` — `2.4.19`
139. `thaumicequivalence` — `1.12.2-1.0.4`
140. `magicbees` — `1.0`
141. `buildcraftrobotics` — `8.0.0`
142. `chesttransporter` — `2.8.8`
143. `eplus` — `5.0.178`
144. `cyclicmagic` — `1.20.12`
145. `mysticalagriculture` — `1.7.5`
146. `ironchest` — `1.12.2-7.0.67.844`
147. `zerocore` — `1.12.2-0.1.2.9`
148. `weaponlevels` — `2.7.1`
149. `minecraft` — `1.12.2`
150. `tconstruct` — `1.12.2-2.13.0.183`
151. `mousetweaks` — `2.10.1`
152. `ftbquests` — `1202.9.0.14`
153. `immersiveengineering` — `0.12-98`
154. `thermaldynamics` — `2.5.6`
155. `silentlib` — `3.0.13`
156. `vanillasatchels` — `1.0.2`
157. `baubles` — `1.5.2`
158. `veinminermodsupport` — `0.38.1`
159. `enderiopowertools` — `5.3.72`
160. `integrationforegoing` — `1.12.2-1.10`
161. `enderio` — `5.3.72`
162. `extrautils2` — `1.0`
163. `mantle` — `1.12-1.3.3.55`
164. `fastbench` — `1.7.4`
165. `autoreglib` — `1.3-24`
166. `fluxnetworks` — `4.1.0`
167. `entityculling` — `6.5.0`
168. `enderiobase` — `5.3.72`
169. `fastfurnace` — `1.3.1`
170. `wanionlib` — `1.12.2-2.91`
171. `xaerominimap_core` — `1.12.2-1.0`
172. `enderioconduitsopencomputers` — `5.3.72`
173. `foamfix@@VERSION` — ``
174. `xaerobetterpvp` — `20.29.0`
175. `practicallogistics2` — `3.0.8`
176. `morphtool` — `1.2-21`
177. `chesthopper` — `1.2.3`
178. `ClientFixer` — `1.12.2-1.9`
179. `forestry` — `5.8.2.427`
180. `morebees` — `1.12.2-2.0.1`

## Замечания по качеству данных

- В двух записях версия представлена как `@@VERSION@`: `arche` и `foamfix`. Это буквально значение из handshake, его нельзя подменять придуманной версией. Для точной идентификации нужны имена JAR-файлов/их метаданные.
- Некоторые записи — служебные компоненты Minecraft/Forge/FML и библиотеки, а не отдельные игровые моды (например, `minecraft`, `forge`, `FML`, `mcp`).
- Наличие mod id в handshake подтверждает загрузку/объявление Forge, но не подтверждает лицензию, возможность публичного распространения или наличие конкретного JAR в репозитории.
- Для manifest установщика дополнительно нужны исходные JAR-файлы, конфигурации и ресурсы, SHA-256 и проверенные источники/разрешения.

## Рекомендация для Lazy Launcher

Использовать этот файл как контрольный список состава runtime при проверке сборки. После получения исходной директории `.minecraft/mods` построить сопоставление: mod id → JAR → версия из metadata → размер → SHA-256 → источник → статус распространения. Не выпускать модпак-манифест на основании одного handshake.
