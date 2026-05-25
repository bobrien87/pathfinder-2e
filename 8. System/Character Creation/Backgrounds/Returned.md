---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "**Boneyard Lore (with Additional Lore perks) Lore"
feats: "[[Diehard]], [[Additional Lore]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You died and miraculously returned with knowledge of the realms beyond death and a stronger link to life. Some dead and undead souls might feel a strange, instinctual kinship with you.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You gain the [[Diehard]] feat and the [[Additional Lore]] feat for Boneyard Lore.

**Source:** `= this.source` (`= this.source-type`)
