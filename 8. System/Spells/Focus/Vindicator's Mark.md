---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Focus]]", "[[Manipulate]]", "[[Sanctified]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "your hunted prey"
duration: "1 minute"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You launch a magical dart at your hunted prey, which marks them with a nimbus only you can detect. Make a spell attack against the target. On a hit, you deal 2d4 spirit damage and the target is marked by a glowing nimbus of energy that only you can see. For the duration of your spell, the marked target takes an additional +2 damage from all your weapon or unarmed attacks. [[Invisible]] targets marked by your *vindicator's mark* are [[Concealed]] to you, rather than [[Undetected]].

You can Dismiss the spell on your turn if your last action dealt damage to the target with a weapon or unarmed attack, instantly dealing an additional @Damage[(ceil(@item.rank/2)+1)d6[spirit]] damage to it.

> [!danger] Effect: Spell Effect: Vindicator's Mark

**Heightened (+2)** The initial damage increases by 2d4, the additional damage you deal increases by 1, and the damage dealt when the spell is Dismissed increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
