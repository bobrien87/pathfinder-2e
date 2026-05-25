---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Alchemical]]", "[[Bomb]]", "[[Consumable]]", "[[Light]]"]
price: "{'gp': 3}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Strike

This vial of glowing goo constantly sheds dim light in a 10-foot radius. When a bioluminescence bomb strikes a creature or a hard surface, it shatters and releases the bioluminescent fluid's energy in a flare of light. Each creature within @Template[burst|distance:10]{10 feet} of where the bomb exploded must succeed at a DC 17 [[Reflex]] save or be marked with dye that continues to glow for 24 hours. An affected creature must also attempt a DC 17 [[Fortitude]] save saving throw against the overwhelming burst of light.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Dazzled]] for 1 round.
- **Critical Failure** The creature is [[Blinded]] for 1 round, then dazzled for 1 round.

**Source:** `= this.source` (`= this.source-type`)
