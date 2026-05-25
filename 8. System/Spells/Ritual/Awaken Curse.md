---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
cast: "1 day"
range: "1 mile"
targets: "1 curse"
duration: "unlimited"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You siphon a tiny portion of life force from each of the ritual's casters to empower a curse against disrupting effects. The difficulty of the counteract check to remove the curse changes based on the success of the ritual. Additionally, the first three times the curse is successfully counteracted, it leaps to the closest possible target within 100 feet, forcing the new target to attempt a saving throw against the curse's initial effects. Saves against the curse are attempted at the same DC as the curse when it was cast, subject to changes based on the ritual's success. If any creature successfully saves against the curse's initial effects, the curse dissipates harmlessly.
- **Critical Success** The first counteract attempt against the curse automatically fails. After that, the curse's counteract rank increases by 2 (to a maximum of 10).
- **Success** The curse's counteract rank increases by 1 (to a maximum of 10).
- **Failure** The curse's counteract rank is unchanged.
- **Critical Failure** You fail to grasp the curse's nuances and entangle yourself in its effects. The curse is lifted from the original target, and you and each secondary caster is affected by the curse with no saving throw.

**Source:** `= this.source` (`= this.source-type`)
