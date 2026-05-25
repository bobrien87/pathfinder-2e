---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Grimoire]]", "[[Incapacitation]]", "[[Magical]]", "[[Shadow]]", "[[Teleportation]]"]
price: "{'gp': 21000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Shadows swirl around this soot-black tome, swallowing up any light that touches them. A faint whispering emanates from the grimoire's pages when opened.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Trigger** Your last action was to cast a spell prepared from this grimoire that has the shadow trait

**Effect** Your shadow, and that of the tome, elongates and reaches hungrily for one foe within 30 feet, who must attempt a [[Fortitude]] save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Blinded]] for 1 round and [[Drained]] 1 as the shadows scrape across it.
- **Failure** The creature is blinded for 1 minute and [[Drained]] 2 as the shadows seize it.
- **Critical Failure** As failure, but the shadows also pull the creature into the tome, teleporting it to the Netherworld.

**Source:** `= this.source` (`= this.source-type`)
