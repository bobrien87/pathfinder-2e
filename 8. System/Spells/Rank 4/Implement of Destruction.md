---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 enemy, and 1 weapon that is either unattended or wielded by you or a willing ally"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You solemnly declare that the target weapon will bring death to a foe, implanting an irrational fear of the weapon into the target enemy's mind. This link echoes at the forefront of the enemy's mind, forming a looming sense of omnipresent dread. The effect is based on the target enemy's Will save.
- **Critical Success** The target enemy is unaffected.
- **Success** The target weapon deals an additional 2d6 mental damage the first time it hits the target enemy before the end of the spell's duration.
- **Failure** The target weapon deals an additional 2d6 persistent,mental damage to the target enemy. If the enemy is critically hit by the weapon, the enemy is [[Doomed]] 1 for as long as it takes this persistent mental damage.
- **Critical Failure** The target weapon deals an additional 4d6 persistent,mental damage to the target enemy. If the enemy is critically hit by the weapon, the enemy is doomed 1.

**Heightened (+2)** Increase the mental damage by 1d6 on a success, and increase the persistent mental damage by 1d6 on a failure or by 2d6 on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
