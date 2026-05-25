---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 piercing or slashing weapon you're wielding"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You place a drop of your blood on a weapon and charge it with magic so that you transfer a small amount of your life essence with your attack. The next creature you successfully Strike with the weapon during the spell's duration takes damage as normal from the attack and must then attempt a Will save; regardless of the outcome of this saving throw, the duration of mark of blood ends. You can have up to one creature cursed by mark of blood at any one time. If you use this spell to mark a different creature, the curse afflicting the previous creature ends.
- **Critical Success** The creature is unaffected.
- **Success** The creature gains a softly glowing mark that resembles Achaekek's symbol somewhere on their body (such as the forehead or back of the hand). This mark can be [[Concealed]] by clothing, but is otherwise permanent until the curse is removed.
- **Failure** As success, but you can [[Seek]] to attempt to know the direction and general distance (within a mile) to the marked creature if the creature is alive and both you and the creature are on the same plane of existence. When you Seek in this way, you attempt a Perception check against the marked creature's Will DC. On a success, you gain the information, which is accurate at the moment that you Seek. On a critical failure, the curse ends, and the creature's mark vanishes.
- **Critical Failure** As failure, but your Perception checks to Seek the marked creature are automatically successful.

**Source:** `= this.source` (`= this.source-type`)
