---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "10 minutes"
range: "touch"
targets: "1 object or a 10-foot-by-10-foot area"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a magical trap by binding a hostile spell into a rune. As part of performing this ritual, you also Cast a Spell to store in the rune. The stored spell must take 3 actions or fewer to cast, have a hostile effect, and target one creature or have an area. You can set a password, a trigger, or both for the rune. Any creature that moves, opens, or touches the target container or enters the target area that doesn't speak the password or that matches the trigger activates the rune, releasing the harmful spell within.

Once a spell is stored in the rune, the rune gains all the traits of that spell. If the stored spell targets one or more creatures, it targets the creature that set off the rune. If it has an area, that area is centered on the creature that set off the rune. The rune is a magical trap, using your spell DC for both the Perception check to notice it and the Thievery check to disable it; both checks require the creature attempting them to be trained in order to succeed. You can Dismiss the rune you create with this ritual so long as you can see it.
- **Critical Success** You create a particularly effective rune, granting a +2 circumstance bonus to the DC to notice and disable the rune.
- **Success** You create the rune successfully.
- **Failure** You fail to create the rune.
- **Critical Failure** The rune backfires, dealing 4d6 force damage per rank of the rune's spell to you, the secondary caster, and all creatures within 10 feet of the ritual's area

**Source:** `= this.source` (`= this.source-type`)
