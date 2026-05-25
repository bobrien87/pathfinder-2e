---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Psychic]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You telekinetically animate a weapon that's unattended or on your person. It brandishes itself at a foe of your choice as if wielded by an invisible duelist. When you first Cast the Spell, the weapon automatically flies to the target and Strikes. It moves along with its target, always remaining within reach. Each time you Sustain the Spell, the weapon either Changes Partners or Strikes. The weapon's attacks use and contribute to your multiple attack penalty.

- **Change Partners** Change the weapon's target to a different creature within 30 feet. The weapon flies to its new target.
- **Strike** (attack) The weapon attacks its target using your spell attack modifier. On a hit, the weapon deals 3d6 damage, of a type determined by the weapon (if the weapon has the versatile trait or can otherwise deal multiple types of damage, you choose each time you attack).

**Heightened (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
