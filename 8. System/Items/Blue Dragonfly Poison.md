---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 7}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Boggards brew a potent toxin made from blue dragonflies. Swampseers consume this mixture to awaken their divine powers, but the poison causes debilitating hallucinations in most other creatures.

**Saving Throw** DC 17 [[Fortitude]] save

**Onset** 10 minutes

**Maximum Duration** 30 minutes

**Stage 1** [[Dazzled]] (10 minutes)

**Stage 2** dazzled and [[Frightened]] 1 (10 minutes)

**Stage 3** frightened 1 and [[Confused]] 1 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
