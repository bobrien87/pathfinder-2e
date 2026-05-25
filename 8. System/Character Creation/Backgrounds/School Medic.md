---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Academia Lore Lore"
feats: "[[Battle Medicine]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether practicing as part of your course of study or serving on staff, you've been asked to help by a school concerned that Sarkoris's lessons might be too harsh for the visiting students. Although the city of Nerosyan is wellprotected from the remaining demons of the Sarkoris Scar, the multitude of students seeking to help in that dangerous land ensure that you have plenty of chances to practice your medical arts.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in Medicine. You're also trained in the Academia Lore skill or a Lore skill associated with your school. You gain the Battle Medicine skill feat.

**Source:** `= this.source` (`= this.source-type`)
