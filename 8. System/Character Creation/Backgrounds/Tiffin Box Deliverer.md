---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Labor Lore Lore"
feats: "[[Streetwise]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Tian Xia origin

Known to some as a dabbawala, you work for a delivery service, delivering and returning sturdy tiffins with hardy lunches for those who can't afford to bring lunch with them on their morning commute. Maybe you saw something you shouldn't have while out on your deliveries. Maybe you want more than just a mundane life. Either way, you know to prepare a lunch or two for your future adventures.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in Society and Labor Lore. You gain the Streetwise skill feat.

**Source:** `= this.source` (`= this.source-type`)
