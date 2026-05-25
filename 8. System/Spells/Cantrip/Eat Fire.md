---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:r`"
duration: "until the end of your next turn"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You would take fire damage.

You consume and ingest fire, making it less harmful to you. You gain resistance 5 to fire damage until the end of the current turn. During the remaining duration of the spell, you can use the Belch Smoke action. The spell ends if you fall [[Unconscious]], inhale, or exhale (this includes speaking).

> [!danger] Effect: Spell Effect: Eat Fire

**Belch Smoke** `pf2:1` You exhale what remains of the smoke, ending the spell and creating a smoke cloud in a @Template[burst|distance:5] within 20 feet. All creatures within the smoke cloud are [[Concealed]], and all other creatures are concealed to them. The smoke lasts for 1 minute or until dispersed by a strong wind.

**Heightened (+3)** The resistance increases by 5.

**Source:** `= this.source` (`= this.source-type`)
