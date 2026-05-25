---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Fear]]", "[[Focus]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
area: "5-foot emanation"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a wave of the hand, you cause all creatures in the area to see the world around them as if a gauzy film had been lifted away to expose the truth that lies below their perceived reality. Natural features they can see grow twisted and horrendous, structures appear distorted and ruined, and objects seem warped and alien. This alternate vision fades quickly, but the glimpse beyond the natural world lingers for the spell's duration.

Aberrations or worshippers of Outer Gods or Great Old Ones are bolstered by this vision of warped reality and gain a +1 status bonus to Will saving throws and attack rolls for 1 minute, while all other creatures must attempt a Will saving throw.

> [!danger] Effect: Spell Effect: Lift Nature's Caul (Bonus)
- **Critical Success** The creature is unaffected and temporarily immune for 1 hour.
- **Success** The creature is [[Sickened]] 1.
- **Failure** The creature is [[Stupefied 1]] for 1 minute and [[Frightened]] 1.
- **Critical Failure** The creature is stupefied 1 for 1 minute and [[Frightened]] 2. It can't reduce the value of its frightened condition below 1 as long as it remains stupefied by this spell.

**Heightened (+2)** The area increases by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
