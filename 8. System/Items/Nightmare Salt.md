---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Ingested]]", "[[Poison]]"]
price: "{'gp': 14000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This potent poison consists of crystals whose flavor and appearance mimics edible salt but whose effects are deadly; victims experience periods of waking nightmares that overload the senses and eventually result in death through a combination of shock and exhaustion.

**Saving Throw** DC 43 [[Fortitude]] save

**Onset** 1 hour

**Maximum Duration** 5 days

**Stage 1** [[Frightened]] 2 once every 1d4 hours, plus [[Fatigued]] (1 day)

**Stage 2** [[Confused]] for 1 minute once every 1d4 hours, plus [[Frightened]] 3 and fatigued (1 day)

**Stage 3** frightened 3, plus confused for 1d4 minutes, once every hour, plus fatigued (1 day)

**Stage 4** death

**Source:** `= this.source` (`= this.source-type`)
