---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Gladitorial Lore Lore"
feats: "[[Experienced Professional]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While others choose to use their engineering ability to heal the injured or make brilliant innovations, you've used your skill to repair and modify clockwork constructs that battle in gladiatorial combat. You know how to get a crowd electrified for your clockwork gladiator, win or lose, and you know how to repair it when it gets damaged. These skills serve you well as an adventurer.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Crafting skill and the Gladiatorial Lore skill. You gain the [[Experienced Professional]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
