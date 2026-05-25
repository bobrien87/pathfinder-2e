---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Detection]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You attune yourself to magnetic fields, becoming aware of the presence or absence of metallic objects, veins, and deposits within the area. You can choose to ignore metal you're fully aware of, such as the gear you and your allies wear and carry.

You detect metal hidden by illusions (such as [[Invisibility]]) only if the illusion has a lower rank than your *detect metal* spell. Against deceptive illusions, *detect metal* always notices an absence of metal when a non-metallic object is disguised as metallic. However, if the deception involves disguising one metallic object as another, such as pretending a copper coin is made of gold, *detect metal* registers only the presence of metal, not its type, even if the rank of your *detect metal* spell exceeds that of the illusion effect.

**Heightened (3rd)** You can discern all types of metal you detected. Your spell can overcome deceptive illusory spells hiding one metal as another if the magic effect's rank is lower than that of your *detect metal* spell.

**Source:** `= this.source` (`= this.source-type`)
