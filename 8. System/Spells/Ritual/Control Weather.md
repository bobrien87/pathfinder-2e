---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
cast: "1 day"
duration: "4d12 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 2-mile-radius circle centered on you

You alter the weather, making it calm and normal for the season or choosing up to two effects based on the season.

- **Spring** drizzle, heat, hurricane, sleet, thunderstorm, tornado

- **Summer** drizzle, downpour, extreme heat, hail, heat

- **Autumn** cold weather, fog, mild heat, sleet

- **Winter** blizzard, mild cold, extreme cold, thaw

You can't specifically control the manifestations, such as the exact path of a tornado or the targets of lightning strikes.
- **Critical Success** You change the weather as desired and can affect a larger area (up to a 5-mile-radius circle), or a longer duration (any number of additional d12 hours, up to 16d12).
- **Success** You change the weather as desired.
- **Failure** You fail to change the weather as desired.
- **Critical Failure** The weather changes in an unanticipated way, determined by the GM but generally as contradictory to your true desires as possible (for instance, a terrible storm emerges when you would prefer good weather).

**Heightened (9th)** You can create unseasonable weather and contradictory weather effects, such as extreme cold and a hurricane. You can make the weather calm and normal weather for a different season or choose weather effects from any season's list.

**Source:** `= this.source` (`= this.source-type`)
