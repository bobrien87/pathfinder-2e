---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Fungus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Tanglebriar has been called a "curse on the land," which has inspired Treerazer's cult to develop this notorious spell. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** A fungal bloom springs up from the ground in a @Template[type:emanation|distance:5] around the target. This area is difficult terrain for creatures that enter the area. The target treats all terrain as difficult terrain since this swath of fungus moves with them as they do, transforming into a tangle of spores and floating tendrils if the target flies or a thick swath of stringy floating algae if the target swims. This effect ends after 1 minute or as soon as the curse is lifted, whichever comes first.
- **Failure** As success, but the fungal bloom increases to 10 feet. It persists until the curse is lifted. In addition, the target is also affected by the spores exuded by the fungal bloom—roll `r 1d4` and consult the results below to see how the spores affect them. This affect reactivates automatically every 24 hours, replacing the previous result.

**1:** The spores cause atrophy; the target is [[Enfeebled]] 1.

**2:** The spores cause fibrous fungal growths to sprout from the target; the target is [[Clumsy]] 1.

**3:** The spores settle in the target's blood and flesh and cause great pain; the target is [[Drained]] 1.

**4:** The spores intrude upon the mind and cause hallucinations; the target is [[Stupefied 1]].
- **Critical Failure** As failure, but the emanation increases to 15 feet, and the condition value caused by the spores increases to 2.

**Source:** `= this.source` (`= this.source-type`)
