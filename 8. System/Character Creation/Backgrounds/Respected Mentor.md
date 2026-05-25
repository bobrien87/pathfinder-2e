---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Performance, Academia Lore Lore"
feats: "[[Fascinating Performance]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While more career-minded peers consider dealing with students an annoyance and distraction from their own research, you're the rare exception who enjoys and finds fulfillment in educating and nurturing youths. Whether you're formally a teacher or still a senior student, you've impressed students with your dedication, entrancing lectures, genuine kindness, and generosity of knowledge.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in Performance. You're also trained in the Academia Lore skill or a Lore skill associated with your school. You gain the Fascinating Performance skill feat.

**Source:** `= this.source` (`= this.source-type`)
