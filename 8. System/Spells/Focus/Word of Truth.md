---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]"]
cast: "`pf2:1`"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You speak a statement you believe to be true and that is free of any attempt to deceive through twisting words, omission, and so on. The statement must be 25 words or fewer. A symbol of your deity glows above your head and lasts for the spell's duration, and anyone who sees you and hears you speak knows that you believe what you say is true. This assurance of honesty grants you a +2 status bonus to Diplomacy checks as long as the symbol persists. You can Dismiss the spell, and if you say something that you don't believe is entirely true, the spell ends before you complete your statement.

> [!danger] Effect: Spell Effect: Word of Truth

**Source:** `= this.source` (`= this.source-type`)
