---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery"
feats: "[[Pickpocket]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You eked out a living by picking pockets on the streets of a major city, never knowing where you'd find your next meal. While some adventure for the glory, you do so to survive.

Choose two attribute boosts. One must be to **Dexterity** or **Constitution**, and one is a free attribute boost.

You're trained in the Thievery skill and a Lore skill for the city you lived in as a street urchin (such as Absalom Lore or Magnimar Lore). You gain the [[Pickpocket]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
