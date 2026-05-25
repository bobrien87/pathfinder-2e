---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Possession]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 living creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You send your mind and soul into the target's body, attempting to take control. The target must attempt a Will save. If you want to exert less control over the target, you can choose to use the effects of any degree of success more favorable to the target.

While you're possessing a target, your own body is [[Unconscious]] and can't wake up normally. You can sense everything the possessed target does. You can Dismiss this spell. If the possessed body dies, the spell ends and you must succeed at a Fortitude save against your spell DC or be [[Paralyzed]] for 1 hour, or 24 hours on a critical failure. If the spell ends during an encounter, you act just before the possessed creature's initiative.
- **Critical Success** The target is unaffected.
- **Success** You possess the target but can't control it. You ride along in the body while the spell lasts.
- **Failure** You possess the target and take partial control of it. You no longer have a separate turn; instead, you might control the target. At the start of each of the target's turns, it attempts another Will save. If it fails, it's [[Controlled]] by you on that turn; if it succeeds, it chooses its own actions; and if it critically succeeds, it forces you out and the spell ends.
- **Critical Failure** You possess the target fully, and it can only watch as you manipulate it like a puppet. The target is controlled by you.

**Heightened (9th)** The duration is 10 minutes, and you can physically enter the creature's body, protecting your physical body while the spell lasts.

**Source:** `= this.source` (`= this.source-type`)
