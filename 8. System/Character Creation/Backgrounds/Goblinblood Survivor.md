---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Goblin Lore Lore"
feats: "[[Forager]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You lost your family to the chaos of the Goblinblood Wars. Maybe you soothed your grief by creating new bonds, or maybe you never put out the flames of righteous anger in your heart. Now whatever semblance of peace you've found is threatened yet again—but this time, you have the skills to ensure that you won't be the one left to mourn.

Choose two attribute boosts. One must be to **Dexterity** or **Constitution**, and one is a free attribute boost.

You're trained in the Survival skill and the Goblin Lore skill. You gain the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
