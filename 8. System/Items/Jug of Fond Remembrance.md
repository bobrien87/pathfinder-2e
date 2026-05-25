---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'gp': 75}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large jug always seems to contain just enough of the holder's favorite alcohol to share with a friend. As long as you're holding the jug, you gain a +1 circumstance bonus to Diplomacy checks. If you share a sip of the liquor from the jug with a creature, you gain a +2 circumstance bonus to your next Diplomacy check to [[Make an Impression]] or [[Request]] something from that creature any time within the next month.

**Activate** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You take a long swig on the jug and then [[Recall Knowledge]] about a creature you can see, with a +2 circumstance bonus to the check. If you fail but don't critically fail this check, you get a success instead. You're then [[Stupefied 1]] for 3 rounds.

**Source:** `= this.source` (`= this.source-type`)
