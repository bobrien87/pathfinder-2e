---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
cast: "4 hours"
area: "50-foot emanation"
targets: "all food and drink in the area"
duration: "1 month"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

An army marches on its stomach, and a city under siege is often cut off from its normal food supplies, so preserving comestibles is of utmost importance during a prolonged conflict. You enchant food and water in the area to not decay or spoil for the duration and grant better nourishment according to the success of the ritual. At the end of the duration, the food and water return to the state they were before the ritual.
- **Critical Success** A single meal of the affected food contains enough nourishment to sustain a typical human for 3 days.
- **Success** A single meal of the affected food contains enough nourishment to sustain a typical human for 1 day.
- **Failure** The ritual has no effect.
- **Critical Failure** The food and water in the area rots and spoils rapidly, releasing noxious fumes. Each living creature in the area becomes [[Sickened]] 2 and can't reduce the value of this condition for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
