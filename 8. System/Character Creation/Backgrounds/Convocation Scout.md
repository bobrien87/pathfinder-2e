---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Politics Lore Lore"
feats: "[[Group Impression]]"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The Convocation is the biggest, most anticipated academic event in recent years. Eager to create long-lasting alliances as well as recruit promising students or staff to their own ranks, your school has sent you as a representative to advance their interests. Your tact, analytical ability, and gift for communication serve you well in scouting profitable partnerships with the Convocation's other sponsors and guests.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in Diplomacy. You're also trained in the Politics Lore skill or a Lore skill associated with your school. You gain the Group Impression skill feat.

**Source:** `= this.source` (`= this.source-type`)
