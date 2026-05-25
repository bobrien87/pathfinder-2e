---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 100}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This porcelain or alabaster mask portrays an angelic visage of kindness and mercy. The mask grants a +1 item bonus to Medicine checks.

**Activate** `pf2:f` (concentrate, fortune)

**Frequency** once per day

**Trigger** You are about to roll a variable number of Hit Points you restore from an action with the healing trait

**Effect** Roll twice to determine the number of Hit Points you restore and take the higher result.

**Source:** `= this.source` (`= this.source-type`)
