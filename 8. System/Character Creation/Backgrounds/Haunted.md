---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are followed by a spirit or entity, either from childhood or since a momentous event. You and others may have seen this entity. You have studied esoteric subjects trying to understand your situation, but this presence in your life remains a mystery. Whatever this entity is or wants, it influences your life in subtle ways, and not always for the better. Sometimes the entity helps you, but at other times, its influence is malevolent or harmful. The entity is most likely to surface in stressful situations.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You are trained in Occultism and an additional skill in which the haunting entity is well-versed, determined by the GM. Any time you attempt a skill check for the entity's skill, the GM can offer you a +1 circumstance bonus to the check, as though the entity were [[Aiding]] you. If you accept but fail the check, you are [[Frightened]] 2 ([[Frightened]] 4 on a critical failure). The initial Frightened value can't be reduced by effects that would reduce or prevent the condition (such as a fighter's bravery).

**Source:** `= this.source` (`= this.source-type`)
