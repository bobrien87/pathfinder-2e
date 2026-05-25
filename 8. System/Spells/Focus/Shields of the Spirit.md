---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Champion]]", "[[Concentrate]]", "[[Focus]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:1`"
requirements: "You are wielding a shield."
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You are wielding a shield.

You Raise your Shield, causing ephemeral spirit shields to float within your champion's aura. The shields last until the start of your next turn or until you're no longer raising your shield, whichever comes first. While one of your allies is in your champion's aura, the shields grant them a +1 status bonus to AC, and each time an enemy makes an attack against the ally, the enemy takes 1d4 spirit damage (even if it misses).

The benefit applies only while an ally is in your aura, ending for any ally that leaves and applying to any that enters later. As normal, you don't count as your own ally and therefore don't get the benefits of the spirit shields yourself.

> [!danger] Effect: Spell Effect: Shields of the Spirit

**Heightened (+2)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
