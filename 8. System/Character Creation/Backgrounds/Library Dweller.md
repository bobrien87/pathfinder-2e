---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Library Lore Lore"
feats: "[[Additional Lore]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The library serves as your refuge from a world that isn't always welcoming or reasonable. Knowledge pools in libraries, their collections accumulating occult power as teachings, interpretations, deconstructions, and translations intertwine. You've glimpsed these esoteric truths, perhaps prompted to by propitious instructors, or you might have independently attained such epiphanies. Whatever the case, you're a frequent pilgrim to archives and academies, and you seek patterns of cosmic proofs within volumes and tomes.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in Occultism. You're also trained in the Library Lore skill or a Lore skill associated with your school. You gain the Additional Lore skill feat.

**Source:** `= this.source` (`= this.source-type`)
