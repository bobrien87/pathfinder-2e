---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]", "[[Mythic]]", "[[Sanctified]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You don a diadem of radiant light, which sheds bright light to a range of 60 feet and dim light to a further 60 feet. When you Cast the Spell and when you Sustain it during the duration, you can draw a disc of spiraling light from the diadem and throw it at a creature within 120 feet. Make a ranged spell attack at mythic proficiency against the target's AC. This action has the attack and spirit traits. On a hit, you deal 4d8 spirit damage, 1d4 persistent spirit damage, and the target is [[Dazzled]] for 1 round (3 rounds on a critical hit). The persistent damage isn't doubled on a critical hit.

If the disc passes through an area of magical darkness or targets a creature affected by magical darkness, the disc's glow attempts to counteract the darkness using your Religion or Occultism skill modifier as the counteract check modifier and half your level as the counteract rank.

> [!danger] Effect: Spell Effect: Diadem of Divine Radiance

**Heightened (+2)** The disc's spirit damage increases by 2d8, and the persistent damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
