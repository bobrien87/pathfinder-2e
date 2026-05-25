---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Belkzen Lore Lore"
feats: "[[Quick Coercion]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The orcs have had a long history of violence that brings some orcs pride, but for you it's a mark of shame. You see the path of reconciliation that Ardax is paving and find hope in the chance to transform your people's ways into one that moves away from stereotypes of brutality.

Choose two attribute boosts. One must be to **Charisma** or **Strength**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Belkzen Lore skill. You gain the [[Quick Coercion]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
