---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Disease]]"]
cast: "4 hours"
range: "touch"
targets: "10 pieces of siege weapon ammunition, such as a ballista bolt or catapult stone"
duration: "1 hour"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You imbue several pieces of siege weapon ammunition with an infectious disease that can bring an opposing force low over time. Once the ritual is successfully concluded, the affected pieces of ammunition glow a sickly green and must be launched within the hour or the enchantment fades. In addition to its normal damage or other effects, a successful attack with a piece of the affected ammunition exposes every creature within a 60-foot-radius emanation from the point of impact to siege sickness.

**Siege Sickness** (disease) Level 8

**Saving Throw** DC 24 [[Fortitude]] save

**Onset** 1 day

**Stage 1** [[Sickened]] 2 (1 day)

**Stage 2** [[Enfeebled]] 1 and sickened 2 (1 day)

**Stage 3** [[Enfeebled]] 2 and [[Sickened]] 3 (1 day)

**Stage 4** [[Enfeebled]] 3, sickened 3, and a creature who comes into physical contact with the afflicted is exposed to siege sickness (1 day)

**Stage 5** death, and a creature who comes into physical contact with the corpse is exposed to siege sickness
- **Critical Success** The siege sickness gains the virulent trait.
- **Success** The siege sickness is normal.
- **Failure** The ritual has no effect.
- **Critical Failure** Instead of being imbued in the ammunition, the disease becomes airborne at the site of the ritual. Each creature within a 60-foot emanation centered on the primary caster is exposed to siege sickness at stage 2.

**Source:** `= this.source` (`= this.source-type`)
