---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Light]]", "[[Visual]]"]
price: "{'gp': 450}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This metallic tube has a complex array of lenses and prisms at one end and a hatch at the other. The hatch can be unlocked, loaded with a [[Glow Rod]], and refastened using 3 Interact actions.

**Activate** `pf2:1` (manipulate)

**Requirements** A glow rod is installed in the dazzler

**Effect** The glow rod burns to dust in a single focused flash, creating a @Template[type:cone|distance:30] of scintillating light. Each creature in the cone must attempt a DC 24 [[Fortitude]] save, with the following effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round or until it spends an Interact action to rub its eyes, ending the blinded condition.
- **Critical Failure** The creature is blinded for 1 round.

**Source:** `= this.source` (`= this.source-type`)
