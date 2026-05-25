---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Arcana, Academia Lore Lore"
feats: "[[Arcane Sense]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You were born to famed scholars of magic; your childhood was filled with old books, ink-stained lesson papers, and casual dinners with your parents' brilliant colleagues. This erudite upbringing eases your academic journey, as you were introduced early on to seminal texts and foundational theories that granted you a preternatural instinct and affinity for magic, but that also exposed you to massive pressures from familial expectations.

Choose two attribute boosts. One must be to **Charisma** or **Intelligence**, and one is a free attribute boost.

You're trained in Arcana. You're also trained in the Academia Lore skill or a Lore skill associated with your school. You gain the Arcane Sense skill feat.

**Source:** `= this.source` (`= this.source-type`)
