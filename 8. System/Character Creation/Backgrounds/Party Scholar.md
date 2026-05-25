---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Deception, Alcohol Lore Lore"
feats: "[[Charming Liar]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Perhaps because you already achieved what you wanted at school or your position makes you invulnerable, you've begun to pour your efforts into a lifestyle of hedonistic excess. The fact that the Convocation isn't a months-long party might thus come as a rude shock to you, but your skill at deflecting blame and making fast friends might mitigate that.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in Deception. You're also trained in the Alcohol Lore skill or a Lore skill associated with your school. You gain the Charming Liar skill feat.

**Source:** `= this.source` (`= this.source-type`)
