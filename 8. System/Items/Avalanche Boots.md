---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 15000}"
usage: "wornshoes"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While the insides of these boots are comfortable, fur-lined leather, the outsides are a jumble of slate plates, giving the impression of a rockslide. You gain a +3 item bonus to Athletics checks and a +2 circumstance bonus to [[Force Open]] and [[Shove]]. When you invest the boots, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You succeed or critically succeed with a Shove

**Effect** If the Shove was a success, you push your opponent up to 10 feet instead of 5 feet. If the Shove was a critical success, you push your opponent up to 20 feet, and you can then choose to knock them [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
