---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Hero-God Lore Lore"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

From subjects of worship to forces of nature that literally reshaped the region, hero-gods are central to Iblydan identity. While every child learns at least a little about their city-state's divinities from the past and present, you have devoured these legends. Do you long to have witnessed their miracles firsthand? Have you studied this topic as an academic, archivist, or priest? Perhaps you just love a good story. Whatever the case, these legends speak to you on an ineffable level. Are the fates hinting at some secret destiny: perhaps you're becoming a hero-god of old?

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in either the Occultism or Religion skill, as well as the Hero-God Lore skill. You gain the [[My Legend Must Be Told]] action. Replace this with the [[Mythic Echo]] action when you gain a mythic calling.

**Source:** `= this.source` (`= this.source-type`)
