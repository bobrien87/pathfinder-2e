---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Concentrate]]", "[[Force]]", "[[Magical]]", "[[Manipulate]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 15000, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand features a carved dragon's head at its top and a polished metal sphere set in its midsection.

**Activate** Cast a Spell

**Frequency** Once per day, plus overcharge

**Effect** You cast [[Force Barrage]] at 7th rank.

After you cast the spell, an additional shard or shards are released from the wand at the start of each of your turns, as though you cast the 1-action version of *force barrage*. Choose targets each time. This lasts for 1 minute, until you're no longer wielding the wand, or until you try to activate the wand again.

**Craft Requirements** Supply a casting of *force barrage* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
