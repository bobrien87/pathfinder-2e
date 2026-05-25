---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 lock, or a door or container with a latch"
duration: "until your next daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target's latch mechanism clinks shut, held fast by unseen magical wards. When you magically lock a target, you set an Athletics and Thievery DC to open it equal to your spell DC or the base lock DC with a +4 status bonus, whichever is higher. Any key or combination that once opened a lock affected by this spell does not do so for the duration of the spell, though the key or combination does grant a +4 circumstance bonus to checks to open the door. If the target is opened, the spell ends. Assuming the target is not barred or locked in some additional way, you can unlock and open it with an Interact action during which you touch the target. This does not end the spell. You can Dismiss this spell at any time and from any distance.

**Heightened (2nd)** The duration is unlimited, but you must expend 6 gp worth of precious metals as an additional cost.

**Source:** `= this.source` (`= this.source-type`)
