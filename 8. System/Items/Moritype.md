---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Gadget]]", "[[Void]]"]
price: "{'gp': 200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This plate of smoky glass is a variation on Dr. Krasovna Gerenevich's krasovnatype that is imprinted with void energies. Creating the plate requires a living thing to die as part of its electrical charging; most creators use insects or lab mice. The moritype creates an image in the same way as a krasovnatype, but also siphons off part of that aura. If used on a living creature, that creature must attempt a DC 27 [[Will]] save.
- **Critical Success** The creature is unaffected.
- **Success** If the creature has any innate, prepared, or spontaneous spells, they're unable to Cast a Spell of their highest-ranked slot for 1 round. Cantrips and focus spells are unaffected.
- **Failure** As success, except they can't cast the 2 highest ranks they have available.
- **Critical Failure** As success, except they can't cast any spells other than cantrips and focus spells.

**Source:** `= this.source` (`= this.source-type`)
