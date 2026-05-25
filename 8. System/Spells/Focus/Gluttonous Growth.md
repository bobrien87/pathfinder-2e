---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Plant]]", "[[Ranger]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "1 minute (sustained)"
requirements: "squares contain plants"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Plants in the area grow rapidly, taking on carnivorous characteristics as they seek to consume prey. All affected squares are difficult terrain, both on the ground and for flying creatures. Each creature that begins its turn in the area must attempt a Reflex save unless it's already [[Grabbed]] or [[Restrained]].

When you Sustain this spell, each creature grabbed or restrained by the plants takes 4d6 piercing damage.
- **Critical Success** The creature is unaffected.
- **Success** The creature is grabbed until the beginning of its next turn or it Escapes.
- **Failure** The creature is grabbed until the spell ends or it Escapes.
- **Critical Failure** The creature is restrained until the spell ends or it Escapes.

**Heightened (+1)** The damage dealt by the plants when you Sustain the spell increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
