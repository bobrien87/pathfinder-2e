---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "up to 6 creatures"
defense: "Will"
duration: "until the end of your next turn"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You utter a powerful secret at odds with the fundamental nature of the target creatures. Choose a specific resistance or weakness with a numerical value that you believe one or more of the targets have due to [[Recall Knowledge]] or previous experience with the targets, such as resistance to fire or weakness to silver. If the information is incorrect for a given target, the spell has no effect on that target. Affected targets must attempt a Will saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 1 damage that matches the type or trait of weakness you chose (thus triggering the creature's weakness) if you chose a weakness, or loses its resistance until the end of your next turn if you chose a resistance.
- **Failure** As success, and the creature becomes [[Frightened]] 1 from the revelation of its dread secret.
- **Critical Failure** As failure, except the creature is [[Frightened]] 3

**Source:** `= this.source` (`= this.source-type`)
