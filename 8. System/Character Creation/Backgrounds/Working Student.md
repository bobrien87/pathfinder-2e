---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Labor Lore Lore"
feats: "[[Streetwise]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Many students look to education as a means of improving their lives. You are in the middle of that process or have spent a lot of time there, juggling lessons and textbooks with the manual labor to pay for them. Although this work might distract from your studies, it also teaches you other lessons, making you more worldly than your classmates.

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in Society. You're also trained in the Labor Lore skill or a Lore skill associated with your school. You gain the Streetwise skill feat.

**Source:** `= this.source` (`= this.source-type`)
