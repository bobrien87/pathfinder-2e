---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Warfare Lore Lore"
feats: "[[Intimidating Glare]]"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are a respected guardian of the Verduran Forest, and the Wildwood Lodge has called upon you to manage security at their upcoming Greenwood Gala. What deeds earned you such trust and esteem? Perhaps you have skirmished with Taldan poachers, subdued riotous fey festivities, or spent years systematically sabotaging illegal Andoren woodcutting ventures. Maybe you are officially part of the Wildwood Lodge, serving as a part-time bodyguard and negotiator to help maintain order—otherwise Taldan nobles might send in their own army to keep the peace. Whatever the case, you know that tensions are building between factions who support and oppose the lodge's current leader, Valenar the Green, and you might have to step in to keep the Greenwood Gala fun and welcoming.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Warfare Lore skill. You gain the [[Intimidating Glare]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
