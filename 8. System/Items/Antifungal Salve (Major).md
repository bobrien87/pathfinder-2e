---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 675}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This foul-smelling pink paste is traditionally kept in a tightly sealed jar. Spreading the salve on exposed skin grants a +4 item bonus to saving throws against all afflictions that have the fungus trait or that originate from creatures with the fungus trait. The bonus lasts for 6 hours.

When you apply the salve, the target can immediately attempt a saving throw against one fungal affliction of 14th level or lower that is affecting them. If they succeed, the affliction is neutralized.

> [!danger] Effect: Antifungal Salve

**Source:** `= this.source` (`= this.source-type`)
