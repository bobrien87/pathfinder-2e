---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Select an elemental trait: air, earth, fire, metal, water, or wood. *Elemental zone* gains the trait you chose. You imbue the area with the raw energy of that element, creating a zone that emits and amplifies magic of that type. The temperature might suddenly rise or fall, a storm cloud might form, and so on. Spells with the chosen elemental trait cast against creatures in the zone get a +2 status bonus to one damage type the spell deals based on the chosen trait: bludgeoning or electricity for air, bludgeoning for earth, fire for fire, electricity or slashing damage for metal, bludgeoning or cold for water, and bludgeoning or vitality damage for wood. The caster chooses one type to add the bonus to if the spell deals more than one eligible type. This bonus is halved if the spell didn't use a spell slot (such as a cantrip, focus spell, or innate spell).

The zone has no effect on the spell if the spell doesn't deal any damage of an eligible type.

**Heightened (+2)** The status bonus increases by 1.

**Source:** `= this.source` (`= this.source-type`)
