---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Air]]", "[[Concentrate]]", "[[Electricity]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 living creature or 1 corpse that died within the last round"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A dense lightning cloud descends to fill the target's space, then fires a jolt of revitalizing lightning into the target. If the target is a corpse that died within the last round, the creature comes back to life with 0 Hit Points, and any effects and conditions it had when it died, with the exception of dying, and its wounded condition increases by 1. The creature's initiative is right before yours.

Regardless of whether the creature came back to life or was already alive, it regains 8d8 Hit Points, and the bolt wakes it up if it was [[Unconscious]]. For the duration of the spell, the target is supercharged. It becomes [[Quickened]] and can use the extra action to Stand, Stride, Strike, or Fly (if it has a fly Speed). In addition, it can cast 5th-rank [[Thunderstrike]] as an innate spell at will, using your spell DC.

The cloud that covered the creature remains until the end of the target's next turn. Any creature in the cloud is [[Hidden]], and anything outside the cloud is hidden to any creature inside the cloud.

**Heightened (+1)** The healing increases by 2d8, and the thunderstrike rank increases by 1.

**Source:** `= this.source` (`= this.source-type`)
