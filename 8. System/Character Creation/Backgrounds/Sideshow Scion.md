---
type: background
source-type: "Remaster"
traits: ["[[Persona wildcard]]"]
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Acrobatics, Games Lore Lore"
feats: "[[Acrobatic Performer]]"
source: "Pathfinder Curtain Call Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Ah, the circus! What child didn't at some point fantasize about running away to join a troupe of clowns and daredevils and live a life on the road sharing living quarters with strange animals and even stranger coworkers? In your case, though, there was no need for fantasy, for you were born into the life. Your parents or extended family have a long tradition in the sideshow, be it as part of a traveling circus or as part of a more localized, year-round performance on a city boardwalk or marketplace. Even if you were the inverse of the youth who dreamed of running away, your childhood instead filled with visions of a sedentary aristocratic life or the rough upbringing of the working class, the sideshow skills and circus tricks you were exposed to seeped into your psyche. Now and then, a turn of phrase that spills from your lips or an unexpected little motion or act catches even your closest friends off guard. After all, what seems normal to you is anything but to someone who didn't grow up in a sideshow!

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in the Acrobatics skill and the Games Lore skill. You gain the [[Acrobatic Performer]] skill feat.

If you have the Wildcard persona trait, you also become trained in the Circus Lore skill.

**Source:** `= this.source` (`= this.source-type`)
