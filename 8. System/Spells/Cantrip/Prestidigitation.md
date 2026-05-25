---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "10 feet"
targets: "1 object (cook, lift, or tidy only)"
duration: "sustained"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The simplest magic does your bidding. You can perform simple magical effects for as long as you Sustain the spell. Each time you Sustain the spell, you can choose one of four options.

- **Cook** Cool, warm, or flavor 1 pound of nonliving material.
- **Lift** Slowly lift an unattended object of light Bulk or less 1 foot off the ground.
- **Make** Create a temporary object of negligible Bulk, made of congealed magical substance. The object looks crude and artificial and is extremely fragile-it can't be used as a tool, weapon, or locus or cost for a spell.
- **Tidy** Color, clean, or soil an object of light Bulk or less. You can affect an object of 1 Bulk with 10 rounds of concentration, and a larger object at 1 minute per Bulk.

*Prestidigitation* can't deal damage or cause adverse conditions. Any actual change to an object (beyond what is noted above) persists only as long as you Sustain the spell.

**Source:** `= this.source` (`= this.source-type`)
