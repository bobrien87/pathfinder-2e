---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You temporarily stop time for everything but yourself, allowing you to use several actions in what appears to others to be no time at all. Immediately after casting *freeze time*, you can use up to 9 actions in 3 sets of up to 3 actions each.

After each set of actions, 1 round passes, but for only you, effects specifically targeting or affecting you, and effects that you create during the stoppage. All other creatures and objects are invulnerable to your attacks, and you can't target or affect them with anything.

Once you have finished your actions, time begins to flow again for the rest of the world. If you created an effect with a duration that extends beyond *freeze time*'s duration, such as [[Wall of Fire]], it immediately affects others again, but it doesn't have any of the effects that happen only when you first Cast the Spell.

**Source:** `= this.source` (`= this.source-type`)
