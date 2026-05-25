---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 21}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A victim of clown monarch is amusing to behold as they repeatedly suffer slapstick pratfalls. This poison disrupts the victim's sense of balance.

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** falls [[Prone]] and must succeed at a DC 5 flat check when attempting a Stand action or the action fails and is lost (1 round)

**Stage 2** as stage 1 but the DC is 10 (DC 10 flat check) (1 round)

**Stage 3** as stage 1 but the DC is 15 (DC 15 flat check) (1 round)

**Source:** `= this.source` (`= this.source-type`)
