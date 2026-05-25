---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 14}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The euphemistically named saboteur's friend looks, smells, and tastes like an appetizing chocolate square. You lace the chocolate with reagents that induce a strong laxative effect. Saboteur's friend is useful for incapacitating rather than dealing lasting harm. Unlike some poisons, saboteur's friend can have its sickened condition reduced (but changing to a higher or lower stage after a save applies any sickened condition listed for that stage, as normal).

**Saving Throw** DC 20 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 1 hour

**Stage 1** [[Sickened]] 1 (10 minutes)

**Stage 2** [[Enfeebled]] 1 and [[Sickened]] 2 (10 minutes)

**Stage 3** enfeebled 1, [[Fatigued]], and [[Sickened]] 3 (10 minutes)

**Source:** `= this.source` (`= this.source-type`)
