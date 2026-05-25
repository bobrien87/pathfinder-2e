---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Lozenge]]"]
price: "{'gp': 40}"
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

Students in Katapesh first used scholar's drop to gain an academic edge, but this hard, sugar-soated candy has since spread across Golarion. Its lemon and green tea flavor adds to its refreshing qualities. For 1 hour, you gain a +1 item bonus to saving throws against effects that could render you [[Fatigued]].

**Secondary Effect** `pf2:1`

**Requirements** You're fatigued

**Effect** Ignore the effects of the fatigued condition for 10 minutes. The drop's other effects end for you, and when the 10 minutes are up, you're temporarily immune to scholar's drops for 1 hour. If you use this effect three times in a single day, you become temporarily immune to scholar's drops entirely until you get a full night's rest.

**Source:** `= this.source` (`= this.source-type`)
