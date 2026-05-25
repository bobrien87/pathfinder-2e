---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Death]]", "[[Mythic]]"]
cast: "8 hours"
range: "10 feet"
area: "1000-foot burst"
duration: "1 week"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Lo, speak of the hero-gods and their ash-strewn endings! Sing of their might as it falls on the land! Taste the bone and char that binds their life to yours! This ritual focuses on the burning of a mythic creature's corpse on a pyre in an outdoor location. Once the corpse has been reduced to ashes, the wind scatters those ashes across a 1,000-foot radius. As the ash lands on creatures within this radius, a fragment of the dead creature's mythic power flows into them.
- **Critical Success** Death has a lessened claim upon those in the ritual's area of effect. All creatures that were of a level equal to or lower than the level of the mythic creature incinerated as part of the ritual gain resistance 10 to void damage and a +2 status bonus to saving throws against death effects and to recovery checks.
- **Success** As critical success, but only as long as the creature remains in the ritual's area.
- **Failure** The ritual has no effect.
- **Critical Failure** Grief washes over the area, and the threat of death looms more closely over the casters, who all gain weakness 10 to void damage and a –2 status penalty to saving throws against death effects and to recovery checks. This is a curse effect.

> [!danger] Effect: Spell Effect: Ash Strewn Ending

**Heightened (6th)** The area increases to a 1-mile radius, the duration increases to 1 month, the void resistance (or weakness) increases to 15, and the status bonus (or penalty) increases to +3.

**Heightened (8th)** The area increases to 10 miles, the duration increases to 1 year, the void resistance (or weakness) increases to 20, and the status bonus (or penalty) increases to +4.

**Heightened (10th)** As 8th rank, but one GM-selected non-mythic creature in the area becomes mythic. This creature's attitude and personality is favorable toward the primary caster.

**Source:** `= this.source` (`= this.source-type`)
