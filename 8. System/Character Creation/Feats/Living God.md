---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Razmiran Priest|Razmiran Priest]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Razmiran Priest Dedication, legendary in Crafting"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have reached heights of power equaling Razmir himself. You can Craft your [[Razmiri Mask]] out of porcelain laced with precious metals, or upgrade your existing mask to a porcelain one in the same time it takes to Craft one made of iron. A Porcelain Razmiri Mask grants a +4 item bonus to Deception checks to [[Lie]] or [[Feint]], is an 18th-level item, and is an apex item that increases your Charisma modifier by 1 or increases it to +4, whichever would give you a higher score. It also gives you the following activation in addition to those granted by the standard, silver, and gold masks.

**Activate—Power of the Living God** `pf2:1` (concentrate, manipulate, occult)

**Frequency** once per day

**Effect** You demand power from the world, using your mask as a locus to force reality to bend to your will. You cast [[Manifestation]] as a 10th-rank occult spell, but no matter what spell you emulate with it, that spell has the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
