---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival"
feats: "[[Forager]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've made a living sorting through the things society throws away. You might have scavenged simply to survive, or plied a trade as a ragpicker, dung carter, or the like. While you've left that life behind, you still keep one eye on the ground out of habit.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Lore skill for the settlement you grew up scavenging in. You gain the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
