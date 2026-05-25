---
type: background
source-type: "Remaster"
traits: ["[[Persona warrior]]"]
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Underworld Lore Lore"
feats: "[[Intimidating Glare]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Force, be it as a physical presence or as a strength of personality, has long given bullies power over others in their groups. Whether it's the threat of a physical beating or the actual assault itself, the bully's methods are usually efficient at establishing a network full of fearful followers and social power. You may have been a bully yourself, and if so, you've never faced any significant comeuppance or retribution for your nefarious actions, and the skills you developed as a youth while bullying others serve you very well today. Yet maybe you weren't the bully—maybe you were a baiter of bullies instead? Someone who put on an irresistible-to-bullies appearance only to turn their tactics back upon them with threats and violence. Were you a champion of the picked-upon and downtrodden in schoolyard and back alley alike, who lured the local bullies into traps that taught them lessons writ in blood and pain?

Choose two attribute boosts. One must be to **Strength** or **Charisma**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Underworld Lore skill. You gain the [[Intimidating Glare]] skill feat.

If you have the Warrior persona trait, you also become trained in the Warfare Lore skill.

**Source:** `= this.source` (`= this.source-type`)
