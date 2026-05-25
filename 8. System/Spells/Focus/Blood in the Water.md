---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Spirit]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature that can bleed"
defense: "basic Reflex"
duration: "1 minute (sustained)"
requirements: "The target is taking persistent bleed damage or your last action dealt slashing damage to the target."
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** The target is taking persistent bleed damage or your last action dealt slashing damage to the target.

Predators are drawn to the scent of blood, and blood can disperse shockingly far in the water. You summon the spirits of aquatic predators to appear as a spectral swarm around the target. When you Cast or Sustain this Spell, the target takes 2d6 spirit damage (basic Reflex save). If the target takes any damage from the spell, it treats all water as difficult terrain for 1 round as the predators try to drag them down. The spectral predators don't take up space, grant flanking, or have any other attributes a creature would. If you deal slashing damage to the target while the spell is active, you automatically Sustain this Spell. If you cast blood in the water while a previous casting of this hex is still in effect, the previous effect ends.

**Heightened (+2)** The damage dealt increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
