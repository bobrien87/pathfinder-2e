---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "touch"
targets: "one unattended item or one item you're holding"
duration: "until your next daily preparations"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an illusion that makes an object seem to be something entirely different. When you Cast this Spell, speak aloud a declarative statement that the target is a different, nonspecific object. Your statement can't presuppose any other facts. For instance, you could claim an object is "a stone" or "an antidote," but not "the Starstone" or "the antidote to the lethal poison you already drank." Creatures who previously observed the target receive an immediate Will save to disbelieve, but on a failure, the illusion temporarily rewrites their memory that the object was something different. A creature who failed their Will save, or didn't already see the item's original form, must Interact with the illusion as normal to receive a Perception check against the spell DC to disbelieve. When the spell ends, targets remember the object's true nature, even if they never disbelieved the spell.

**Source:** `= this.source` (`= this.source-type`)
