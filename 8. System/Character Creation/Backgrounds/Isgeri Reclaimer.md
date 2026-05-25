---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Stealth, Isger Lore Lore"
feats: "[[Terrain Stalker]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're descended from the original group of Kellid tribes that made up Isger, which was driven from its lands by Taldor's Seventh Army of Exploration centuries ago. While your people lost much to their colonizers, they did not lose their determination to keep their heritage alive, and your very existence is proof of this resolve. Though war brings great calamity, it also brings great opportunity for you to right the wrongs that were done and remind the world that you are here, and you haven't forgotten what it owes your people.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Stealth skill and the Isger Lore skill. You gain the [[Terrain Stalker]] skill feat in either rubble or underbrush. You know Hallit as a free additional language.

**Source:** `= this.source` (`= this.source-type`)
