---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Ocean Lore Lore"
feats: "[[Underwater Marauder]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Tian Xia origin

You're one of the sea people, the divers who inhabit the rough shorelines. Diving into foreign depths with neither magic nor air reserves, it's your job to haul up seafood to feed your communities. Tourists come to watch you, listening to your whistles and songs as they crane their necks to catch sight of the pearls you sometimes bring to the surface. They might call you mermaids, but you know better. You've seen the true folk of the sea as you've gathered shellfish in your nets. You know to wear white to ward off sharks and worse. When adventure or treasure is found in the waves, you're one of the few who could possibly deal with it.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in Athletics and Ocean Lore. You gain the Underwater Marauder skill feat.

**Source:** `= this.source` (`= this.source-type`)
