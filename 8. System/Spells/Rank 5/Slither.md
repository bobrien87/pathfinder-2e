---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Shadow]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A mass of snakes made of shadow rise up to capture creatures in the area. Each creature in the area when you Cast the Spell takes 3d6 piercing damage and 1d6 persistent,poison damage from a biting snake, and it's [[Grabbed]] or [[Restrained]] depending on its Reflex save. A creature that ends its turn in the area must also attempt this save, even if it's already grabbed or restrained by the snakes. You can Dismiss the spell.
- **Success** The creature is unaffected.
- **Failure** The creature takes full damage and is grabbed by a snake. The snakes' [[Escape]] DC is equal to your spell DC. A creature can attack a snake to release the creature. A snake's AC is equal to your spell DC, and it's destroyed if it takes 12 or more damage at once. New snakes continually regrow as long as the spell lasts, so destroying snakes doesn't prevent slither from capturing more creatures.
- **Critical Failure** As failure, but the creature takes double damage and is restrained by a snake.

**Heightened (+2)** The persistent poison damage increases by 1d6 and snake HP increases by 6.

**Source:** `= this.source` (`= this.source-type`)
