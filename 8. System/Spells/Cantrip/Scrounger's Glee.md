---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Cantrip]]", "[[Concentrate]]", "[[Fear]]", "[[Hex]]", "[[Mental]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a cruel laugh and a flash of your canines, you make a target understand that death is coming to claim it and that its demise will serve to strengthen another. The target becomes [[Frightened]] 1 if it fails a Will save (or [[Frightened]] 2 on a critical failure). This condition can't be reduced below 1 while the spell is active and the target can hear you. You can Dismiss the spell as a reaction when an ally critically succeeds at a Strike against the target, restoring @Damage[(ceil(@item.level/2))d4[healing]] Hit Points to that ally.

**Heightened (+2)** The number of Hit Points restored when you Dismiss the spell increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
