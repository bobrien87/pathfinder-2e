---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 20]]"]
price: "{'gp': 430}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #208: Hoof, Cinder, and Storm"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *returning throwing knife* is specially made for Lyrune-Quah hunters, and its blade is carved with constellations.

**Ribbon Wrap** `pf2:r` (concentrate)

**Frequency** once per hour

**Trigger** You deal damage to a target with the starknife

**Effect** Silver ribbons of starlight entangle the target, dealing 4d6 spirit damage. This is silver damage for the purposes of weaknesses, resistances, and the like. The target must attempt a DC 24 [[Reflex]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Clumsy]] 1.
- **Failure** The creature takes full damage and is [[Immobilized]] for 1 round.
- **Critical Failure** The creature takes full damage and is [[Restrained]] with an [[Escape]] DC of 24.

**Source:** `= this.source` (`= this.source-type`)
