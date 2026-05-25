---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 70000}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Constructed of dull gray metal, this breastplate is decorated with the symbol of a craggy black mountaintop. This breastplate functions as a *+3 greater resilient breastplate*. When you're Shoved or otherwise forced to move, you can reduce the amount you move by up to 10 feet. When you invest the breastplate, you either increase your Constitution modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You pound a solid and constant rhythm on your breastplate and cast a 7th-rank regeneration spell on yourself.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** With a single tap, you gain immunity to poison for 1 minute.

> [!danger] Effect: Breastplate of the Mountain

**Activate** R (concentrate)

**Frequency** once per day

**Trigger** You fail or critically fail a Fortitude saving throw

**Effect** If you failed the saving throw, it becomes a success. If you critically failed, it becomes a failure instead.

**Source:** `= this.source` (`= this.source-type`)
