---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Darkness]]"]
cast: "4 hours"
range: "1,000 feet"
area: "200-foot burst"
duration: "1 hour"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a squadron of shadows to surge forth and plunge your enemies into darkness. All non-magical light sources in the area are extinguished and can't be lit again during the duration. Any dim light from sources outside the area can't penetrate the area, and sources of bright light from outside the area shed only dim light into the area. The shadows also attempt to counteract any magical light in the area, with a counteract rank of 2 and a counteract modifier of +13. If a new magical light effect enters the area during the duration, the shadows immediately attempt to counteract it.
- **Critical Success** The shadows are particularly powerful. Their counteract rank increases by 1, and they gain a +2 circumstance bonus to their counteract check.
- **Success** The shadows are of normal power.
- **Failure** The ritual has no effect.
- **Critical Failure** The shadows instead cling to you and obscure your vision, rendering you [[Blinded]] for 24 hours.

**Heightened (4th)** The shadows have a counteract rank of 4 and a counteract modifier of +18.

**Heightened (6th)** The shadows have a counteract rank of 6 and a counteract modifier of +24.

**Heightened (8th)** The shadows have a counteract rank of 8 and a counteract modifier of +29.

**Source:** `= this.source` (`= this.source-type`)
