---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 70}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This tiny capsule of soluble material is filled with a flavorless clear powder mixed with thousands of microscopic eggs laid by insidious parasites known as sportlebores. If the capsule or its contents are swallowed by an unwitting victim, the eggs rapidly hatch inside their unfortunate host, causing great abdominal pain. The target can't recover from the poison's enfeebled or sickened condition except by magic. After stage 3, the target returns to stage 1, but if it progresses to stage 3 a second time, the damage is doubled.

**Saving Throw** DC 22 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 6 minutes

**Stage 1** [[Sickened]] 1 (1 minute)

**Stage 2** [[Enfeebled]] 1 and sickened 1 (1 minute)

**Stage 3** 4d6 bludgeoning damage (DC 23 [[Fortitude]] save) and [[Enfeebled]] 2 as the affected target painfully vomits (1 minute)

**Source:** `= this.source` (`= this.source-type`)
