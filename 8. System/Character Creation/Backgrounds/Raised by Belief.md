---
type: background
source-type: "Remaster"
boosts: "Cha/Con/Dex/Int/Str/Wis, Cha/Con/Dex/Int/Str/Wis"
feats: "[[Assurance]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether in a monastery, a religious household, or just as part of your everyday life, your upbringing was steeped in the traditions of a particular deity. You might remain committed or you may have turned from your childhood creed, but your skills are still founded in your devotion.

Choose two attribute boosts. One must be to an attribute specified in your deity's **Divine Attribute**, and the other is a free attribute boost.

You're trained in the deity's listed Divine Skill and gain the [[Assurance]] feat with that skill. You gain a Lore skill related to your deity (Abadar Lore, for example).

**Source:** `= this.source` (`= this.source-type`)
