---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
defense: "Will"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A flowing cloak of utter darkness drapes over you, filled with pinpricks of light like distant stars. It imparts the stillness of the cosmos to you, granting you a +2 status bonus to Stealth checks to [[Hide]] and [[Sneak]].

While outside under a starry night sky, you're also [[Invisible]] as long as you remain still. When moving under a starry night sky, you're [[Concealed]] instead.

Gazing too closely into the stars is disorienting. Any creature that ends its turn adjacent to you must attempt a Will save; this is a mental, visual effect.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Dazzled]] until the end of its next turn.
- **Critical Failure** The creature is [[Confused]] and dazzled until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
