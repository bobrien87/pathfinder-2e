---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Only the leader of an army could wear this diamond and ruby-encrusted scabbard that somehow always remains shiny no matter how terrible the conditions. While wearing the scabbard, you feel exceptionally powerful, and you gain a +3 item bonus to Athletics checks.

When you invest the scabbard, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value. The commandant's scabbard holds one melee weapon of 1 Bulk or lighter. Whenever a weapon is drawn from the scabbard, it gains a +4 status bonus to damage for 1 round.

> [!danger] Effect: Commandant's Scabbard

**Activate—Commanding Draw** `pf2:1` (fortune)

**Frequency** once per hour

**Requirements** You have a weapon sheathed in your commandant's scabbard

**Effect** You Interact to draw your weapon from your scabbard and Strike with it. On that Strike, you can roll twice and take the better result.

> [!danger] Effect: Commanding Draw

**Source:** `= this.source` (`= this.source-type`)
