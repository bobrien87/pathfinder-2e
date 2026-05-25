---
type: background
source-type: "Remaster"
boosts: "Con/Dex/Str"
skills: "Nature, Survival"
feats: "[[Forager]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You spent your youth in the wilderness, living close to or perhaps raised by animals. You have a close, mystical connection with these animals and gained certain abilities from them, though this limited your well-roundedness in mental pursuits.

Choose one ability boost. It must be **Strength**, **Dexterity**, or **Constitution**.

You are trained in Nature and Survival. You gain low-light vision (or darkvision if you already had low-light vision), imprecise scent with a range of 30 feet, and the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
