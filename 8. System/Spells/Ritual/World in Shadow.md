---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Darkness]]", "[[Mythic]]"]
cast: "8 hours"
range: "8-mile radius circle centered on you"
duration: "5 days"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

This ritual must be cast at night, at which point darkness becomes everlasting. Casters with darkvision gain a +1 circumstance bonus to their check to cast the ritual.
- **Critical Success** As success, except that all light levels within the area are lowered by two steps toward darkness, and light effects that would counteract the darkness take a –2 status penalty to their counteract checks.
- **Success** All light levels within the area are lowered by one step toward darkness. Areas that are already dark become magical darkness. Light effects that would counteract the darkness only do so in the area of the counteracting spell or effect (for example, 40 feet for a [[Light]] spell).
- **Failure** The ritual has no effect.
- **Critical Failure** The casters are all plunged into their own personal darknesses. For 1 week, each caster can see no farther than 5 feet regardless of ambient light level. Anything beyond that distance is treated as if it were in magical darkness that can't be counteracted; darkvision and greater darkvision similarly can't penetrate this darkness.

**Source:** `= this.source` (`= this.source-type`)
