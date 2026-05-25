---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance, Gladatorial Lore Lore"
feats: "[[Impressive Performance]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The bloody games of the arena taught you the art of combat. Before you attained true fame, you departed—or escaped—the arena to explore the world. Your skill at drawing both blood and a crowd's attention pay off in a new adventuring life.

Choose two attribute boosts. One must be to **Strength** or **Charisma**, and one is a free attribute boost.

You're trained in the Performance skill and the Gladiatorial Lore skill. You gain the [[Impressive Performance]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
