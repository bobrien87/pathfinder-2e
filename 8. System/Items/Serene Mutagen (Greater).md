---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Elixir]]", "[[Mutagen]]", "[[Polymorph]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (manipulate)

You gain inner serenity, but you find violence off-putting.

**Benefit** You gain a +3 item bonus to Will saves and Perception, Medicine, Nature, Religion, and Survival checks. This bonus improves to +4 when you attempt Will saves against mental effects. When you roll a success on a Will save against a mental effect, you get a critical success instead.

**Drawback** You take a -1 penalty to attack rolls and save DCs of offensive spells, and a -1 penalty per damage die to all weapon, unarmed attack, and spell damage.

**Duration** 1 hour.

> [!danger] Effect: Serene Mutagen (Greater)

**Source:** `= this.source` (`= this.source-type`)
