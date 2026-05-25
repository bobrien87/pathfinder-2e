---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Arcana"
feats: "[[Quick Identification]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have fought against oppressive leaders and governments, harnessing ancient magical energies to help liberate your community from much larger, better-resourced armies. Using magical methods to harass and sabotage your oppressors, you've learned to take advantage of their blind spots and use their own resources against them.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Arcana skill and the Lore skill related to the settlement you liberated. You gain the [[Quick Identification]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
